# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_window(object):
    def setupUi(self, edit_window):
        edit_window.setObjectName("edit_window")
        edit_window.resize(700, 100)
        edit_window.setMinimumSize(QtCore.QSize(700, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        edit_window.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(edit_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(edit_window)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(edit_window)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(edit_window)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mode = QtWidgets.QComboBox(edit_window)
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.mode.addItem("")
        self.horizontalLayout.addWidget(self.mode)
        self.combination = QtWidgets.QLineEdit(edit_window)
        self.combination.setEnabled(True)
        self.combination.setReadOnly(True)
        self.combination.setObjectName("combination")
        self.horizontalLayout.addWidget(self.combination)
        self.add_combination = QtWidgets.QPushButton(edit_window)
        self.add_combination.setToolTip("")
        self.add_combination.setStatusTip("")
        self.add_combination.setWhatsThis("")
        self.add_combination.setObjectName("add_combination")
        self.horizontalLayout.addWidget(self.add_combination)
        self.path_or_txt = QtWidgets.QLineEdit(edit_window)
        self.path_or_txt.setObjectName("path_or_txt")
        self.horizontalLayout.addWidget(self.path_or_txt)
        self.open_button = QtWidgets.QPushButton(edit_window)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(edit_window)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(edit_window)
        self.buttonBox.accepted.connect(edit_window.accept)
        self.buttonBox.rejected.connect(edit_window.reject)
        QtCore.QMetaObject.connectSlotsByName(edit_window)

    def retranslateUi(self, edit_window):
        _translate = QtCore.QCoreApplication.translate
        edit_window.setWindowTitle(_translate("edit_window", "Edit"))
        self.label_3.setText(_translate("edit_window", "Mode"))
        self.label.setText(_translate("edit_window", "Create hotkey"))
        self.label_2.setText(_translate("edit_window", "Argument"))
        self.mode.setToolTip(_translate("edit_window", "<html><head/><body><p><span style=\" font-size:10pt;\">Choose operation mode</span></p></body></html>"))
        self.mode.setItemText(0, _translate("edit_window", "Open file"))
        self.mode.setItemText(1, _translate("edit_window", "Open directory"))
        self.mode.setItemText(2, _translate("edit_window", "Open URL"))
        self.mode.setItemText(3, _translate("edit_window", "Type from file"))
        self.mode.setItemText(4, _translate("edit_window", "Type from entered text"))
        self.combination.setToolTip(_translate("edit_window", "<html><head/><body><p>Click the button and then press combination</p></body></html>"))
        self.add_combination.setText(_translate("edit_window", "Create combination"))
        self.path_or_txt.setToolTip(_translate("edit_window", "<html><head/><body><p>If operating mode &quot;Type from entered text&quot; type here your text, but if operating mode &quot;Open file&quot; or &quot;Type from file&quot; press the buttom or just paste here path to file/dir</p></body></html>"))
        self.open_button.setText(_translate("edit_window", "Open"))
