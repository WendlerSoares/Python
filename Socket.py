import socket
try:
    #                         IPV4               TCP
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print("houve um erro durante a criação do socket")
    exit()
host = "" #127.0.0.1
porta= 9999

tcp_socket.bind((host,porta)) #listening
tcp_socket.listen(1)

while True:
    c, addr = tcp_socket.accept()
    print("connection from {}:{}".format(addr[0],addr[1]))



tcp_socket.close() #fechar server