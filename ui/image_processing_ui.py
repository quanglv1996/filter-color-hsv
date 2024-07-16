# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Projects-Persional\filter-color-hsv\ui\image_processing.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(962, 718)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonCamera = QtWidgets.QRadioButton(Form)
        self.radioButtonCamera.setObjectName("radioButtonCamera")
        self.verticalLayout.addWidget(self.radioButtonCamera)
        self.radioButtonImage = QtWidgets.QRadioButton(Form)
        self.radioButtonImage.setObjectName("radioButtonImage")
        self.verticalLayout.addWidget(self.radioButtonImage)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButtonApply = QtWidgets.QPushButton(Form)
        self.pushButtonApply.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButtonApply.setObjectName("pushButtonApply")
        self.horizontalLayout.addWidget(self.pushButtonApply)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 20)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameConfig = QtWidgets.QFrame(Form)
        self.frameConfig.setAutoFillBackground(True)
        self.frameConfig.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameConfig.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameConfig.setObjectName("frameConfig")
        self.verticalLayout_3.addWidget(self.frameConfig)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonExportConfig = QtWidgets.QPushButton(Form)
        self.pushButtonExportConfig.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButtonExportConfig.setObjectName("pushButtonExportConfig")
        self.horizontalLayout_2.addWidget(self.pushButtonExportConfig)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonLoadConfig = QtWidgets.QPushButton(Form)
        self.pushButtonLoadConfig.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButtonLoadConfig.setObjectName("pushButtonLoadConfig")
        self.horizontalLayout_2.addWidget(self.pushButtonLoadConfig)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.labelNotify = QtWidgets.QLabel(Form)
        self.labelNotify.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNotify.setObjectName("labelNotify")
        self.verticalLayout_3.addWidget(self.labelNotify)
        self.verticalLayout_3.setStretch(0, 20)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 20)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "Image processing"))
        self.label_2.setText(_translate("Form", "Choose type"))
        self.radioButtonCamera.setText(_translate("Form", "Camera"))
        self.radioButtonImage.setText(_translate("Form", "Image"))
        self.pushButtonApply.setText(_translate("Form", "Apply"))
        self.label_3.setText(_translate("Form", "Viewer"))
        self.pushButtonExportConfig.setText(_translate("Form", "Export config"))
        self.pushButtonLoadConfig.setText(_translate("Form", "Load config"))
        self.labelNotify.setText(_translate("Form", "Notify"))
