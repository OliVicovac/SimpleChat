"""
Created on 20.12.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171220

@description: Implementation of a simple message handler
based on http://codingnights.com/coding-fully-tested-python-chat-server-using-sockets-part-1/
"""
import multiprocessing, struct

logger = multiprocessing.get_logger()


class MessageHandler:
    ENCODING = 'utf-8'
    RECV_BUFSIZE = 4096
    RECV_MSG_LEN = 4

    MSG_DELIMITER = '\r\n'

    CMD_ACK = '/ACK'
    CMD_EXIT = '/EXIT'
    CMD_NAME = '/NAME'
    CMD_LIST = CMD_ACK+CMD_EXIT+CMD_NAME

    def receive(self, socket):
        """
        Receives an incoming message from the client and unpacks it.

        :param socket: the incoming socket
        :return: the unpacked string message
        """
        data = None
        msg_len = None

        # Retrieves the first 4 bytes from the message
        tot_len = 0
        while tot_len < self.RECV_MSG_LEN:
            msg_len = socket.recv(self.RECV_MSG_LEN)
            tot_len += len(msg_len)
        # If the message has the 4 bytes representing the length
        if msg_len is not None:
            data = bytes()
            # Unpacks the message and gets the message length
            msg_len = struct.unpack('>I', msg_len)[0]
            tot_data_len = 0
            while tot_data_len < msg_len:
                # Retrieves the chunk i-th chunk of RECV_BUFFER size
                chunk = socket.recv(self.RECV_BUFSIZE)

                # If there isn't the expected chunk
                if not chunk:
                    data = None
                    break
                else:
                    # Merges the chunks content
                    data += chunk
                    tot_data_len += len(chunk)

        message = data.decode(self.ENCODING)
        show_debug("receive::message: "+message)

        # If there is a bouncing Info in message, only take the first part
        message = message.split(self.MSG_DELIMITER)[0]

        return message

    def send(self, message, socket):
        """
        Prefixes each message with a 4-byte length before sending.

        :param socket: the outgoing socket
        :param message: the string message to send
        """
        # Sets the defined end of a message
        show_debug("send::message: " + message)
        message += self.MSG_DELIMITER

        # Packs the message with 4 leading bytes representing the message length
        data = struct.pack('>I', len(message)) + bytes(message.encode(self.ENCODING))

        # Sends the packed message
        socket.send(data)


def show_info(info_message):
    logger.info("MSG_HANDLER::"+info_message)


def show_debug(debug_message):
    logger.debug("MSG_HANDLER::" + debug_message)


def show_error(error_message):
    logger.debug("MSG_HANDLER::"+error_message)