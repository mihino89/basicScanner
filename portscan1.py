#!/usr/bin/python

import socket 
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
# socket.SOCK_STREAM means that: packet by TCP

host = raw_input("[*] Enter the host to SCAN: ")
#port = int(raw_input("[*] Enter the port to SCAN: "))


def portscanner(port):
    if sock.connect_ex((host, port)):
        print(colored("[!!] Port %s is closed" % (port), 'red'))
    else:
        print(colored("[+] Port %s is opened" % (port), 'green'))

for port in range(1,1000):
    portscanner(port)
