from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from settings import Ui_settings_window

from global_definitions import get_colour
from global_definitions import read_settings_json, write_settings_json

from constants import DEFAULT_SETTINGS
from constants import CSS_SETTINGS_BRIGHT, CSS_SETTINGS_DARK

dict_of_settings = read_settings_json()


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
        write_settings_json(dict_of_settings)

    def on_reset(self):
        for name, value in DEFAULT_SETTINGS.items():
            dict_of_settings[name] = value

        self.load_graphic_display_settings(True)
