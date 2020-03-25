# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\add_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 100)
        Dialog.setMinimumSize(QtCore.QSize(700, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/logo2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mode = QtWidgets.QComboBox(Dialog)
        self.mode.setEditable(False)
        self.mode.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.mode.setObjectName("mode")
        self.horizontalLayout.addWidget(self.mode)
        self.combination = QtWidgets.QLineEdit(Dialog)
        self.combination.setEnabled(True)
        self.combination.setReadOnly(True)
        self.combination.setObjectName("combination")
        self.horizontalLayout.addWidget(self.combination)
        self.add_combination = QtWidgets.QPushButton(Dialog)
        self.add_combination.setToolTip("")
        self.add_combination.setStatusTip("")
        self.add_combination.setWhatsThis("")
        self.add_combination.setObjectName("add_combination")
        self.horizontalLayout.addWidget(self.add_combination)
        self.path_or_txt = QtWidgets.QLineEdit(Dialog)
        self.path_or_txt.setObjectName("path_or_txt")
        self.horizontalLayout.addWidget(self.path_or_txt)
        self.open_button = QtWidgets.QPushButton(Dialog)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.is_enable_check = QtWidgets.QCheckBox(Dialog)
        self.is_enable_check.setChecked(True)
        self.is_enable_check.setObjectName("is_enable_check")
        self.horizontalLayout_3.addWidget(self.is_enable_check)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.suppress_check = QtWidgets.QCheckBox(Dialog)
        self.suppress_check.setObjectName("suppress_check")
        self.horizontalLayout_3.addWidget(self.suppress_check)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Hotkey"))
        self.label_3.setText(_translate("Dialog", "Mode"))
        self.label.setText(_translate("Dialog", "Create hotkey"))
        self.label_2.setText(_translate("Dialog", "Argument"))
        self.mode.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Choose operation mode</span></p></body></html>"))
        self.combination.setToolTip(_translate("Dialog", "<html><head/><body><p>Click the button and then press combination</p></body></html>"))
        self.add_combination.setText(_translate("Dialog", "Create combination"))
        self.path_or_txt.setToolTip(_translate("Dialog", "<html><head/><body><p>If operating mode &quot;Type from entered text&quot; type here your text, but if operating mode &quot;Open file&quot; or &quot;Type from file&quot; press the buttom or just paste here path to file/dir</p></body></html>"))
        self.open_button.setText(_translate("Dialog", "Open"))
        self.is_enable_check.setText(_translate("Dialog", "Enable"))
        self.suppress_check.setText(_translate("Dialog", "Suppress"))