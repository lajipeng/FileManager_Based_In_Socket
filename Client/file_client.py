#!/usr/bin/python
#coding:utf-8
import socket
import sys
import time

class fileClient:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip, port):
        self.sock.connect((ip, port))

    def sendFile(self, filename):
        f = open(filename, 'rb')
        while True:
            data = f.read(4096)
            # print(data)
            if not data:
                print("send all")
                break
            self.sock.sendall(data)
        f.close()
        time.sleep(0.5)
        self.sock.sendall('EOF'.encode())

    def recvFile(self, filename):
        f = open(filename, 'wb')
        while True:
            data = self.sock.recv(4096).decode()
            if data == 'EOF':
                print('copy it!')
                break
            f.write(data.encode())
        f.close()

    def sendImage(self, filename):
        f = open(filename,'rb')
        while True:
            data = f.read(4096)
            # print(data)
            if not data:
                print("send all")
                break
            self.sock.sendall(data)
        f.close()
        time.sleep(1)
        self.sock.sendall('EOF'.encode())

    def recvImage(self, filename):
        f = open(filename, 'wb')
        while True:
            data = self.sock.recv(1024)
            # print(data)
            if data == b'EOF':
                print('copy it')
                break
            f.write(data)
        f.close() 

    def sendVideo(self, filename):
        f = open(filename,'rb')
        while True:
            data = f.read(4096)
            # print(data)
            if not data:
                print("send all")
                break
            self.sock.sendall(data)
        f.close()
        time.sleep(1)
        self.sock.sendall('EOF'.encode())

    def recvVideo(self, filename):
        f = open(filename, 'wb')
        while True:
            data = self.sock.recv(1024)
            # print(data)
            if data == b'EOF':
                break
            f.write(data)
        f.close()

    def confirm(self, command):
        self.sock.send(command.encode())
        data = self.sock.recv(4096).decode()
        print(data)
        if data == 'ready':
            return True

    def input(self, command):
        if not command:
            return
        action, filename, filetype = command.split()
        if action == 'put':
            if filetype == 'txt':
                if self.confirm(command):
                    self.sendFile(filename)
                else:
                    pass
            elif filetype == 'jpg':
                if self.confirm(command):
                    self.sendImage(filename)
                else:
                    pass
            elif filetype == 'video':
                if self.confirm(command):
                    self.sendVideo(filename)
                else:
                    pass
            else:
                pass


        elif action == 'get':
            if filetype == 'txt':
                self.sock.send(command.encode())
                self.recvFile(filename)
            elif filetype == 'jpg':
                self.sock.send(command.encode())
                self.recvImage(filename)
            elif filetype == 'video':
                self.sock.send(command.encode())
                self.recvVideo(filename)
            else:
                pass
        else:
            pass

    def close(self):
        self.sock.close()

if __name__ == '__main__':
    fc = fileClient()
    IP_fileManager = input("Please into the fileManager IP：")
    print ("Connecting: ", IP_fileManager)
    fc.connect(IP_fileManager, 1010)
    nameClient = input("Please input your username：")
    passWord = input("Please input your password：")
    print("Loading...")
    print("Welcome back！",nameClient)
    try:
        while True:
            command = input("Please input your command：(put/get filename.txt/jpg/avi txt/jpg/video)\n")
            fc.input(command)
            YN = input("Do you want to continue?(Y/N)\n")
            if(YN == 'N'):
                break
            elif(YN == 'Y'):
                continue
            else:
                print("Input error! Quit")
                break
    except:
        print('error! Quit')