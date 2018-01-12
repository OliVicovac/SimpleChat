"""
Created on 30.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171130

@description: Implementation eines einfachen Chat Servers
              
"""

from serverView import Ui_ChatServer as ServerView
from socketChat.chatServer import ChatServer

from PyQt5 import QtCore, QtGui, QtWidgets


class ServerController(object):

    def __init__(self, server_name, address, port):
        """
        Creates a new Server GUI

        :param server_name:
        :param address:
        :param port:
        """

        self.dialog = QtWidgets.QDialog()
        self.view = ServerView()

        self.chat_server = ChatServer(address, port)
        self.chat_server.start()

        self.view.setupUi(self.dialog)
        self.dialog.setLayout(self.view.mainLayout)
        self.view.messages.addItem(server_name + ": Chat Server is up and running")

    def show(self):
        """
        Shows the Dialog
        :return: None
        """
        self.dialog.show()

    def received(self, data):
        """
        Write data to Message-Widget-List
        :param data: string data
        :return: None
        """
        self.view.messages.addItem(data)

    def close(self):
        """
        Closes the Server and all active client connections
        :return:
        """
        self.chat_server.close()
