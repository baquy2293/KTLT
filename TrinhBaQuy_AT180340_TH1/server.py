import socket


HOST = 'localhost'
#thiết lập địa chỉ server
PORT = 8000
#thiết lập cổng để kết nối để kết nối với sẻrver

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# cấu hình socket
# socket.AF_INET:Thiết lập địa chỉ kết nối dưới dạng IPV4
# socket.SOCK_STREAM: Thiết lập giao thức cho socket thuộc loại TCP

serverSocket.bind((HOST, PORT))
# dùng để lắng nghe đến địa chỉ ip và cổng được thiết lập ở trên

serverSocket.listen(1)
#lắng nghe 1 kết nối

conn, addr = serverSocket.accept()
#chấp nhận kết nối từ client và trả về đối tượng socket là conn và địa chỉ là addr

with conn:
    print('Connected by', addr)
    #in ra được kết nối với addr

    while True:
        data = conn.recv(1024)
        #nhận nội dung từ client gửi tới ở dạng mã hóa qua giao thức TCP

        print('Client Sent:', data.decode())
        # giải mã nội dung nhận được và in ra màn hình

        data_upper = data.decode().upper()
        #tạo biến data_upper lưu data ở dạng inhoa thông qua hàm upper để gửi về client

        conn.sendall(data_upper.encode())
        #gửi data về client ở dạng mã hóa  thông qua kết nối TCP đã thiết lập

        if not data:
            break
        #nếu hết data thì dừng 
conn.close()
#đóng kết nối

serverSocket.close()
#đóng socket
