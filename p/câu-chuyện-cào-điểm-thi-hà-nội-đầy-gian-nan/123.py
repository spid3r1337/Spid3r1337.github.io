import base64

def generate_key_sequence():
    # Đoạn mở đầu
    prefix = "https://tsdaucap.hanoi.gov.vn/TraCuu/KetQuaTraCuuTuyenSinh10?key=aW5wdXREgBHx5LLwS"
    # Mã trường
    field_code = "YXRhPTEz"
    # Đoạn giữa
    middle_code = "DsqOznbvq"
    # Đoạn cuối
    suffix = "h1D0qxcHiZ0eXBlQ2hlY2s9MDI="

    # Duyệt qua các số từ 9001 đến 9999
    for i in range(9001, 10000):
        # Chuyển số sang base64
        index_base64 = base64.b64encode(str(i).encode()).decode()
        # Tăng giá trị ký tự cuối cùng lên 2
        modified_base64 = index_base64[:-3] + chr(ord(index_base64[-3]) + 2)
        # Ghép các thành phần để tạo key
        key = f"{prefix}{field_code}{middle_code}{modified_base64}{suffix}"
        # In key ra màn hình hoặc lưu vào một danh sách/tệp tin tùy ý
        print(key)
# Gọi hàm để gen ra các key
generate_key_sequence()
