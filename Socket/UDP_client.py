# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:06:06 2017

@author: 黃大祐
UDP client
"""
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 12000
MESSAGE = "Hello, World!"
 
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)
 
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode('utf-8'),(UDP_IP, UDP_PORT))
#網路再傳只能二進位
#modifiedMessage,severAddress = sock.recvfrom(2048)
#print(modifiedMessage)
#sock.close()