import socket

HOST = input("Nhập ip cần kiểm tra: ")

number_port = int(input("nhập số port muốn kiếm tra\n"))
# nhập số lượng các port mà muốn kiểm tra

listPort = []
# tạo ra một mảng để lưu trưx các port của người dùng nhập vào



def scan_list_port(number):# đầu tiên ta tạo một hàm để người dùng có thể nhập port
    for port in range(0,number):
        # vòng for chạy lần lượt n các port

        listPort.append(int(input(f"Nhập port thứ {port+1} ")))
        # câu lệnh trên dùng để nhập một port và lưu vào mảng
        # apppend có chức năng thêm một phẩn tử vào cuối mảng
        # input dùng để nhập dữ liệu  từ bàn phím
        # int ()  dùng để nhập vào một số dạng số nguyên
        # f""  dùng để có thể hiện thị giá trị của một biến trong câu lệnh in ra màn hình


def scan_port(host):
    # gọi lại hàm nhập các giá trị port
    scan_list_port(number_port)

    # duyệt lần lượt các port chưa trong mảng
    for i in range(0,number_port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Tạo socket
        # tham số đầu tiên  cho biết kiểu địa chỉ IP socket.AF_INET:Thiết lập địa chỉ kết nối dưới dạng IPV4
        # tham số thứ 2 socket.SOCK_STREAM: Thiết lập giao thức cho socket thuộc loại TCP

        s.settimeout(6)  # Đặt thời gian chờ để tránh chờ quá lâu cho các cổng không mở

        result = s.connect_ex((host, listPort[i]))
        # tạo một biến để lưu kết quả trả về
        # phương thức connect_ex() là đối tượng của socket để kết nối đến địa chỉ đa cung cấp ở trên và cổng được nhập
        # phương thức này trả về 0 nếu được kết nối thành công và ngược lại
        # (host, listPort[i])  là các cặp giá trị ban đầu là địa chỉ IP  và thứ 2 là cổng muốn thử kết nối

        if result == 0:# nếu thành công sẽ trả về một
            print(f"Port {listPort[i]} mở")
        else:# ngươic lại sẽ là kết nối khong thành công
            print(f"Port {listPort[i]} đóng")

scan_port(HOST)
# gọi hàm thực hiện Kiểm tra các dịch vụ đang mở của máy chủ đích