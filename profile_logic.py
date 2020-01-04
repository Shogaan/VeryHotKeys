from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5.QtGui import QIcon

from keyboard import unhook_all_hotkeys

from profile import Ui_Dialog

from global_definitions import read_settings_json, write_settings_json
from global_definitions import read_hotkeys_json, write_hotkeys_json

from constants import CSS_PROFILE_BRIDHT, CSS_PROFILE_DARK
from constants import TEMPLATE_FOR_CREATION_PROFILE

dict_of_settings = read_settings_json()


class ProfileWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(ProfileWindow, self).__init__()
        self.setupUi(self)

        self.old_profile_name = ""
        self.new_profile_name = ""

        self.old_profiles = {}

        self.was_enabled = None
        self.is_first = True
        self.none_is_enable_after_addition = True

        self.load_profiles()
        self.load_settings()

        self.name_profile.setEnabled(False)

        self.profiles_list.itemClicked.connect(self.choosed_item_logic)

        self.save_profile_name_btn.clicked.connect(self.change_profile_name)

        self.add_profile_btn.clicked.connect(self.add_new_profile)
        self.delete_profile_btn.clicked.connect(self.delete_profile)

    def choosed_item_logic(self, item):
        self.name_profile.setEnabled(True)
        self.name_profile.setText(item.text())
        self.old_profile_name = item.text()

    def change_profile_name(self):
        if self.name_profile.text() != self.old_profile_name and self.name_profile != "":
            self.new_profile_name = self.name_profile.text()

            dict_of_hotkeys = read_hotkeys_json()

            if self.new_profile_name not in dict_of_hotkeys:
                self.profiles_list.currentItem().setText(self.new_profile_name)

                dict_of_hotkeys[self.profiles_list.currentItem().text()] = dict_of_hotkeys.pop(self.old_profile_name)

                write_hotkeys_json(dict_of_hotkeys)

            else:
                self.name_profile.setText(self.old_profile_name)

    def add_new_profile(self):
        dict_of_hotkeys = read_hotkeys_json()

        if self.is_first:
            self.old_profiles = {**self.old_profiles, **dict_of_hotkeys}
            self.is_first = False

        generated_name = self.generate_profile_name(dict_of_hotkeys)

        self.profiles_list.addItem(QListWidgetItem(generated_name))
        dict_of_hotkeys[generated_name] = eval(TEMPLATE_FOR_CREATION_PROFILE)

        a = list(dict_of_hotkeys.values())
        for i in a:
            if i['enable']:
                self.none_is_enable_after_addition = False

        write_hotkeys_json(dict_of_hotkeys)

    def delete_profile(self):
        try:
            deleted_item = self.profiles_list.currentItem().text()
        except AttributeError:
            pass
        else:
            _ = self.profiles_list.takeItem(self.profiles_list.row(self.profiles_list.currentItem()))

            self.name_profile.setText("")

            dict_of_hotkeys = read_hotkeys_json()

            if self.is_first:
                self.old_profiles = {**self.old_profiles, **dict_of_hotkeys}
                self.is_first = False

            self.was_enabled = dict_of_hotkeys[deleted_item]['enable']

            dict_of_hotkeys.pop(deleted_item)

            write_hotkeys_json(dict_of_hotkeys)

# ------ Initialization CSS -----
    def load_settings(self):
        if dict_of_settings['theme'] == "bright":
            self.setting_bright()
        elif dict_of_settings['theme'] == "dark":
            self.setting_dark()
        else:
            dict_of_settings['theme'] = "bright"
            write_settings_json(dict_of_settings)

    def setting_bright(self):
        with open(CSS_PROFILE_BRIDHT) as file:
            self.setStyleSheet(eval(file.read()))

        self.add_profile_btn.setIcon(QIcon("./images/plus-black.png"))
        self.delete_profile_btn.setIcon(QIcon("images/minus-black.png"))

    def setting_dark(self):
        with open(CSS_PROFILE_DARK) as file:
            self.setStyleSheet(eval(file.read()))

        self.add_profile_btn.setIcon(QIcon("images/plus-white.png"))
        self.delete_profile_btn.setIcon(QIcon("images/minus-white.png"))
# -------------------------------

# ----- Some "system" methods ---
    def load_profiles(self):
        dict_of_profiles = read_hotkeys_json()

        for profile_name in dict_of_profiles:
            self.profiles_list.addItem(QListWidgetItem(profile_name))

    @staticmethod
    def generate_profile_name(dictionary):
        keys = dictionary.keys()

        default = "Profile "
        a = 0

        while True:
            if default + str(a) not in keys:
                return default + str(a)
            else:
                a += 1

    def on_accepted(self):
        dict_of_hotkeys = read_hotkeys_json()

        if self.was_enabled is not None and (self.was_enabled or self.none_is_enable_after_addition):
            try:
                unhook_all_hotkeys()
            except AttributeError:
                pass

            dict_of_hotkeys[next(iter(dict_of_hotkeys))]['enable'] = True
            write_hotkeys_json(dict_of_hotkeys)

    def on_rejected(self):
        if self.old_profiles != {}:
            write_hotkeys_json(self.old_profiles)
# -------------------------------
