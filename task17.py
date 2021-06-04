import socket
import os
import threading


s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip = "192.168.43.94"
port = 1009
s.bind( (ip , port) )

clientip = input("enter client ip:")
print("welcome to chat server")
print("**************************************************************")

def send():
    while True:
        p = input("JACK:")
        data = p.encode()
        s.sendto(data ,("192.168.43.211" , 1709))


def receive():
    while True:
        x = s.recvfrom(1234)
        data = x[0].decode()
        print("\t\t\t\t JILL"+ ":" +data)


x1 = threading.Thread(target = receive)
x2 = threading.Thread(target = send)
x1.start()
x2.start()
