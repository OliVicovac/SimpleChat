"""
Created on 20.12.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171220

@description: Implementation eines Chat Controllers
              
"""
from clientView import Ui_ChatClient as ClientView
from socketChat.chatClient import ChatClient
from PyQt5 import QtCore, QtGui, QtWidgets


class ClientController(object):

    def __init__(self, client_name, host=None, port=None):
        self.dialog = QtWidgets.QDialog()
        self.view = ClientView()

        self.client = ChatClient(host, port, client_name=client_name)
        self.client.start()


        self.view.setupUi(self.dialog)

        self.dialog.setLayout(self.view.mainLayout)
        self.view.sendButton.clicked.connect(self.send)

    def show(self):
        self.dialog.show()

    def send(self):
        message = self.view.input.text()
        self.view.input.clear()

        self.client.sendmsg(message)

    def received(self, data):
        print(data)
        self.view.messages.addItem(data)

    def close(self):
        self.client.close()
