

import urllib.request
# Import module cho phép truy cập và tương tác với URL từ Python.

from urllib.request import Request
# Import class Request từ module urllib.request  cung cấp các chức năng để tạo yêu cầu HTTP.
url = 'http://python.org'
# lưu địa chỉ URL của trang web cần truy cập vào biến url

user_agent = 'Mozilla/5.0 (Windows NT 11)'
# Định nghĩa biến user_agent là một chuỗi đại diện cho trình duyệt và hệ điều hành của người dùng.
# Trong trường hợp này, user agent là "Mozilla/5.0 (Windows NT 1)" mô tả một trình duyệt trên hệ điều hành Windows 11
def chorm_user ():
    opener = urllib.request.build_opener()
    # tạo một đối tượng có tên là opener  bằng cách sử dụng phương thức build_opener
    # là một đối tượng có khả năng gửi yêu cầu HTTP

    opener.addheaders = [('User-Agent', user_agent)]
    # cung cấp thông tin về user_agent  cho opener vừa tạo ra
    # User-Agent là một chuỗi đại diện cho một tiêu đề HTTP
    # được sử dụng để xác định loại trình duyệt và hệ điều hành của người dùng đang sử dụng khi gửi yêu cầu HTTP.
    # nó là tiêu đề mà trình duyệt sẽ gửi đến máy chủ web để xác định trình duyệt và hệ điều hành đang được sử dụng.
    # user_agent: Biến này chứa giá trị của tiêu đề User-Agent trong trường hợp này là 'Mozilla/5.0 (Windows NT 11)'.
    # Đây là một giả mạo User-Agent cho một trình duyệt web chạy trên hệ điều hành Windows 11

    urllib.request.install_opener(opener)
    #urllib.request.install_opener(opener) Dòng này cài đặt Opener đã tạo trước đó bằng cách sử dụng hàm build_opener()
    # việc cài đặt Opener có nghĩa là chúng ta xác định Opener này là Opener mặc định được sử dụng cho tất cả các yêu cầu HTTP tiếp theo được thực hiện bằng thư viện urllib.request
    # đảm bảo rằng mọi yêu cầu HTTP sau này sẽ được gửi với các cài đặt mà Opener đã chứa, bao gồm cả tiêu đề User-Agent đã được thiết lập trước đó

    request = urllib.request.urlopen(url)
#response = urllib.request.urlopen(url): Dòng này gửi một yêu cầu HTTP đến URL được chỉ định ('http://python.org') bằng cách sử dụng hàm urlopen() từ module urllib.request.
    # Do Opener đã được cài đặt trước đó, yêu cầu này sẽ được gửi với các cài đặt đã được xác định trong Opener chứa thông tin như mã trạng thái, tiêu đề và nội dung của phản hồi từ máy chủ.
    # Đối tượng request chứa thông tin cần thiết về trang web đã được yêu cầu.

    print("response headers")
    print('-----------------')
    for header,value in request.getheaders():
        print(header+": " + value)
     # duyệt và lấy danh sách các tiêu đề của yêu cầu

    request = Request(url)
    # taoj đối tượng request với url được chỉ định

    request.add_header("User-Agent", user_agent)
    #  ta thêm tiêu đề "User-Agent" với giá trị của biến user_agent

    print("\nrequest headers")
    print('-----------------')

    for header,value in request.headers.items():
        print(header+": " + value)
        #  lặp qua tất cả các tiêu đề của yêu cầu HTTP sử dụng phương thức items() của thuộc tính headers của đối tượng request, và in ra mỗi tiêu đề và giá trị tương ứng của nó.


if __name__ == '__main__':
    chorm_user()
