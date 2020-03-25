JS_HOTKEYS = "jsons/hotkeys.json"
JS_SETTINGS = "jsons/settings.json"
JS_KEYS_TO_SIMULATE = "jsons/keys.json"
JS_MODES = "jsons/modes.json"

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
                    "font_colour_dark": "(214, 214, 214)",
                    "header_border_colour_bright": "(208, 208, 208)",
                    "header_border_colour_dark": "(36, 36, 36)",
                    "hover_colour_bright": "(205, 205, 205)",
                    "hover_colour_dark": "(65, 65, 65)",
                    "menu_bar_selected_bg_colour_bright": "(65, 65, 65)",
                    "menu_bar_hover_bg_colour_bright": "(98, 98, 98)",
                    "menu_bar_selected_bg_colour_dark": "(225, 225, 225)",
                    "menu_bar_hover_bg_colour_dark": "(175, 175, 175)",
                    "menu_bar_action_hover_colour_bright": "(219, 219, 219)",
                    "menu_bar_action_hover_colour_dark": "(65, 65, 65)",
                    "select_colour_bright": "(113, 113, 113)",
                    "select_colour_dark": "(214, 214, 214)",
                    "select_font_colour_bright": "(255, 255, 255)",
                    "select_font_colour_dark": "(43, 43, 43)",
                    }

RUS_SYMBOLS = u"ёЁйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
ENG_SYMBOLS = u"""`~qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""

TRANSLATE_TABLE_RUS_ENG = str.maketrans(RUS_SYMBOLS, ENG_SYMBOLS)

TEMPLATE_FOR_CREATION_PROFILE = '{"enable": False,"hotkeys": []}'
