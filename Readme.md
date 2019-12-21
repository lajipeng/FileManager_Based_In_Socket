# FileManager based on socket

## Introduction

Use socket programming to implement a simple file server. The client program implements put (to transfer a file from the local to the file server) and get (to save a remote file from the file server as a local file). The client and file server are not on the same machine.

## How to start

- Download the two folders and same them respectively on two different machines

- Change the IP address in the file_server.py. Here is the position! I recommend you should input **ipconfig** in a cmd window and then you could get the IP of host!  Remember that you should input the same IP address in the client-user-window.

  ![ChangeIPinCode](Report\ChangeIPinCode.png)

- Go to the /Server and run the  **Run_me_to_activate_server.bat** which is used to run file_server.py before you have finished the above tips. Now the server is running and thus the client can send request to the server.

- Go to the /Client and run the **Run_me_to_login.bat** which is used to run file_client.py Now the client is activated. Just follow the instructions.

  This is a test reference. You just need to input those content. If you type the wrong cipher, don't worry about it because you have three chances!
  Don't forget to change your IP address! Please note that this is the server IP . 

  If  your computer is connecting the wifi, I recommend you to choose the follows(after you input "ipconfig" in cmd.exe)

![IPconfig](Report\IPconfig.png)

IP：10.223.240.198
Username：Wang Peng
PassWord：AA
Command：put test1.txt txt
Command：Y
Command：put test1.jpg jpg
Command：Y
Command：put test1.avi video
Command：Y
Command：get test2.txt txt
Command：Y
Command：get test2.jpg jpg
Command：Y 
Command：get test2.avi video

Command：N

- Untill now, congratulationsions!  you have done all the test! 
- I would appreciate it if you could  give me a star.