from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QDialog, QSystemTrayIcon, QAction, qApp, QMenu
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QDialogButtonBox, QMessageBox, QCheckBox
from PyQt5.QtCore import Qt, QItemSelectionModel

from pathlib import Path

from interface import Ui_MainWindow
from add_window import Ui_Dialog
from settings import Ui_settings_window

import keyboard
import webbrowser
import asyncio
import json
import os
import sys

JS_HOTKEYS = "hotkeys.json"
JS_SETTINGS = "settings.json"
JS_KEYS_TO_SIMULATE = "keys.json"

CSS_MAIN_BRIGHT = "css/main_interface_bright.fcss"
CSS_MAIN_DARK = "css/main_interface_dark.fcss"

CSS_ADD_WINDOW_BRIGHT = "css/add_window_bright.fcss"
CSS_ADD_WINDOW_DARK = "css/add_window_dark.fcss"

CSS_SETTINGS_BRIGHT = "css/settings_bright.fcss"
CSS_SETTINGS_DARK = "css/settings_dark.fcss"

DEFAULT_SETTINGS = {"bg_colour_bright": "(255, 255, 255)",
                    "font_colour_bright": "(0, 0, 0)",
                    "bg_colour_dark": "(43, 43, 43)",
                    "font_colour_dark": "(214, 214, 214)"}

RUS_SYMBOLS = u"ёЁйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
ENG_SYMBOLS = u"""`~qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""

TRANSLATE_TABLE_RUS_ENG = str.maketrans(RUS_SYMBOLS, ENG_SYMBOLS)

dict_of_settings = {}


class AddAndEditWindow(QDialog, Ui_Dialog):
    def __init__(self, **kwargs):
        super(AddAndEditWindow, self).__init__()
        self.setupUi(self)

        self.load_theme()

        self.is_edit = kwargs['is_edit']
        self.index_of_hotkey_for_edit = kwargs['index_of_hotkey_for_edit'] if self.is_edit else None

        if self.is_edit:
            with open(JS_HOTKEYS) as file_hotkeys:
                self.old_is_enable,\
                self.old_has_suppress,\
                self.old_combination,\
                self.operating_mode,\
                self.argument = json.load(file_hotkeys)[self.index_of_hotkey_for_edit]

                self.is_enable_check.setChecked(self.old_is_enable)
                self.suppress_check.setChecked(self.old_has_suppress)

            self.mode.setCurrentText(self.operating_mode)
            self.redraw_interface()
            self.combination.setText(self.old_combination)
            self.path_or_txt.setText(self.argument)

        self.buttonBox.accepted.connect(self.add_hotkey)

        self.add_combination.clicked.connect(self.get_combination)
        self.open_button.clicked.connect(self.get_file_or_dir)
        self.mode.currentTextChanged.connect(self.redraw_interface)

    def get_combination(self):
        try:
            cb = keyboard.read_hotkey(suppress=False)
            self.combination.setText(cb.translate(TRANSLATE_TABLE_RUS_ENG))
        except:
            pass

    def get_file_or_dir(self):
        if self.mode.currentText() == "Open directory":
            file_name_or_dir = str(QFileDialog.getExistingDirectory(directory=r"c:\\"))
        else:
            file_name_or_dir = str(QFileDialog.getOpenFileName(directory=r"c:\\",
                                                               options=QFileDialog.DontResolveSymlinks)[0])

        self.path_or_txt.setText(file_name_or_dir)

    def add_hotkey(self): # dif
        if self.is_edit and self.old_is_enable:
            keyboard.remove_hotkey(self.old_combination)

        is_enable = self.is_enable_check.isChecked()
        has_suppress = self.suppress_check.isChecked()
        mode = self.mode.currentText()
        combination = self.combination.text()
        argument = self.button_to_simulate.currentText() if mode == "Simulate pressing button"\
                                                                                            else self.path_or_txt.text()

        if self.is_edit:
            with open(JS_HOTKEYS) as file_hotkeys:
                list_of_hotkeys = json.load(file_hotkeys)
                list_of_hotkeys[self.index_of_hotkey_for_edit] = [is_enable, has_suppress, combination, mode, argument]

                write_hotkeys_json(list_of_hotkeys)

        else:
            with open(JS_HOTKEYS) as file_hotkeys:
                list_of_hotkeys = json.load(file_hotkeys)
                list_of_hotkeys.append([is_enable, has_suppress, combination, mode, argument])

                write_hotkeys_json(list_of_hotkeys)

    def on_reject(self, index):
        with open(JS_HOTKEYS) as file:
            list_of_hotkeys = json.load(file)
            list_of_hotkeys[index] = [self.old_is_enable, self.old_has_suppress,
                                      self.old_combination, self.operating_mode, self.argument]

            write_hotkeys_json(list_of_hotkeys)

    def redraw_interface(self):
        if self.mode.currentText() == "Simulate pressing button":
            self.path_or_txt.hide()
            self.open_button.hide()

            with open(JS_KEYS_TO_SIMULATE, "r") as file_keys:
                keys = json.load(file_keys)

            self.button_to_simulate = QtWidgets.QComboBox()
            self.button_to_simulate.setObjectName("button_to_simulate")

            for i, key in enumerate(keys):
                self.button_to_simulate.addItem("")
                self.button_to_simulate.setItemText(i, QtCore.QCoreApplication.translate("Dialog", key))

            self.horizontalLayout.addWidget(self.button_to_simulate)

        else:
            try:
                self.button_to_simulate.hide()
            except:
                pass

            self.path_or_txt.show()
            self.open_button.show()

        if self.mode.currentText() == "Type from entered text" or self.mode.currentText() == "Open URL":
            self.open_button.setEnabled(False)
        else:
            self.open_button.setEnabled(True)

    def load_theme(self):
        if dict_of_settings['theme'] == "bright":
            with open(CSS_ADD_WINDOW_BRIGHT) as file:
                self.setStyleSheet(eval(file.read()))
        else:
            with open(CSS_ADD_WINDOW_DARK) as file:
                self.setStyleSheet(eval(file.read()))


class SettingsWindow(QDialog, Ui_settings_window):

    template = "QFrame{background-color: rgb"

    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)

        self.load_graphic_display_settings(False)

        self.btn_choose_bg_colour_bright.clicked.connect(self.get_bg_colour_bright)
        self.btn_choose_font_colour_bright.clicked.connect(self.get_font_colour_bright)

        self.btn_choose_bg_colour_dark.clicked.connect(self.get_bg_colour_dark)
        self.btn_choose_font_colour_dark.clicked.connect(self.get_font_colour_dark)

        self.font_type.setCurrentFont(QFont(dict_of_settings['font']))
        self.font_size.setValue(dict_of_settings['font_size'])

        self.buttonBox.button(QDialogButtonBox.Reset).clicked.connect(self.on_reset)

# --------Show choosed colours--------------------
    def get_bg_colour_bright(self):
        dict_of_settings['bg_colour_bright'] = get_colour()
        self.showed_bg_colour_bright.setStyleSheet(self.template + dict_of_settings['bg_colour_bright'] + "}")

    def get_font_colour_bright(self):
        dict_of_settings['font_colour_bright'] = get_colour()
        self.showed_font_colour_bright.setStyleSheet(self.template + dict_of_settings['font_colour_bright'] + "}")

    def get_bg_colour_dark(self):
        dict_of_settings['bg_colour_bright'] = get_colour()
        self.showed_bg_colour_dark.setStyleSheet(self.template + dict_of_settings['bg_colour_bright'] + "}")

    def get_font_colour_dark(self):
        dict_of_settings['font_colour_bright'] = get_colour()
        self.showed_font_colour_dark.setStyleSheet(self.template + dict_of_settings['font_colour_dark'] + "}")
# ------------------------------------------------

    def load_graphic_display_settings(self, is_reset: bool):
        self.showed_bg_colour_bright.setStyleSheet(self.template + dict_of_settings['bg_colour_bright'] + "}")
        self.showed_font_colour_bright.setStyleSheet(self.template + dict_of_settings['font_colour_bright'] + "}")
        self.showed_bg_colour_dark.setStyleSheet(self.template + dict_of_settings['bg_colour_dark'] + "}")
        self.showed_font_colour_dark.setStyleSheet(self.template + dict_of_settings['font_colour_dark'] + "}")

        if not is_reset:
            if dict_of_settings['theme'] == "bright":
                self.bright_theme_btn.setChecked(True)

                with open(CSS_SETTINGS_BRIGHT) as file:
                    self.setStyleSheet(eval(file.read()))
            elif dict_of_settings['theme'] == "dark":
                self.dark_theme_btn.setChecked(True)

                with open(CSS_SETTINGS_DARK) as file:
                    self.setStyleSheet(eval(file.read()))

    def on_accepted(self):
        dict_of_settings['font'] = self.font_type.currentFont().family()
        dict_of_settings['font_size'] = self.font_size.value()

        if self.bright_theme_btn.isChecked():
            dict_of_settings['theme'] = "bright"
        elif self.dark_theme_btn.isChecked():
            dict_of_settings['theme'] = "dark"
        write_settings_json()

    def on_reset(self):
        for name, value in DEFAULT_SETTINGS.items():
            dict_of_settings[name] = value

        self.load_graphic_display_settings(True)


class MainInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainInterface, self).__init__()
        self.setupUi(self)

        self.is_closing = False

        self.load_saved_hotkeys()
        self.load_settings()

        self.plus_button.clicked.connect(self.open_add_window)
        self.minus_button.clicked.connect(self.delete)
        self.edit_button.clicked.connect(self.open_edit_window)

        self.actionTo_tray.triggered.connect(self.hide)
        self.actionSettings_.triggered.connect(self.open_settings_window)

        self.actionExit.triggered.connect(self.close)

        # --------------Set tray icon---------------------
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("images/logo2.ico"))

        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)

        show_action.triggered.connect(self.show_main_window)
        quit_action.triggered.connect(qApp.quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
    # ------------------------------------------------

    # -----------------Initialization CSS-------------
    def load_settings(self):
        if dict_of_settings['theme'] == "bright":
            self.setting_bright()
        elif dict_of_settings['theme'] == "dark":
            self.setting_dark()

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
        add_window = AddAndEditWindow(is_edit=False)
        add_window.setModal(True)
        dialog_window = add_window.exec_()

        with open(JS_HOTKEYS) as file:
            list_of_hotkeys = json.load(file)

        if dialog_window == QDialog.Accepted:
            if list_of_hotkeys[-1][0] != "":
                self.add_hotkey_to_table()
                self.create_hotkeys(list_of_hotkeys[-1])
            else:
                list_of_hotkeys.pop(-1)

                write_hotkeys_json(list_of_hotkeys)

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
            edit_window = AddAndEditWindow(is_edit=True, index_of_hotkey_for_edit=index)
            edit_window.setModal(True)
            dialog_window = edit_window.exec_()

            with open(JS_HOTKEYS) as file:
                list_of_hotkeys = json.load(file)

            if dialog_window == QDialog.Accepted:
                if list_of_hotkeys[index][2] != "":
                    self.update_hotkey_in_table(index, list_of_hotkeys[index])
                    self.create_hotkeys(list_of_hotkeys[index])
                else:
                    edit_window.on_reject(index)
            elif dialog_window == QDialog.Rejected:
                edit_window.on_reject(index)

    def show_main_window(self):
        self.show()
        self.setWindowState(Qt.WindowActive)
    # ------------------------------------------------

    # --------Work with table-------------------------
    def add_hotkey_to_table(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())

        with open(JS_HOTKEYS) as file_hotkeys:
            list_of_hotkeys = json.load(file_hotkeys)
            for i_r, e in enumerate(list_of_hotkeys):
                for i_e, item in enumerate(e):

                    item_in_table = QtWidgets.QTableWidgetItem(item)

                    if i_e == 0 or i_e == 1:
                        item_in_table.setCheckState(Qt.Checked if item else Qt.Unchecked)
                        self.tableWidget.setItem(i_r, i_e, item_in_table)
                    else:
                        self.tableWidget.setItem(i_r, i_e, item_in_table)

            self.tableWidget.resizeColumnsToContents()

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
    def load_saved_hotkeys(self):
        with open(JS_HOTKEYS) as file_hotkeys:
            list_of_hotkeys = json.load(file_hotkeys)

            for i in range(len(list_of_hotkeys)):
                self.tableWidget.insertRow(self.tableWidget.rowCount())

            for i_r, e in enumerate(list_of_hotkeys):
                for i_e, item in enumerate(e):

                    item_in_table = QtWidgets.QTableWidgetItem(item)

                    if i_e == 0 or i_e == 1:
                        item_in_table.setCheckState(Qt.Checked if item else Qt.Unchecked)
                        self.tableWidget.setItem(i_r, i_e, item_in_table)
                    else:
                        if i_e == 4:
                            path = Path(item)
                            try:
                                if path.exists():
                                    self.tableWidget.setItem(i_r, i_e, item_in_table)
                                else:
                                    self.tableWidget.setItem(i_r, i_e, QtWidgets.QTableWidgetItem("File doesn't exist"))
                            except:
                                self.tableWidget.setItem(i_r, i_e, item_in_table)

                        else:
                            self.tableWidget.setItem(i_r, i_e, item_in_table)

                self.tableWidget.resizeColumnsToContents()
                self.create_hotkeys(e)

    @staticmethod
    def create_hotkeys(element):
        create_hotkey = True

        is_enable, has_suppress, combination, mode_name, argument = element

        if mode_name == "Open file" or mode_name == "Open directory":
            path = Path(argument)

            mode = "os.startfile"

            if not path.exists():
                create_hotkey = False

        elif mode_name == "Open URL":
            mode = "webbrowser.open"

        elif mode_name == "Type from entered text":
            mode = "keyboard.write"

        elif mode_name == "Type from file":
            path = Path(argument)

            if path.exists():
                with open(argument) as file:
                    argument = file.read()
            else:
                create_hotkey = False
            mode = "keyboard.write"

        elif mode_name == "Simulate pressing button":
            mode = "keyboard.send"

            with open(JS_KEYS_TO_SIMULATE, 'r') as keys_file:
                keys = json.load(keys_file)
                argument = keys[argument]

        if create_hotkey and is_enable:
            eval(f"keyboard.add_hotkey('{combination}', {mode}, args=['{argument}'], suppress={has_suppress})")

    def delete(self):
        selected_row = self.tableWidget.selectionModel().selectedRows()

        index = selected_row[0].row() if selected_row != [] else -1
        if index != -1:
            self.tableWidget.removeRow(index)

            with open(JS_HOTKEYS) as file_hotkeys:
                list_of_hotkeys = json.load(file_hotkeys)
                try:
                    keyboard.remove_hotkey(list_of_hotkeys[index][2])
                except: pass
                list_of_hotkeys.pop(index)

                write_hotkeys_json(list_of_hotkeys)
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
                write_settings_json()

            if close == QMessageBox.Yes:
                self.is_closing = True
                event.accept()
            else:
                event.ignore()
        else:
            self.is_closing = True

    def hideEvent(self, event):
        if not self.is_closing:
            event.ignore()
            self.hide()


# Open "Colour Chooser"`s window
def get_colour():
    colour = QColorDialog.getColor().getRgb()
    colour = colour[:-1]

    return str(colour)


def read_settings_json():
    global dict_of_settings
    with open(JS_SETTINGS) as file:
        dict_of_settings = json.load(file)


def write_settings_json():
    with open(JS_SETTINGS, 'w') as file:
        json.dump(dict_of_settings, file, indent=2)


def write_hotkeys_json(list_of_hotkeys):
    with open(JS_HOTKEYS, 'w') as file:
        json.dump(list_of_hotkeys, file, indent=2)


async def main():
    read_settings_json()

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
