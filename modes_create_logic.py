from pathlib import Path

from constants import JS_KEYS_TO_SIMULATE, JS_MODES

import json


def treat_information_for_creating(mode_name, argument):

    def check_path(path_to_check):
        path = Path(path_to_check)

        if path.exists():
            return True
        return False

    def open_file_directory(path):
        if check_path(path):
            return True, "os.startfile", path
        return False, None, None

    def open_url(argument):
        return True, "webbrowser.open", argument

    def type_from_file(path):
        if check_path(path):
            with open(path) as file:
                return True, "keyboard.write", file.read()
        return False, None, None

    def type_from_entered(argument):
        return True, "keyboard.write", argument

    def simulate_button(button):
        with open(JS_KEYS_TO_SIMULATE, 'r') as keys_file:
            return True, "keyboard.send", json.load(keys_file)[button]

    with open(JS_MODES, 'r') as modes:
        create_hotkey, mode, argument = eval(json.load(modes)[mode_name])

    return create_hotkey, mode, argument
