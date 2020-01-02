JS_HOTKEYS = "hotkeys.json"
JS_SETTINGS = "settings.json"
JS_KEYS_TO_SIMULATE = "keys.json"
JS_MODES = "modes.json"

CSS_MAIN_BRIGHT = "css/main_interface_bright.fcss"
CSS_MAIN_DARK = "css/main_interface_dark.fcss"

CSS_ADD_WINDOW_BRIGHT = "css/add_window_bright.fcss"
CSS_ADD_WINDOW_DARK = "css/add_window_dark.fcss"

CSS_SETTINGS_BRIGHT = "css/settings_bright.fcss"
CSS_SETTINGS_DARK = "css/settings_dark.fcss"

CSS_PROFILE_BRIDHT = "css/profile_bright.fcss"
CSS_PROFILE_DARK = "css/profile_dark.fcss"

DEFAULT_SETTINGS = {"bg_colour_bright": "(255, 255, 255)",
                    "font_colour_bright": "(0, 0, 0)",
                    "bg_colour_dark": "(43, 43, 43)",
                    "font_colour_dark": "(214, 214, 214)"}

RUS_SYMBOLS = u"ёЁйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
ENG_SYMBOLS = u"""`~qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""

TRANSLATE_TABLE_RUS_ENG = str.maketrans(RUS_SYMBOLS, ENG_SYMBOLS)

TEMPLATE_FOR_CREATION_PROFILE = '{"enable": False,"hotkeys": []}'
