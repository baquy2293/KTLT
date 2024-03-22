import socket

HOST = 'localhost'
#thiết lập địa chỉ client
PORT = 8000
#thiết lập cổng để kết nối để kết nối với client

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# cấu hình socket
# socket.AF_INET:Thiết lập địa chỉ kết nối dưới dạng IPV4
# socket.SOCK_STREAM: Thiết lập giao thức cho socket thuộc loại TCP

clientSocket.connect((HOST, PORT))
#kết nối tới port và host như trên ở đây là localhost 127.0.0.1

data = input('Enter text to send to server: ')
#data được nhập vào từ input và lưu vào biến data

clientSocket.sendall(data.encode())
#gửi data về server ở dạng mã hóa  thông qua kết nối TCP đã thiết lập

data_upper = clientSocket.recv(1024)
#lưu data nhận được từ server gửi về ở biến data_upper "data đang ở dạng mã hóa vaf nhận dưới giao thức TCP"

print('Server Response:', data_upper.decode())
#in ra data ở dạng clear text 
clientSocket.close()
#đóng socket