#encoding:utf-8

import socket

class Manager():
    socketHandle=None
    socketAddr=None
    def setClientInfo(self,socketHandle,socketAddr):
        self.socketHandle=socketHandle
        self.socketAddr=socketAddr
