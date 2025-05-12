# Nhập dictionary từ người dùng
dau_vao = input("Nhập các cặp key:value, phân cách bằng dấu phẩy (ví dụ: a:1,b:2,c:3): ")

# Tạo dictionary từ chuỗi nhập vào
dict_nguoi_dung = {}
for cap in dau_vao.split(','):
    if ':' in cap:
        key, value = cap.split(':')
        dict_nguoi_dung[key.strip()] = value.strip()

# Hiển thị dictionary ban đầu
print("Dictionary ban đầu:", dict_nguoi_dung)

# Nhập key cần xóa
key_xoa = input("Nhập key cần xóa: ").strip()

# Xóa key nếu tồn tại
if key_xoa in dict_nguoi_dung:
    del dict_nguoi_dung[key_xoa]
    print(f"Đã xóa phần tử có key '{key_xoa}'.")
else:
    print(f"Key '{key_xoa}' không tồn tại trong dictionary.")

# Hiển thị dictionary sau khi xóa
print("Dictionary sau khi xóa:", dict_nguoi_dung)
