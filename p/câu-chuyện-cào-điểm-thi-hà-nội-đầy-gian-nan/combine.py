import base64
from bs4 import BeautifulSoup
import requests

prefix = (
    "https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10?key=aW5wdXREgBHx5LLwS"
)
field_code = "YXRhPTEz"
middle_code = "DsqOznbvq"
suffix = "h1D0qxcHiZ0eXBlQ2hlY2s9MDI="

for i in range(9001, 10000):
    try:
        index_base64 = base64.b64encode(str(i).encode()).decode()
        modified_base64 = index_base64[:-3] + chr(ord(index_base64[-3]) + 2)
        url = f"{prefix}{field_code}{middle_code}{modified_base64}{suffix}"
        response = requests.get(url)
        response.raise_for_status()

        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        b_tags = soup.find_all("b")

        for b_tag in b_tags:
            #Các thông tin cách nhau bởi dấu "," để tách ra khi sử dụng csv để lưu trữ
            print(b_tag.text.strip(), end =",")
        print("\n")

    except requests.exceptions.RequestException as e:
        print(f"Error for index {i}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for index {i}: {e}")
