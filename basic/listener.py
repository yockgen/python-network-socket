#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = '192.168.0.9' #socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from ', addr)

   talkerMsg  = "dummy" #c.recv(1024).decode()

   print('msg from talker - ', talkerMsg )
    
   strMsg = 'yockgen!!!!!yockgen!!!' +  talkerMsg
   c.send(strMsg.encode())
   c.close()                # Close the connection
