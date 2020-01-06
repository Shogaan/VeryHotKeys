from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog

from add_window import Ui_Dialog

from global_definitions import read_settings_json
from global_definitions import read_hotkeys_json, write_hotkeys_json

from constants import JS_KEYS_TO_SIMULATE, JS_MODES
from constants import TRANSLATE_TABLE_RUS_ENG
from constants import CSS_ADD_WINDOW_BRIGHT, CSS_ADD_WINDOW_DARK

import json
import keyboard

dict_of_settings = read_settings_json()


class AddAndEditWindow(QDialog, Ui_Dialog):
    def __init__(self, **kwargs):
        super(AddAndEditWindow, self).__init__()
        self.setupUi(self)

        self.draw_modes()
        self.load_theme()

        self.is_edit = kwargs['is_edit']
        self.index_of_hotkey_for_edit = kwargs['index_of_hotkey_for_edit'] if self.is_edit else None
        self.profile = kwargs['profile']

        if self.is_edit:
            self.old_is_enable, \
            self.old_has_suppress, \
            self.old_combination, \
            self.operating_mode, \
            self.argument = read_hotkeys_json()[self.profile]['hotkeys'][self.index_of_hotkey_for_edit]

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
        except AttributeError:
            pass

    def get_file_or_dir(self):
        if self.mode.currentText() == "Open directory":
            file_name_or_dir = str(QFileDialog.getExistingDirectory(directory=r"c:\\"))
        else:
            file_name_or_dir = str(QFileDialog.getOpenFileName(directory=r"c:\\",
                                                               options=QFileDialog.DontResolveSymlinks)[0])

        self.path_or_txt.setText(file_name_or_dir)

    def add_hotkey(self):
        if self.is_edit and self.old_is_enable:
            keyboard.remove_hotkey(self.old_combination)

        is_enable = self.is_enable_check.isChecked()
        has_suppress = self.suppress_check.isChecked()
        mode = self.mode.currentText()
        combination = self.combination.text()
        argument = self.button_to_simulate.currentText() if mode == "Simulate pressing button" \
                                                                                            else self.path_or_txt.text()

        if self.is_edit:
            dict_of_profiles = read_hotkeys_json()
            list_of_hotkeys = dict_of_profiles[self.profile]['hotkeys']
            list_of_hotkeys[self.index_of_hotkey_for_edit] = [is_enable, has_suppress, combination, mode, argument]

            dict_of_profiles[self.profile]['hotkeys'] = list_of_hotkeys

            write_hotkeys_json(dict_of_profiles)

        else:
            dict_of_profiles = read_hotkeys_json()
            list_of_hotkeys = dict_of_profiles[self.profile]['hotkeys']
            list_of_hotkeys.append([is_enable, has_suppress, combination, mode, argument])

            dict_of_profiles[self.profile]['hotkeys'] = list_of_hotkeys

            write_hotkeys_json(dict_of_profiles)

    def on_reject(self, index):
        dict_of_profiles = read_hotkeys_json()
        list_of_hotkeys = dict_of_profiles[self.profile]['hotkey']
        list_of_hotkeys[index] = [self.old_is_enable, self.old_has_suppress,
                                  self.old_combination, self.operating_mode, self.argument]

        dict_of_profiles[self.profile]['hotkeys'] = list_of_hotkeys

        write_hotkeys_json(dict_of_profiles)

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
            except AttributeError:
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

    def draw_modes(self):
        with open(JS_MODES, 'r') as modes_file:
            modes = json.load(modes_file)

        for i, mode in enumerate(modes):
            self.mode.addItem("")
            self.mode.setItemText(i, QtCore.QCoreApplication.translate("Dialog", mode))
