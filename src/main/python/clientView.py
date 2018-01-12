# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatClient(object):
    def setupUi(self, ChatClient):
        ChatClient.setObjectName("ChatClient")
        ChatClient.resize(455, 381)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChatClient.sizePolicy().hasHeightForWidth())
        ChatClient.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(ChatClient)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 437, 362))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName("mainLayout")
        self.messages = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.messages.setMinimumSize(QtCore.QSize(400, 300))
        self.messages.setObjectName("messages")
        self.mainLayout.addWidget(self.messages)
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setContentsMargins(0, -1, -1, -1)
        self.inputLayout.setSpacing(10)
        self.inputLayout.setObjectName("inputLayout")
        self.input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input.setMinimumSize(QtCore.QSize(350, 30))
        self.input.setObjectName("input")
        self.inputLayout.addWidget(self.input)
        self.sendButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendButton.setMinimumSize(QtCore.QSize(45, 30))
        self.sendButton.setObjectName("sendButton")
        self.inputLayout.addWidget(self.sendButton)
        self.mainLayout.addLayout(self.inputLayout)

        self.retranslateUi(ChatClient)
        QtCore.QMetaObject.connectSlotsByName(ChatClient)

    def retranslateUi(self, ChatClient):
        _translate = QtCore.QCoreApplication.translate
        ChatClient.setWindowTitle(_translate("ChatClient", "Chat Client"))
        self.sendButton.setText(_translate("ChatClient", "Send"))

