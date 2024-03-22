import requests
logins = []
with open('E:/pyhton/pythonProject/Th2/login.txt', 'r') as filehandle:
    for line in filehandle:
        login = line[:-1]
        logins.append(login)
domain = 'http://testphp.vulnweb.com'
for login in logins:
    # In ra màn hình url đang thực hiện
    print("Checking..." + domain + login)
    # Gửi yêu câu tới url đang thực hiện và gán giá trị trả về là response
    response = requests.get(domain + login)
    # Nếu giá trị trả về là 200 thì là thành công
    if response.status_code == 200:
        print("Login resource detected: " + login)