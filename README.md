# VeryHotKeys

Windows' app for creating shortcuts.

## Installing

First of all, if you want to **customize** a code, you can clone it by Git
```
git clone https://github.com/Shogaan/VeryHotKeys.git
```

You need to have installed python3.6. Then in project's folder open cmd(**I REALLY recommend to use Windows**). Create virtualenv by
```bash
pip install virtualenv
virtualenv venv
```
Then activate it by `venv\Scripts\activate.bat` and, finally, install requirements
```bash
pip install -r requirements.txt
```
To launch the app you need to have activated venv and in cmd type `python main.py`

Second way is using exe-files([click](https://github.com/Shogaan/VeryHotKeys/releases)).

For more information check [wiki](https://github.com/Shogaan/VeryHotKeys/wiki/Installation-and-converting-to-exe)

## New in v1.1.1

### Fixed:
* Ability to delete last profile

## New in v1.1.0

### Added:
* Profiles
* Simulation key pressing
* Enable/disable hotkey or its suppress by checkboxes in table
* Better design
* Open main window on left click on tray icon

### Fixed:
* Incorrect display info in "Argument"
* Crashes(?) when was entered incorrect name of theme

### Rewritten:
* main.py was separated on different files

## New in v1.0.1

### Added:
* Open URLs
* Correct opening links in "Open file" mode
* Quit window
* Hide to tray when minimized
* Checking does file exist

### Fixed:

* Selection, now working correctly
* Open Edit window
* Bug with russian letters

### Rewritten:

* Work with Edit Window
* Work with hotkeys inside the code

## New in v1.1

* Added dark theme and small customization option
* Added editing of hotkeys(shortcuts)
* Now you can open dirs
* Fixed crashes when you two times click "Create combination" in "Add window"

## Built with

* [PyQt5](https://www.riverbankcomputing.com/news)
* [keyboard](https://github.com/boppreh/keyboard)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details
