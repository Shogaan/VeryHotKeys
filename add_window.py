# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 72)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mode = QtWidgets.QComboBox(Dialog)
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.horizontalLayout.addWidget(self.mode)
        self.combination = QtWidgets.QLineEdit(Dialog)
        self.combination.setObjectName("combination")
        self.horizontalLayout.addWidget(self.combination)
        self.add_combination = QtWidgets.QPushButton(Dialog)
        self.add_combination.setObjectName("add_combination")
        self.horizontalLayout.addWidget(self.add_combination)
        self.path_or_txt = QtWidgets.QLineEdit(Dialog)
        self.path_or_txt.setObjectName("path_or_txt")
        self.horizontalLayout.addWidget(self.path_or_txt)
        self.open_button = QtWidgets.QPushButton(Dialog)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Hotkey"))
        self.mode.setItemText(0, _translate("Dialog", "Open file"))
        self.mode.setItemText(1, _translate("Dialog", "Type from file"))
        self.mode.setItemText(2, _translate("Dialog", "Type from entered text"))
        self.add_combination.setText(_translate("Dialog", "Create combination"))
        self.open_button.setText(_translate("Dialog", "Open"))


