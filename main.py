from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QDialog, QSystemTrayIcon, QAction, qApp, QMenu
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QDialogButtonBox

from interface import Ui_MainWindow
from add_window import Ui_Dialog
from settings import Ui_settings_window
from edit_window import Ui_edit_window

import keyboard
import webbrowser
import asyncio
import json
import os
import sys

JS_HOTKEYS = "hotkeys.json"
JS_SETTINGS = "settings.json"
DEFAULT_SETTINGS = {"bg_colour_bright": "(255, 255, 255)",
                    "font_colour_bright": "(0, 0, 0)",
                    "bg_colour_dark": "(43, 43, 43)",
                    "font_colour_dark": "(214, 214, 214)"}

list_of_hotkeys = []
dict_of_settings = {}


class AddWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(AddWindow, self).__init__()
        self.setupUi(self)

        self.load_theme()

        self.buttonBox.accepted.connect(self.add_hotkey)

        self.add_combination.clicked.connect(self.get_combination)
        self.open_button.clicked.connect(self.get_file_or_dir)
        self.mode.currentTextChanged.connect(self.disable_open_btn)

    def get_combination(self):
        try:
            cb = keyboard.read_hotkey(suppress=False)
            self.combination.setText(cb)
        except:
            pass

    def get_file_or_dir(self):
        if self.mode.currentText() == "Open directory":
            file_name_or_dir = str(QFileDialog.getExistingDirectory(directory=r"c:\\"))
        else:
            file_name_or_dir = str(QFileDialog.getOpenFileName(directory=r"c:\\")[0])

        self.path_or_txt.setText(file_name_or_dir)

    def add_hotkey(self):
        mode = self.mode.currentText()
        combination = self.combination.text()
        argument = self.path_or_txt.text()
        list_of_hotkeys.append([combination, mode, argument])

    def disable_open_btn(self):
        if self.mode.currentText() == "Type from entered text" or self.mode.currentText() == "Open URL":
            self.open_button.setEnabled(False)
        else:
            self.open_button.setEnabled(True)

    def load_theme(self):
        if dict_of_settings['theme'] == "bright":
            self.setStyleSheet("""
            QDialog {
                background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """;
            }
            
            QLabel {
                color: rgb""" + dict_of_settings['font_colour_bright'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            
            QLineEdit {
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            """)
        else:
            self.setStyleSheet("""
            QDialog {
                background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """;
            }
            
            QLabel {
                color: rgb""" + dict_of_settings['font_colour_dark'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            
            QLineEdit {
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            """)


# This class is copy-paste of AddWindow with some changes
# TODO Simple this shit
class EditWindow(QDialog, Ui_edit_window):
    def __init__(self, index_of_hotkey_for_edit):
        super(EditWindow, self).__init__()
        self.setupUi(self)

        self.load_theme()

        self.index_of_hotkey_for_edit = index_of_hotkey_for_edit

        self.old_combination, self.operating_mode, self.argument = list_of_hotkeys[index_of_hotkey_for_edit]
        self.mode.setCurrentText(self.operating_mode)
        self.combination.setText(self.old_combination)
        self.path_or_txt.setText(self.argument)

        self.buttonBox.accepted.connect(self.add_hotkey)

        self.add_combination.clicked.connect(self.get_combination)
        self.open_button.released.connect(self.get_file_or_dir)
        self.mode.currentTextChanged.connect(self.disable_open_btn)

        if self.mode.currentText() == "Type from entered text":
            self.open_button.setEnabled(False)

    def get_combination(self):
        try:
            cb = keyboard.read_hotkey(suppress=False)
            self.combination.setText(cb)
        except:
            pass

    def get_file_or_dir(self):
        if self.mode.currentText() == "Open directory":
            file_name_or_dir = str(QFileDialog.getExistingDirectory(directory=r"c:\\"))
        else:
            file_name_or_dir = str(QFileDialog.getOpenFileName(directory=r"c:\\")[0])

        self.path_or_txt.setText(file_name_or_dir)

    def add_hotkey(self):
        keyboard.remove_hotkey(self.old_combination)

        mode = self.mode.currentText()
        combination = self.combination.text()
        argument = self.path_or_txt.text()
        list_of_hotkeys.pop(self.index_of_hotkey_for_edit)
        list_of_hotkeys.insert(self.index_of_hotkey_for_edit, [combination, mode, argument])

    def disable_open_btn(self):
        if self.mode.currentText() == "Type from entered text" or self.mode.currentText() == "Open URL":
            self.open_button.setEnabled(False)
        else:
            self.open_button.setEnabled(True)

    def load_theme(self):
        if dict_of_settings['theme'] == "bright":
            self.setStyleSheet("""
            QDialog {
                background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """;
            }

            QLabel {
                color: rgb""" + dict_of_settings['font_colour_bright'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }

            QLineEdit {
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            """)
        else:
            self.setStyleSheet("""
            QDialog {
                background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """;
            }

            QLabel {
                color: rgb""" + dict_of_settings['font_colour_dark'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }

            QLineEdit {
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            """)


class SettingsWindow(QDialog, Ui_settings_window):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)

        self.load_graphic_display_settings()

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
        self.showed_bg_colour_bright.setStyleSheet("QFrame{"
                                                   "background-color: rgb"+dict_of_settings['bg_colour_bright']+"}")

    def get_font_colour_bright(self):
        dict_of_settings['font_colour_bright'] = get_colour()
        self.showed_font_colour_bright.setStyleSheet("QFrame{"
                                                     "background-color: rgb"+dict_of_settings['font_colour_bright']+"}")

    def get_bg_colour_dark(self):
        dict_of_settings['bg_colour_bright'] = get_colour()
        self.showed_bg_colour_dark.setStyleSheet("QFrame{"
                                                   "background-color: rgb"+dict_of_settings['bg_colour_bright']+"}")

    def get_font_colour_dark(self):
        dict_of_settings['font_colour_bright'] = get_colour()
        self.showed_font_colour_dark.setStyleSheet("QFrame{"
                                                     "background-color: rgb"+dict_of_settings['font_colour_dark']+"}")
# ------------------------------------------------

    def load_graphic_display_settings(self):
        self.showed_bg_colour_bright.setStyleSheet("QFrame{"
                                                   "background-color: rgb"+dict_of_settings['bg_colour_bright']+"}")
        self.showed_font_colour_bright.setStyleSheet("QFrame{"
                                                     "background-color: rgb"+dict_of_settings['font_colour_bright']+"}")
        self.showed_bg_colour_dark.setStyleSheet("QFrame{"
                                                 "background-color: rgb"+dict_of_settings['bg_colour_dark']+"}")
        self.showed_font_colour_dark.setStyleSheet("QFrame{"
                                                   "background-color: rgb"+dict_of_settings['font_colour_dark']+"}")

        if dict_of_settings['theme'] == "bright":
            self.bright_theme_btn.setChecked(True)

            self.setStyleSheet("""
            QDialog {
                background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """;
            }
            
            QLabel {
                color: rgb""" + dict_of_settings['font_colour_bright'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            
            #tab {
                background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """
            }
            
            #tab_2 {
                background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """
            }
            
            QRadioButton {
                color: rgb""" + dict_of_settings['font_colour_bright'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            
            QTabBar::tab {
                font-family: """ + dict_of_settings['font'] + """;
                font-size: 11px
            }
            
            QGroupBox {
                color: rgb""" + dict_of_settings['font_colour_bright'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            """)
        else:
            self.dark_theme_btn.setChecked(True)

            self.setStyleSheet("""
            QDialog {
                background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """;
            }

            QLabel {
                color: rgb""" + dict_of_settings['font_colour_dark'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            
            #tab {
                background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """
            }
            
            #tab_2 {
                background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """
            }
            
            QRadioButton {
                color: rgb""" + dict_of_settings['font_colour_dark'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            
            QTabBar::tab {
                font-family: """ + dict_of_settings['font'] + """;
                font-size: 11px
            }
            
            QGroupBox {
                color: rgb""" + dict_of_settings['font_colour_dark'] + """;
                font-family: """ + dict_of_settings['font'] + """;
                font-size: """ + str(dict_of_settings['font_size']) + """px
            }
            """)

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
        write_settings_json()
        self.load_graphic_display_settings()


class MainInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainInterface, self).__init__()
        self.setupUi(self)

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

        show_action.triggered.connect(self.show)
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

    def setting_dark(self):
        self.setStyleSheet("""
        QMainWindow{
        background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """
        }
        
        QLabel {
            color: rgb""" + dict_of_settings['font_colour_dark'] + """;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }

        #tableWidget {
            color: rgb""" + dict_of_settings['font_colour_dark'] + """;
            background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """;
            selection-color: rgb""" + dict_of_settings['bg_colour_dark'] + """;
            selection-background-color: #D6D6D6;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }
        
        #menubar {
            color: rgb""" + dict_of_settings['font_colour_dark'] + """;
            background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }
        
        #menuFile {
            color: rgb""" + dict_of_settings['font_colour_dark'] + """;
            background-color: rgb""" + dict_of_settings['bg_colour_dark'] + """;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }
        """)

        self.plus_button.setIcon(QIcon("images/plus-white.png"))
        self.minus_button.setIcon(QIcon("images/minus-white.png"))
        self.edit_button.setIcon(QIcon("images/pencil-white.png"))

    def setting_bright(self):
        self.setStyleSheet("""
        QMainWindow {
            background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """
        }

        QLabel {
            color: rgb""" + dict_of_settings['font_colour_bright'] + """;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }
        
        #tableWidget {
            color: rgb""" + dict_of_settings['font_colour_bright'] + """;
            background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """;
            selection-color: rgb""" + dict_of_settings['font_colour_bright'] + """;
            selection-background-color: #D6D6D6;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }
        
        #menubar {
            color: rgb""" + dict_of_settings['font_colour_bright'] + """;
            background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }
        
        #menuFile {
            color: rgb""" + dict_of_settings['font_colour_bright'] + """;
            background-color: rgb""" + dict_of_settings['bg_colour_bright'] + """;
            font-family: """ + dict_of_settings['font'] + """;
            font-size: """ + str(dict_of_settings['font_size']) + """px
        }
        """)

        self.plus_button.setIcon(QIcon("images/plus-black.png"))
        self.minus_button.setIcon(QIcon("images/minus-black.png"))
        self.edit_button.setIcon(QIcon("images/pencil-black.png"))
# ------------------------------------------------

# ---------Open different windows-----------------
    def open_add_window(self):
        add_window = AddWindow()
        add_window.setModal(True)
        dialog_window = add_window.exec_()

        if dialog_window == QDialog.Accepted:
            if list_of_hotkeys[-1][0] != "":
                self.add_hotkey_to_table_and_save_it()
                self.create_hotkeys(list_of_hotkeys[-1])
            else:
                list_of_hotkeys.pop(-1)

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
        index = self.tableWidget.currentRow()
        edit_window = EditWindow(index)
        edit_window.setModal(True)
        dialog_window = edit_window.exec_()

        if dialog_window == QDialog.Accepted:
            if list_of_hotkeys[index][0] != "":
                self.update_hotkey_in_table_and_save_it(index, list_of_hotkeys[index])
                self.create_hotkeys(list_of_hotkeys[index])
            else:
                list_of_hotkeys.pop(index)
# ------------------------------------------------

# --------Work with table-------------------------
    def add_hotkey_to_table_and_save_it(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())

        for i_r, e in enumerate(list_of_hotkeys):
            for i_e, item in enumerate(e):
                self.tableWidget.setItem(i_r, i_e, QtWidgets.QTableWidgetItem(item))

        self.tableWidget.resizeColumnsToContents()
        write_hotkeys_json()

    def update_hotkey_in_table_and_save_it(self, index, element):
        for column, item in enumerate(element):
            self.tableWidget.setItem(index, column, QtWidgets.QTableWidgetItem(item))
        write_hotkeys_json()
# ------------------------------------------------

# --------Some "system" methods-------------------
    def load_saved_hotkeys(self):
        for i in range(len(list_of_hotkeys)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())

        for i_r, e in enumerate(list_of_hotkeys):
            for i_e, item in enumerate(e):
                self.tableWidget.setItem(i_r, i_e, QtWidgets.QTableWidgetItem(item))

            self.tableWidget.resizeColumnsToContents()
            self.create_hotkeys(e)

    @staticmethod
    def create_hotkeys(element):
        combination, mode_name, argument = element

        if mode_name == "Open file" or mode_name == "Open directory":
            mode = "os.startfile"

        elif mode_name == "Open URL":
            mode = "webbrowser.open"

        elif mode_name == "Type from entered text":
            mode = "keyboard.write"

        else:
            with open(argument) as file:
                argument = file.read()
            mode = "keyboard.write"

        eval(f"keyboard.add_hotkey('{combination}', {mode}, args=['{argument}'], suppress=True)")

    def delete(self):
        index = self.tableWidget.currentRow()
        if index != -1:
            self.tableWidget.removeRow(index)
            keyboard.remove_hotkey(list_of_hotkeys[index][0])
            list_of_hotkeys.pop(index)
            write_hotkeys_json()
# ------------------------------------------------

# Open "Colour Chooser"'s window
def get_colour():
    colour = QColorDialog.getColor().getRgb()
    colour = colour[:-1]

    return str(colour)


def read_hotkeys_json():
    global list_of_hotkeys
    with open(JS_HOTKEYS) as file:
        list_of_hotkeys = json.load(file)


def write_hotkeys_json():
    with open(JS_HOTKEYS, 'w') as file:
        json.dump(list_of_hotkeys, file)


def read_settings_json():
    global dict_of_settings
    with open(JS_SETTINGS) as file:
        dict_of_settings = json.load(file)


def write_settings_json():
    with open(JS_SETTINGS, 'w') as file:
        json.dump(dict_of_settings, file)


async def main():
    read_hotkeys_json()
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
