# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:12:31 2017

@author: 黃大祐
"""
import socket
    
UDP_IP = "127.0.0.1"
UDP_PORT = 12000
    
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT)) 
while True:
   data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
   print("received message:", data)
