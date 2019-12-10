#!/usr/bin/python
#coding:utf-8
import socketserver
import subprocess
import string
import time
class FileTcpServer(socketserver.BaseRequestHandler):
    def recvfile(self, filename):
        print("start recv")
        f = open(filename, 'wb')
        self.request.send('ready'.encode())
        while True:
            data = self.request.recv(1024).decode()
            # print(data)
            if data == 'EOF':
                print("recv success")
                break
            f.write(data.encode())
        f.close()
                                       
    def sendfile(self, filename):
        print("start send")
        try:
            f = open(filename, 'rb')
            while True:
                data = f.read(1024)
                if not data:
                    break
                # print(data)
                self.request.send(data)
            f.close()
            time.sleep(0.5)
            self.request.send('EOF'.encode())
            print("send success")
        except:
            self.request.send('EOF'.encode())

    def recvImage(self, filename):
        print("start recv")
        f = open(filename, 'wb')
        self.request.send('ready'.encode())
        while True:
            data = self.request.recv(1024)
            # print(data)
            if data == b'EOF':
                print("recv success")
                break
            f.write(data)
        f.close()
    def sendImage(self, filename):
        print("start send")
        # self.request.send('ready'.encode())
        try:
            f = open(filename, 'rb')
            while True:
                data = f.read(1024)
                if not data:
                    break
                # print(data)
                self.request.send(data)
            f.close()
            time.sleep(0.5)
            self.request.send('EOF'.encode())
            print("send success")
        except:
            self.request.send('EOF'.encode())
    def recvVideo(self, filename):
        print("start recv")
        f = open(filename, 'wb')
        self.request.send('ready'.encode())
        while True:
            data = self.request.recv(1024)
            # print(data)
            if data == b'EOF':
                print("recv success")
                break
            f.write(data)
        f.close()
    def sendVideo(self, filename):
        print("start send")
        # self.request.send('ready'.encode())
        try:
            f = open(filename, 'rb')
            while True:
                data = f.read(1024)
                if not data:
                    break
                # print(data)
                self.request.send(data)
            f.close()
            time.sleep(0.5)
            self.request.send('EOF'.encode())
            print("send success")
        except:
            self.request.send('EOF'.encode())
    # put代表用户需要存储文件，根据文件的类型（txt\jpg\video）执行不同的接收模式
    # get代表用户需要取文件，根据文件的类型（txt\jpg\video）执行不同的发送模式
    def handle(self):
        # 显示连接对象
        print("get connection from :",self.client_address)
        while True:
            try:
                # 接收用户请求
                data = self.request.recv(1024).decode()
                print("get client command:", data) 
                if not data:
                    print("break the connection")
                    break                
                else:
                    
                    action, filename, filetype = data.split()
                    if action == "put":
                        if filetype == 'txt':
                            self.recvfile(filename)
                        elif filetype == 'jpg':
                            self.recvImage(filename)
                        elif filetype == 'video':
                            self.recvVideo(filename)
                        else:
                            pass
                    elif action == 'get':
                        if filetype == 'txt':
                            self.sendfile(filename)
                        elif filetype == 'jpg':
                            self.sendImage(filename)
                        elif filetype == 'video':
                            self.sendVideo(filename)
                        else:
                            pass 
                    else:
                        print("get error when action!")
                        continue
            except Exception:
                print("The client has quit! Over")
                break
                                           
                                       
if __name__ == "__main__":
    host = '192.168.1.103'
    port = 1010
    s = socketserver.ThreadingTCPServer((host,port), FileTcpServer)
    s.serve_forever()