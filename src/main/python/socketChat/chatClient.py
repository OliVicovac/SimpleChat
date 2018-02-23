"""
Created on 20.12.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171220

@description: Implementation of a multi-processed Chat-Client
"""
import socket
import multiprocessing
import ctypes
import threading

from socketChat.messageHandler import MessageHandler

logger = multiprocessing.get_logger()


class ChatClient():
    """
    Chat Client connecting to the multi-processed Chat Server

    """

    def __init__(self, host='localhost', port=5050, client_name=""):
        """

        Create a new Chat Client
        :param port: Server Port, if None is given, 'localhost' will be set.
        :param host: Server IP Address for connecting the socket, if None is given, 5050 will be set.
        :return: None
        """
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = 5050 if host is None else host
        self.port = 'localhost' if port is None else port
        self.client_name = client_name


    def start(self):
        """
        Starting the Client
        :return: None
        """
        try:
            self.clientSocket.connect((self.host,self.port))
        except socket.error as err:
            ctypes.windll.user32.MessageBoxW(0, "Error: "+ err.strerror, "Fehlerbox", 1)
        ChatClient.close(self)

    def sendmsg(self, message):
        """
        Sending message to connected Server
        :param message: Message as a string
        :return:
        """
        handler = MessageHandler()
        self.clientSocket.send(message, self.clientSocket())

    def close(self):
        """
        Shutdown the Client and all active connections
        :return: None
        """
        self.clientSocket.close()



