# from pystray import Icon as icon, Menu as menu, MenuItem as item
# from PIL import Image
# from main import MainInterface
#
#
# def exit_from_app(icon, item):
#     MainInterface().close()
#     icon.stop()
#
#
# def open_window(icon, item):
#     MainInterface().show_window()
#     icon.update_menu()
#     icon.stop()
#
#
# def start():
#     im = Image.open("images/Ubuntu_small_logo.png")
#     butt = menu(item('Open', open_window), item('Exit', exit_from_app))
#     icon_im = icon("try", icon=im, menu=butt)
#     icon_im.run()
# from time import sleep
# import sys
# import os
#
# if getattr(sys, 'frozen', False):
#     application_path = os.path.abspath(sys.executable)
# elif __file__:
#     application_path = os.path.abspath(__file__)
#
# print(application_path)
# sleep(5)

import keyboard

a = keyboard.read_key(suppress=True)
print(a)
print(keyboard.key_to_scan_codes(a))
