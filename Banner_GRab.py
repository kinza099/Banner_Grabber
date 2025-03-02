#!/usr/bin/python3

import socket
import pyfiglet

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024).decode())

def main():
  
    ascii_banner = pyfiglet.figlet_format("Banner Grabber")
    print(ascii_banner)

    ip = input("Please Enter the IP Address: ")
    port = str(input("Enter the Port: "))
    banner(ip, port)

if __name__ == "__main__":
    main()