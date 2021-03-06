#encoding:utf-8

import socket
import slaves

HOSTNAME='localhost'
HOSTPORT=8052
SERVERADDR=(HOSTNAME,HOSTPORT)

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(SERVERADDR)
serverSocket.listen(0)
clientStatistics=1
while True:
    clientSocket,clientAddr=serverSocket.accept()
    clientStatistics+=1
    print("*Client[",clientAddr[0],":",clientAddr[1],"]:",clientStatistics)
    slave=slaves.slave()
    slave.setClientInfo(clientSocket,clientAddr)
    slave.start()
