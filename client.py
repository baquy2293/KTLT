

import  socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input("nhap\n")
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()