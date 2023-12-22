import csv
import base64
from bs4 import BeautifulSoup
import requests

with open('10Hanoi.csv', "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ['oke']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Move this outside the loop

    prefix = "https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10?key=aW5wdXREgBHx5LLwS"
    field_code = "YXRhPTEz"
    middle_code = "DsqOznbvq"
    suffix = "h1D0qxcHiZ0eXBlQ2hlY2s9MDI="

    for i in range(9001, 10000):
        try:
            index_base64 = base64.b64encode(str(i).encode()).decode()
            modified_base64 = index_base64[:-3] + chr(ord(index_base64[-3]) + 2)
            url = f"{prefix}{field_code}{middle_code}{modified_base64}{suffix}"
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            html_content = response.text

            # Sử dụng BeautifulSoup để parse HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Tìm tất cả các thẻ <b>
            b_tags = soup.find_all('b')

            # Lặp qua từng thẻ và lấy nội dung
            data_list = [b_tag.text.strip() for b_tag in b_tags]
            writer.writerow({'oke': data_list})
        except requests.exceptions.RequestException as e:
            print(f"Error for index {i}: {e}")
