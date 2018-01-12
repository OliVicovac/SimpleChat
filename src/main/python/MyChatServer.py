"""
Created on 30.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171130

@description: Implementation eines einfachen Chat Servers
"""

from serverController import ServerController
from PyQt5 import QtWidgets
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", help="name of server instance (default: ServerAdmin)", required=False)
    parser.add_argument("-l", "--listen", help="server hostname or IP address for incoming clients (default: localhost)", required=False)
    parser.add_argument("-p", "--port", help="port number (default: 5050)", required=False)
    args = parser.parse_args()

    # TODO check consistency of arguments
    server_name = 'ServerAdmin' if args.server is None else args.server
    listen = 'localhost' if args.listen is None else args.listen
    port = 5050 if args.port is None else args.port

    app = QtWidgets.QApplication([])
    controller = ServerController(server_name, listen, port)
    controller.show()
    app.exec_()

    controller.close()


if __name__ == "__main__":
    main()
