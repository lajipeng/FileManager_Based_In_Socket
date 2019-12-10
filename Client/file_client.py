#!/usr/bin/python
#coding:utf-8
import socket
import sys
import time

class fileClient:
    # 创建客户的套接字。AF_INET 指示底层网络使用的IPv4，SOCK_STREAM指示套接字类型
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将服务器的端口号serverPort与该套接字关联起来
    def connect(self, ip, port):
        self.sock.connect((ip, port))
    # sendFile 执行打开文件并且发送数据，文件发送完毕之后向服务器发送“EOF”表示传输已经完成
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
    # sendFile 执行打开文件并且写入接收的数据，收到“EOF”表示传输已经完成
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
    # command 为用户输入的命令行，我们根据用户输入的信息判断执行哪一类操作
    def input(self, command):
        if not command:
            return
        action, filename, filetype = command.split()
        # put代表用户需要存储文件，根据文件的类型（txt\jpg\video）执行不同的发送模式
        # 在发送之前，需要调用self.confirm(command)确认服务器是否已经准备接收数据，
        # 接到服务器指示后，返回True继续执行相应的发送模式
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

        # get代表用户需要取文件，根据文件的类型（txt\jpg\video）执行不同的接收模式
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
    # 关闭套接口
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