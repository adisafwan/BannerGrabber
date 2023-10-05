import socket

# Declare s from socket module as socket object
s = socket.socket()

# Prompt user to enter IP address and port number
ip = input("Please enter the IP address: ")
port = input ("Please enter the port number: ")

# Connecting the ip and port to socket
s.connect((ip, port))

