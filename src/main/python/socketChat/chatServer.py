"""
Created on 20.12.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171220

@description: Implementation of a multi-processed Chat-Server
"""
import multiprocessing, threading, ctypes
import socket
import logging, traceback
from socketChat.messageHandler import MessageHandler

logger = multiprocessing.log_to_stderr(logging.INFO)


class ChatServer:
    """
    Multi-processed Chat-Server

    Every client has its own Handler, which manages sending and receiving messages
    """

    BACKLOG = 2
    connections = []

    def __init__(self, address, port):
        """
        Create a new Chat Server
        
        :param address: IP-Address as string. If None is given, 'localhost' will be set.
        :param port: Port number. If None is given, 505 will be set.
        :return: None
        """
        self.address = 'localhost' if address is None else address
        self.port = 5050 if port is None else port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def start(self):
        """
        Start the Server after successful Initialisation
        :return: None
        """
        self.serverSocket.bind((str(self.address), int(self.port)))
        self.serverSocket.listen(1)

    def send(self, message, sender=-1, recipients=None):
        """
        Send message to clients
        :param message: String message
        :param sender: Number of client, who is sending the message
        :param recipients: List of numbers to whom the message should be delivered
        :return: None
        """
        self.s.sendall(message)



    def remove(self, number=-1):
        """
        Remove the client with the corresponding number
        If no number is given, close and remove all clients
        :param number:
        :return: None
        """
        pass

    def get_active_clients(self):
        """
        Get a list of active clients in the format (client_number, client_name)
        :return: [client_number, client_name]
        """
        pass

    def close(self):
        """
        Close the server and all active connections
        :return: None
        """

