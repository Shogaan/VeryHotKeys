from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDialog, QSystemTrayIcon, QAction, qApp, QMenu
from PyQt5.QtWidgets import QMessageBox, QCheckBox, QActionGroup
from PyQt5.QtCore import Qt

from pathlib import Path

from interface import Ui_MainWindow

from add_and_edit_logic import AddAndEditWindow
from settings_logic import SettingsWindow
from profile_logic import ProfileWindow

from modes_create_logic import treat_information_for_creating

from global_definitions import read_settings_json, write_settings_json
from global_definitions import read_hotkeys_json, write_hotkeys_json

from constants import CSS_MAIN_BRIGHT, CSS_MAIN_DARK

import keyboard
import webbrowser
import asyncio
import os
import sys

dict_of_settings = read_settings_json()


class MainInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainInterface, self).__init__()
        self.setupUi(self)

        self.is_closing = False
        self.current_profile = ""

        self.tray_icon = QSystemTrayIcon(self)
        self.profiles_group = QActionGroup(self.menubar)

        self.profiles_submenu_tray = QMenu(self)
        self.profiles_submenu_tray_group = QActionGroup(self.tray_icon)

        self.profiles_group.triggered.connect(self.change_profile)
        self.profiles_submenu_tray_group.triggered.connect(self.change_profile)

        dict_of_hotkeys = read_hotkeys_json()
        for profile_name in dict_of_hotkeys:
            profile = QAction(text=profile_name)
            profile.setCheckable(True)
            if dict_of_hotkeys[profile_name]['enable']:
                self.current_profile = profile_name
                profile.setChecked(True)

            self.profiles_group.addAction(profile)
            self.profiles_menu.addAction(profile)

            # ----- Add profile in submenu for tray -----
            self.profiles_submenu_tray_group.addAction(profile)
            self.profiles_submenu_tray.addAction(profile)
            # -------------------------------------------
        del dict_of_hotkeys

        self.load_hotkeys()
        self.load_settings()

        self.plus_button.clicked.connect(self.open_add_window)
        self.minus_button.clicked.connect(self.delete)
        self.edit_button.clicked.connect(self.open_edit_window)

        self.tableWidget.cellClicked.connect(self.on_cell_changed)

        self.actionTo_tray.triggered.connect(self.hide)
        self.actionSettings_.triggered.connect(self.open_settings_window)

        self.profile_managment.triggered.connect(self.open_profile_window)

        self.actionExit.triggered.connect(self.close)

        # --------------Set tray icon---------------------
        self.tray_icon.setIcon(QIcon("images/logo2.ico"))

        show_action = QAction("Show", self)
        profiles_action = QAction("Profiles", self)
        quit_action = QAction("Exit", self)

        profiles_action.setMenu(self.profiles_submenu_tray)

        show_action.triggered.connect(self.show_main_window)

        quit_action.triggered.connect(qApp.quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(profiles_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.if_show_main_window_on_tray_click)
        self.tray_icon.show()
        # ------------------------------------------------

    # -----------------Initialization CSS-------------
    def load_settings(self):
        if dict_of_settings['theme'] == "bright":
            self.setting_bright()
        elif dict_of_settings['theme'] == "dark":
            self.setting_dark()
        else:
            dict_of_settings['theme'] = "bright"
            self.setting_bright()
            write_settings_json(dict_of_settings)

    def setting_bright(self):
        with open(CSS_MAIN_BRIGHT) as file:
            self.setStyleSheet(eval(file.read()))

        self.plus_button.setIcon(QIcon("images/plus-black.png"))
        self.minus_button.setIcon(QIcon("images/minus-black.png"))
        self.edit_button.setIcon(QIcon("images/pencil-black.png"))

    def setting_dark(self):
        with open(CSS_MAIN_DARK) as file:
            self.setStyleSheet(eval(file.read()))

        self.plus_button.setIcon(QIcon("images/plus-white.png"))
        self.minus_button.setIcon(QIcon("images/minus-white.png"))
        self.edit_button.setIcon(QIcon("images/pencil-white.png"))
    # ------------------------------------------------

    # ---------Open different windows-----------------
    def open_add_window(self):
        add_window = AddAndEditWindow(is_edit=False, profile=self.current_profile)
        add_window.setModal(True)
        dialog_window = add_window.exec_()

        dict_of_profiles = read_hotkeys_json()

        if dialog_window == QDialog.Accepted:
            if dict_of_profiles[self.current_profile]['hotkeys'][-1][2] != "":
                self.add_hotkey_to_table()
                self.create_hotkeys(dict_of_profiles[self.current_profile]['hotkeys'][-1])
            else:
                dict_of_profiles[self.current_profile]['hotkeys'].pop(-1)

                write_hotkeys_json(dict_of_profiles)

    @staticmethod
    def open_settings_window():
        settings_window = SettingsWindow()
        settings_window.setModal(True)
        dialog_settings_window = settings_window.exec_()

        if dialog_settings_window == QDialog.Accepted:
            settings_window.on_accepted()
        elif dialog_settings_window == QDialog.Rejected:
            read_settings_json()

    def open_edit_window(self):
        selected_row = self.tableWidget.selectionModel().selectedRows()

        index = selected_row[0].row() if selected_row != [] else -1

        if index != -1:
            edit_window = AddAndEditWindow(is_edit=True, index_of_hotkey_for_edit=index, profile=self.current_profile)
            edit_window.setModal(True)
            dialog_window = edit_window.exec_()

            dict_of_profiles = read_hotkeys_json()

            if dialog_window == QDialog.Accepted:
                if dict_of_profiles[self.current_profile]['hotkeys'][index][2] != "":
                    self.update_hotkey_in_table(index, dict_of_profiles[self.current_profile]['hotkeys'][index])
                    self.create_hotkeys(dict_of_profiles[self.current_profile]['hotkeys'][index])
                else:
                    edit_window.on_reject(index)
            elif dialog_window == QDialog.Rejected:
                edit_window.on_reject(index)

    def open_profile_window(self):
        profile_window = ProfileWindow()
        profile_window.setModal(True)
        dialog_window = profile_window.exec_()

        if dialog_window == QDialog.Accepted:
            profile_window.on_accepted()

            self.redraw_profile_menu()

        elif dialog_window == QDialog.Rejected:
            profile_window.on_rejected()

            self.redraw_profile_menu()

    def if_show_main_window_on_tray_click(self, reason):
        if reason == 3:
            self.show_main_window()

    def show_main_window(self):
        self.show()
        self.setWindowState(Qt.WindowActive)
    # ------------------------------------------------

    # --------Work with table-------------------------
    def add_hotkey_to_table(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())

        list_of_hotkeys = read_hotkeys_json()[self.current_profile]['hotkeys']

        for index, e in enumerate(list_of_hotkeys):
            for column, item in enumerate(e):

                item_in_table = QtWidgets.QTableWidgetItem(item)

                if column == 0 or column == 1:
                    item_in_table.setCheckState(Qt.Checked if item else Qt.Unchecked)
                    self.tableWidget.setItem(index, column, item_in_table)
                else:
                    self.tableWidget.setItem(index, column, item_in_table)

            self.tableWidget.resizeColumnsToContents()

    def on_cell_changed(self, row, column):
        if column in (0, 1):
            dict_of_profiles = read_hotkeys_json()
            list_of_hotkeys = dict_of_profiles[self.current_profile]['hotkeys']

            if list_of_hotkeys[row][0]:
                keyboard.remove_hotkey(list_of_hotkeys[row][2])

            state = self.tableWidget.item(row, column).checkState()
            list_of_hotkeys[row][column] = True if state == 2 else False

            dict_of_profiles[self.current_profile]['hotkeys'] = list_of_hotkeys

            write_hotkeys_json(dict_of_profiles)
            self.create_hotkeys(list_of_hotkeys[row])

    def update_hotkey_in_table(self, index, element):
        for column, item in enumerate(element):
            item_in_table = QtWidgets.QTableWidgetItem(item)
            if column == 0 or column == 1:
                item_in_table.setCheckState(Qt.Checked if item else Qt.Unchecked)
                self.tableWidget.setItem(index, column, item_in_table)
            else:
                self.tableWidget.setItem(index, column, item_in_table)
    # ------------------------------------------------

    # --------Some "system" methods-------------------
    def change_profile(self, choosed_profile):
        dict_of_profiles = read_hotkeys_json()
        dict_of_profiles[self.current_profile]['enable'] = False

        self.current_profile = choosed_profile.text()

        dict_of_profiles[self.current_profile]['enable'] = True

        try:
            keyboard.unhook_all_hotkeys()
        except AttributeError:
            pass

        self.tableWidget.clearContents()

        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(row)

        write_hotkeys_json(dict_of_profiles)
        self.load_hotkeys()

    def redraw_profile_menu(self):
        self.profiles_menu.clear()
        self.profiles_menu.addAction(self.profile_managment)
        self.profiles_menu.addSeparator()

        dict_of_hotkeys = read_hotkeys_json()
        for profile_name in dict_of_hotkeys:
            profile = QAction(text=profile_name)
            profile.setCheckable(True)
            if dict_of_hotkeys[profile_name]['enable']:
                self.current_profile = profile_name
                profile.setChecked(True)

            self.profiles_group.addAction(profile)
            self.profiles_menu.addAction(profile)

    def load_hotkeys(self):
        list_of_hotkeys = read_hotkeys_json()[self.current_profile]['hotkeys']

        for i in range(len(list_of_hotkeys)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())

        for i_r, e in enumerate(list_of_hotkeys):
            for i_e, item in enumerate(e):

                item_in_table = QtWidgets.QTableWidgetItem(item)

                if i_e == 0 or i_e == 1:
                    item_in_table.setCheckState(Qt.Checked if item else Qt.Unchecked)
                    self.tableWidget.setItem(i_r, i_e, item_in_table)
                elif i_e == 3:
                    mode = i_e
                    self.tableWidget.setItem(i_r, i_e, item_in_table)
                else:
                    if i_e == 4 and mode in ("Open file", "Open directory", "Type from file"):
                        path = Path(item)

                        if path.exists():
                            self.tableWidget.setItem(i_r, i_e, item_in_table)
                        else:
                            self.tableWidget.setItem(i_r, i_e, QtWidgets.QTableWidgetItem("File doesn't exist"))

                    else:
                        self.tableWidget.setItem(i_r, i_e, item_in_table)

            self.tableWidget.resizeColumnsToContents()
            self.create_hotkeys(e)

    @staticmethod
    def create_hotkeys(element):

        is_enable, has_suppress, combination, mode, argument = element

        create_hotkey, mode, argument = treat_information_for_creating(mode, argument)

        if create_hotkey and is_enable:
            eval(f"keyboard.add_hotkey('{combination}', {mode}, args=['{argument}'], suppress={has_suppress})")

    def delete(self):
        selected_row = self.tableWidget.selectionModel().selectedRows()

        index = selected_row[0].row() if selected_row != [] else -1
        if index != -1:
            self.tableWidget.removeRow(index)

            dict_of_profiles = read_hotkeys_json()
            list_of_hotkeys = dict_of_profiles[self.current_profile]['hotkeys']

            if list_of_hotkeys[index][0]:
                keyboard.remove_hotkey(list_of_hotkeys[index][2])

            list_of_hotkeys.pop(index)

            dict_of_profiles[self.current_profile]['hotkeys'] = list_of_hotkeys

            write_hotkeys_json(dict_of_profiles)
# ------------------------------------------------

    def closeEvent(self, event):
        if dict_of_settings['show_message_on_exit']:
            checkbox = QCheckBox(parent=self, text="Don`t ask me again")

            question_on_close = QMessageBox(self)
            question_on_close.setWindowTitle("QUIT")
            question_on_close.setText("Sure?\nThe hotkeys won't working!")
            question_on_close.setIcon(QMessageBox.Icon.Question)
            question_on_close.addButton(QMessageBox.Yes)
            question_on_close.addButton(QMessageBox.No)
            question_on_close.setCheckBox(checkbox)

            close = question_on_close.exec_()

            if checkbox.isChecked():
                dict_of_settings['show_message_on_exit'] = False
                write_settings_json(dict_of_settings)

            if close == QMessageBox.Yes:
                self.is_closing = True
                self.tray_icon.hide()
                event.accept()
            else:
                event.ignore()
        else:
            self.is_closing = True
            self.tray_icon.hide()

    def hideEvent(self, event):
        if not self.is_closing:
            event.ignore()
            self.hide()


async def main():

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainInterface()
    main_window.show()

    app.exec_()
    loop.stop()


async def start_listening_keyboard():
    keyboard.wait()
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
