import socket, sys

ip = input("Digite o ip: ")
porta = int(input("Digite a porta: "))

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
respo = client.connect_ex((ip, porta))

if (respo == 0):
    print("porta está aberta")
else:
    print("porta fechada")

