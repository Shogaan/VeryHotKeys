# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settings_window(object):
    def setupUi(self, settings_window):
        settings_window.setObjectName("settings_window")
        settings_window.resize(490, 215)
        settings_window.setMinimumSize(QtCore.QSize(490, 215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settings_window.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(settings_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(settings_window)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.font_type = QtWidgets.QFontComboBox(settings_window)
        self.font_type.setEnabled(True)
        self.font_type.setObjectName("font_type")
        self.horizontalLayout_2.addWidget(self.font_type)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(settings_window)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.font_size = QtWidgets.QSpinBox(settings_window)
        self.font_size.setFrame(True)
        self.font_size.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.font_size.setMinimum(10)
        self.font_size.setMaximum(72)
        self.font_size.setProperty("value", 12)
        self.font_size.setObjectName("font_size")
        self.horizontalLayout_3.addWidget(self.font_size)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(settings_window)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bright_theme_btn = QtWidgets.QRadioButton(self.groupBox)
        self.bright_theme_btn.setObjectName("bright_theme_btn")
        self.verticalLayout_2.addWidget(self.bright_theme_btn)
        self.dark_theme_btn = QtWidgets.QRadioButton(self.groupBox)
        self.dark_theme_btn.setObjectName("dark_theme_btn")
        self.verticalLayout_2.addWidget(self.dark_theme_btn)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(settings_window)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tab_widget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tab_widget.setObjectName("tab_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.showed_bg_colour_bright = QtWidgets.QFrame(self.tab)
        self.showed_bg_colour_bright.setFrameShape(QtWidgets.QFrame.Box)
        self.showed_bg_colour_bright.setFrameShadow(QtWidgets.QFrame.Plain)
        self.showed_bg_colour_bright.setLineWidth(1)
        self.showed_bg_colour_bright.setObjectName("showed_bg_colour_bright")
        self.horizontalLayout_5.addWidget(self.showed_bg_colour_bright)
        self.btn_choose_bg_colour_bright = QtWidgets.QPushButton(self.tab)
        self.btn_choose_bg_colour_bright.setObjectName("btn_choose_bg_colour_bright")
        self.horizontalLayout_5.addWidget(self.btn_choose_bg_colour_bright)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.showed_font_colour_bright = QtWidgets.QFrame(self.tab)
        self.showed_font_colour_bright.setFrameShape(QtWidgets.QFrame.Box)
        self.showed_font_colour_bright.setFrameShadow(QtWidgets.QFrame.Plain)
        self.showed_font_colour_bright.setObjectName("showed_font_colour_bright")
        self.horizontalLayout_6.addWidget(self.showed_font_colour_bright)
        self.btn_choose_font_colour_bright = QtWidgets.QPushButton(self.tab)
        self.btn_choose_font_colour_bright.setObjectName("btn_choose_font_colour_bright")
        self.horizontalLayout_6.addWidget(self.btn_choose_font_colour_bright)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.tab_widget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.showed_bg_colour_dark = QtWidgets.QFrame(self.tab_2)
        self.showed_bg_colour_dark.setFrameShape(QtWidgets.QFrame.Box)
        self.showed_bg_colour_dark.setFrameShadow(QtWidgets.QFrame.Plain)
        self.showed_bg_colour_dark.setLineWidth(1)
        self.showed_bg_colour_dark.setObjectName("showed_bg_colour_dark")
        self.horizontalLayout_8.addWidget(self.showed_bg_colour_dark)
        self.btn_choose_bg_colour_dark = QtWidgets.QPushButton(self.tab_2)
        self.btn_choose_bg_colour_dark.setObjectName("btn_choose_bg_colour_dark")
        self.horizontalLayout_8.addWidget(self.btn_choose_bg_colour_dark)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.showed_font_colour_dark = QtWidgets.QFrame(self.tab_2)
        self.showed_font_colour_dark.setFrameShape(QtWidgets.QFrame.Box)
        self.showed_font_colour_dark.setFrameShadow(QtWidgets.QFrame.Plain)
        self.showed_font_colour_dark.setObjectName("showed_font_colour_dark")
        self.horizontalLayout_7.addWidget(self.showed_font_colour_dark)
        self.btn_choose_font_colour_dark = QtWidgets.QPushButton(self.tab_2)
        self.btn_choose_font_colour_dark.setObjectName("btn_choose_font_colour_dark")
        self.horizontalLayout_7.addWidget(self.btn_choose_font_colour_dark)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.tab_widget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tab_widget)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(settings_window)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(settings_window)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(settings_window)
        self.tab_widget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(settings_window.accept)
        self.buttonBox.rejected.connect(settings_window.reject)
        QtCore.QMetaObject.connectSlotsByName(settings_window)

    def retranslateUi(self, settings_window):
        _translate = QtCore.QCoreApplication.translate
        settings_window.setWindowTitle(_translate("settings_window", "Settings"))
        self.label_2.setText(_translate("settings_window", "Font type"))
        self.label_3.setText(_translate("settings_window", "Font size"))
        self.font_size.setToolTip(_translate("settings_window", "<html><head/><body><p>Set font size from 10 to 72</p></body></html>"))
        self.groupBox.setTitle(_translate("settings_window", "Theme"))
        self.bright_theme_btn.setText(_translate("settings_window", "Bright"))
        self.dark_theme_btn.setText(_translate("settings_window", "Dark"))
        self.groupBox_2.setTitle(_translate("settings_window", "Colours"))
        self.label_4.setText(_translate("settings_window", "Background colour"))
        self.btn_choose_bg_colour_bright.setText(_translate("settings_window", "Choose"))
        self.label_5.setText(_translate("settings_window", "Font colour"))
        self.btn_choose_font_colour_bright.setText(_translate("settings_window", "Choose"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("settings_window", "Bright"))
        self.label_7.setText(_translate("settings_window", "Background colour"))
        self.btn_choose_bg_colour_dark.setText(_translate("settings_window", "Choose"))
        self.label_6.setText(_translate("settings_window", "Font colour"))
        self.btn_choose_font_colour_dark.setText(_translate("settings_window", "Choose"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), _translate("settings_window", "Dark"))
        self.label.setText(_translate("settings_window", "All changes need to rerun the app!!!"))

