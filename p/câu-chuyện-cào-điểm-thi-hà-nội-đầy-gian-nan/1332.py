import requests
from bs4 import BeautifulSoup

url = "https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10?key=aW5wdXREgBHx5LLwSYXRhPTEzDsqOznbvqOTAzMyh1D0qxcHiZ0eXBlQ2hlY2s9MDI="

# Gửi yêu cầu HTTP và lấy về nội dung HTML
response = requests.get(url)
html_content = response.text

# Sử dụng BeautifulSoup để parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Tìm tất cả các thẻ <b>
b_tags = soup.find_all('b')

# Lặp qua từng thẻ và in ra nội dung
for b_tag in b_tags:
    print(b_tag.text.strip(), end =",")
