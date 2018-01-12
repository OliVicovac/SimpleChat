"""
Created on 20.12.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171220

@description: Implementation eines einfachen Chat Clients
"""

from clientController import ClientController
from PyQt5 import QtCore, QtGui, QtWidgets
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="name of user client", required=False)
    parser.add_argument("--host", help="server host (default: localhost)", required=False)
    parser.add_argument("-p", "--port", help="server port (default: 5050)", required=False)
    args = parser.parse_args()

    # TODO check consistency of arguments
    username = "" if args.server is None else args.username
    host = 'localhost' if args.host is None else args.host
    port = 5050 if args.port is None else args.port

    app = QtWidgets.QApplication([])
    controller = ClientController(username, host, port)
    controller.show()
    app.exec_()

    controller.close()


if __name__ == "__main__":
    main()