# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatServer(object):
    def setupUi(self, ChatServer):
        ChatServer.setObjectName("ChatServer")
        ChatServer.resize(450, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChatServer.sizePolicy().hasHeightForWidth())
        ChatServer.setSizePolicy(sizePolicy)
        ChatServer.setLayoutDirection(QtCore.Qt.LeftToRight)
        ChatServer.setSizeGripEnabled(False)
        ChatServer.setModal(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ChatServer)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 432, 322))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName("mainLayout")
        self.messages = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messages.sizePolicy().hasHeightForWidth())
        self.messages.setSizePolicy(sizePolicy)
        self.messages.setMinimumSize(QtCore.QSize(300, 300))
        self.messages.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.messages.setBaseSize(QtCore.QSize(300, 400))
        self.messages.setObjectName("messages")
        self.mainLayout.addWidget(self.messages)
        self.userLayout = QtWidgets.QVBoxLayout()
        self.userLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.userLayout.setContentsMargins(0, -1, -1, -1)
        self.userLayout.setSpacing(10)
        self.userLayout.setObjectName("userLayout")
        self.clients = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.clients.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clients.sizePolicy().hasHeightForWidth())
        self.clients.setSizePolicy(sizePolicy)
        self.clients.setMinimumSize(QtCore.QSize(100, 270))
        self.clients.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clients.setBaseSize(QtCore.QSize(0, 0))
        self.clients.setMovement(QtWidgets.QListView.Snap)
        self.clients.setResizeMode(QtWidgets.QListView.Adjust)
        self.clients.setObjectName("clients")
        self.userLayout.addWidget(self.clients)
        self.disconnect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnect.sizePolicy().hasHeightForWidth())
        self.disconnect.setSizePolicy(sizePolicy)
        self.disconnect.setMinimumSize(QtCore.QSize(100, 20))
        self.disconnect.setMaximumSize(QtCore.QSize(100, 20))
        self.disconnect.setObjectName("disconnect")
        self.userLayout.addWidget(self.disconnect)
        self.mainLayout.addLayout(self.userLayout)

        self.retranslateUi(ChatServer)
        QtCore.QMetaObject.connectSlotsByName(ChatServer)

    def retranslateUi(self, ChatServer):
        _translate = QtCore.QCoreApplication.translate
        ChatServer.setWindowTitle(_translate("ChatServer", "Chat Server"))
        self.clients.setSortingEnabled(True)
        self.disconnect.setText(_translate("ChatServer", "Disconnect User"))

