import shodan
import os
# Khai báo API key của Shodan
# api_key = os.environ['SHODAN_API_KEY']  # Thay YOUR_API_KEY bằng API key của bạn
#
# print(api_key)
# Tạo đối tượng API của Shodan
api = shodan.Shodan('eGvZsD76Wpy40np4U4f60T8XBBH11XWD')

# Thực hiện tìm kiếm
query = "port: 21 Anonymous user logged in"  # Thay 'apache' bằng từ khóa tìm kiếm của bạn
try:
    # Thực hiện truy vấn
    results = api.search(query)

    # In kết quả
    print('Số kết quả tìm thấy:', results['total'])
    for result in results['matches']:
        print('IP:', result['ip_str'])
        print(result['data'])
        print('')
except shodan.APIError as e:
    print('Error:', e)
