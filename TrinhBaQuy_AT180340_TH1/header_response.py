
import requests

url = "http://google.com"

# Thực hiện GET request
response = requests.get(url)
#hàm get tự động xử lý việc tạo request và nhận response.

# In ra tất cả các headers của response
print("Response Headers:")
print("------------------")
for header, value in response.headers.items():
    print(f"{header}: {value}")
