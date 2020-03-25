# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uis\profile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 229)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/logo2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.profiles_list = QtWidgets.QListWidget(Dialog)
        self.profiles_list.setObjectName("profiles_list")
        self.horizontalLayout_3.addWidget(self.profiles_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_profile_btn = QtWidgets.QPushButton(Dialog)
        self.add_profile_btn.setAutoFillBackground(False)
        self.add_profile_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/plus-black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_profile_btn.setIcon(icon1)
        self.add_profile_btn.setAutoRepeat(False)
        self.add_profile_btn.setDefault(False)
        self.add_profile_btn.setFlat(True)
        self.add_profile_btn.setObjectName("add_profile")
        self.horizontalLayout.addWidget(self.add_profile_btn)
        self.delete_profile_btn = QtWidgets.QPushButton(Dialog)
        self.delete_profile_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/minus-black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_profile_btn.setIcon(icon2)
        self.delete_profile_btn.setFlat(True)
        self.delete_profile_btn.setObjectName("delete_profile")
        self.horizontalLayout.addWidget(self.delete_profile_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.name_profile = QtWidgets.QLineEdit(Dialog)
        self.name_profile.setObjectName("name_profile")
        self.horizontalLayout_2.addWidget(self.name_profile)
        self.save_profile_name_btn = QtWidgets.QPushButton(Dialog)
        self.save_profile_name_btn.setObjectName("save_profile_name_btn")
        self.horizontalLayout_2.addWidget(self.save_profile_name_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Profiles"))
        self.label.setText(_translate("Dialog", "Name of the profile"))
        self.save_profile_name_btn.setText(_translate("Dialog", "Save"))
