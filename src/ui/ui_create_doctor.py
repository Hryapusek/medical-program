# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_doctor.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateDoctorForm(object):
    def setupUi(self, CreateDoctorForm):
        CreateDoctorForm.setObjectName("CreateDoctorForm")
        CreateDoctorForm.resize(383, 236)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CreateDoctorForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(CreateDoctorForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(CreateDoctorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(CreateDoctorForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.surnameEdit = QtWidgets.QLineEdit(CreateDoctorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surnameEdit.sizePolicy().hasHeightForWidth())
        self.surnameEdit.setSizePolicy(sizePolicy)
        self.surnameEdit.setObjectName("surnameEdit")
        self.horizontalLayout_2.addWidget(self.surnameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(CreateDoctorForm)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.specializationEdit = QtWidgets.QLineEdit(CreateDoctorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.specializationEdit.sizePolicy().hasHeightForWidth())
        self.specializationEdit.setSizePolicy(sizePolicy)
        self.specializationEdit.setObjectName("specializationEdit")
        self.horizontalLayout_3.addWidget(self.specializationEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(CreateDoctorForm)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.phoneEdit = QtWidgets.QLineEdit(CreateDoctorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneEdit.sizePolicy().hasHeightForWidth())
        self.phoneEdit.setSizePolicy(sizePolicy)
        self.phoneEdit.setObjectName("phoneEdit")
        self.horizontalLayout_5.addWidget(self.phoneEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(CreateDoctorForm)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.emailEdit = QtWidgets.QLineEdit(CreateDoctorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailEdit.sizePolicy().hasHeightForWidth())
        self.emailEdit.setSizePolicy(sizePolicy)
        self.emailEdit.setObjectName("emailEdit")
        self.horizontalLayout_6.addWidget(self.emailEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(CreateDoctorForm)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.cabinetEdit = QtWidgets.QLineEdit(CreateDoctorForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cabinetEdit.sizePolicy().hasHeightForWidth())
        self.cabinetEdit.setSizePolicy(sizePolicy)
        self.cabinetEdit.setObjectName("cabinetEdit")
        self.horizontalLayout_7.addWidget(self.cabinetEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateDoctorForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(CreateDoctorForm)
        self.buttonBox.accepted.connect(CreateDoctorForm.accept) # type: ignore
        self.buttonBox.rejected.connect(CreateDoctorForm.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(CreateDoctorForm)

    def retranslateUi(self, CreateDoctorForm):
        _translate = QtCore.QCoreApplication.translate
        CreateDoctorForm.setWindowTitle(_translate("CreateDoctorForm", "Dialog"))
        self.label.setText(_translate("CreateDoctorForm", "Имя"))
        self.label_2.setText(_translate("CreateDoctorForm", "Фамилия"))
        self.label_3.setText(_translate("CreateDoctorForm", "Специальность"))
        self.label_5.setText(_translate("CreateDoctorForm", "Контактный телефон"))
        self.label_6.setText(_translate("CreateDoctorForm", "Email"))
        self.label_7.setText(_translate("CreateDoctorForm", "Кабинет"))
