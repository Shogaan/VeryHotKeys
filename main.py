from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDialog, QSystemTrayIcon, QAction, qApp, QMenu
from PyQt5.QtWidgets import QFileDialog

from interface import Ui_MainWindow
from add_window import Ui_Dialog

import keyboard
import asyncio
import json
import os
import sys

JSFILE = "hotkeys.json"
data = []


class AddWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(AddWindow, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.add_hotkey)

        self.add_combination.clicked.connect(self.get_combination)
        self.open_button.released.connect(self.get_file)

    def get_combination(self):
        cb = keyboard.read_hotkey(suppress=False)
        self.combination.setText(cb)

    def get_file(self):
        file_name = str(QFileDialog.getOpenFileName(directory=r"c:\\")[0])
        self.path_or_txt.setText(file_name)

    def add_hotkey(self):
        mode = self.mode.currentText()
        combination = self.combination.text()
        argument = self.path_or_txt.text()
        data.append([combination, mode, argument])


class MainInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainInterface, self).__init__()
        self.setupUi(self)

        self.load_saved_hotkeys()

        self.plus_button.clicked.connect(self.open_add_window)
        self.minus_button.clicked.connect(self.delete)

        self.actionTo_tray.triggered.connect(self.hide)
        self.actionExit.triggered.connect(self.close)

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

    def open_add_window(self):
        add_window = AddWindow()
        add_window.setModal(True)
        dialog_window = add_window.exec_()

        if dialog_window == QtWidgets.QDialog.Accepted:
            self.add_hotkey_to_table_and_save_it()
            self.create_hotkeys(data[-1])

    def add_hotkey_to_table_and_save_it(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())

        for i_r, e in enumerate(data):
            for i_e, item in enumerate(e):
                self.tableWidget.setItem(i_r, i_e, QtWidgets.QTableWidgetItem(item))

        self.tableWidget.resizeColumnsToContents()
        write_json()

    def load_saved_hotkeys(self):
        for i in range(len(data)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())

        for i_r, e in enumerate(data):
            for i_e, item in enumerate(e):
                self.tableWidget.setItem(i_r, i_e, QtWidgets.QTableWidgetItem(item))

            self.tableWidget.resizeColumnsToContents()
            self.create_hotkeys(e)

    @staticmethod
    def create_hotkeys(element):
        combination, mode_name, argument = element

        if mode_name == "Open file":
            mode = "os.startfile"

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
            keyboard.remove_hotkey(data[index][0])
            data.pop(index)
            write_json()


def read_json():
    global data
    with open(JSFILE) as file:
        data = json.load(file)


def write_json():
    with open(JSFILE, 'w') as file:
        json.dump(data, file)


async def main():
    read_json()

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainInterface()
    main_window.show()

    # sys.exit(app.exec_())
    app.exec_()
    keyboard.press_and_release(57394)
    loop.stop()


async def start_listening_keyboard():
    keyboard.wait(57394, suppress=True)
    loop.stop()


def go_to_autostart_win():
    from winreg import ConnectRegistry, OpenKey, CloseKey, QueryInfoKey, EnumValue, SetValueEx
    from winreg import HKEY_LOCAL_MACHINE, KEY_WRITE, REG_SZ

    global temp_name

    temp_name = 0

    a_reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

    a_key = OpenKey(a_reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
    for i in range(QueryInfoKey(a_key)[1]):
        name, _, _ = EnumValue(a_key, i)
        if name == "Very Hot Keys Dev":
            temp_name = 1
            CloseKey(a_key)
            break

    if temp_name != 1:
        a_key = OpenKey(a_reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
        path_to_app = ""

        if getattr(sys, 'frozen', False):
            path_to_app = os.path.abspath(sys.executable)
        elif __file__:
            path_to_app = os.path.abspath(__file__)

        SetValueEx(a_key, "Very Hot Keys Dev", 0, REG_SZ, path_to_app)
        CloseKey(a_key)

    CloseKey(a_reg)


if __name__ == "__main__":
    import platform
    if platform.system() == "Windows":
        go_to_autostart_win()
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    # loop.create_task(start_listening_keyboard())
    loop.run_forever()
