#encoding:utf-8

import struct

def step1(cmd):
    if cmd[0] != 5:
        return (-1,"Version Not Support",cmd[0])
    if cmd[1] != 1:
        return (-2,"Unsupported NMETHOD Value",cmd[1])
    if cmd[2] != 0:
        return (-3,"Invalid Method Value",cmd[2])
    return (0,"OK")
def step2(cmd):
    if cmd[0] != 5:
        return (-1,"Unsupported METHOD Value")
    if cmd[1] != 1:
        return (-2,"Unsupported CMD")
    if cmd[2] != 0:
        return (-3,"Reserved Value Must Set to Zero")
    if cmd[3] != 1:
        return (-4,"Unsupported Address Type,Only Supported IPv4 Now")
    dstAddr="%s.%s.%s.%s" % tuple(cmd[4:8])
    dstPort=struct.unpack('H',struct.pack('2B',cmd[9],cmd[8]))
    return (0,dstAddr,dstPort)
