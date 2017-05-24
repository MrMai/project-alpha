import os, time, socket

port = 4445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
'''
#while True:
    connection, address = s.accept()
    print("connection established to [REDACTED]")
    headercommand = connection.recv(25)
    print(headercommand)
    connection.close()
'''
connection, address = s.accept()
print("connection established to [REDACTED]")
headercommand = connection.recv(25)
print(headercommand)
connection.close()

def socketstart():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen()
