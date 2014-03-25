#encoding:utf-8

import socket
import threading
import sockutils
import struct

class slave(threading.Thread):
    socketHandle=None
    socketAddr=None
    proxySocket=None
    def setClientInfo(self,socketHandle,socketAddr):
        self.socketHandle=socketHandle
        self.socketAddr=socketAddr
    def run(self):
        try:
            cmd=self.socketHandle.recv(3)
            if sockutils.step1(cmd)[0] != 0:
                print(sockutils.step1(cmd))
                exit(-1)
            self.socketHandle.send(b'\x05\x00')
            cmd=self.socketHandle.recv(10)
            step2Ret=sockutils.step2(cmd)
            if step2Ret[0] != 0:
                exit(-1)
            print("线程:",self.name,"连接",step2Ret[1],":",step2Ret[2][0])
            step2Hex=struct.pack(">BBBBBBBBH",5,0,0,1,cmd[4],cmd[5],cmd[6],cmd[7],cmd[8]+cmd[9])
            self.socketHandle.send(step2Hex)
            data=b""
            while True:
                tmp=self.socketHandle.recv(256)
                data+=tmp
                if len(tmp)<256:
                    break
            if data == b'':
                print(self.name,"没有数据，断开连接")
                exit()
            self.proxySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.proxySocket.connect((step2Ret[1],step2Ret[2][0]))
            self.proxySocket.send(data)
            while True:
                tmp=self.proxySocket.recv(10240)
                self.socketHandle.send(tmp)
                if len(tmp)==0:
                    break
            self.proxySocket.close()
            self.socketHandle.close()
            print("----",self.name,"end----")
        except Exception as e:
            self.proxySocket.close()
            self.socketHandle.close()
            print(e)
            print("----",self.name,"Exception End----")
        
