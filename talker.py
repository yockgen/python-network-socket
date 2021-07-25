#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 80                # Reserve a port for your service.

s.connect((host, port))
st='!!!!from talker!!!'
byt=st.encode()
s.send(byt)

print (s.recv(1024).decode())
s.close()                     # Close the socket when done
