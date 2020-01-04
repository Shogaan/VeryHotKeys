from PyQt5.QtWidgets import QColorDialog

from constants import JS_HOTKEYS, JS_SETTINGS

import json


# Open "Colour Chooser"`s window
def get_colour():
    colour = QColorDialog.getColor().getRgb()
    colour = colour[:-1]

    return str(colour)


def read_settings_json():
    with open(JS_SETTINGS) as file:
        return json.load(file)


def write_settings_json(dict_of_settings):
    with open(JS_SETTINGS, 'w') as file:
        json.dump(dict_of_settings, file, indent=2)


def read_hotkeys_json():
    with open(JS_HOTKEYS, 'r') as file:
        return json.load(file)


def write_hotkeys_json(dict_of_hotkeys):
    with open(JS_HOTKEYS, 'w') as file:
        json.dump(dict_of_hotkeys, file, indent=2)
