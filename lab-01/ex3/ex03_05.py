# Nhập danh sách từ bàn phím
dau_vao = input("Nhập các phần tử của danh sách, phân cách bằng dấu phẩy: ")

# Tách chuỗi thành danh sách
danh_sach = dau_vao.split(',')

# Khởi tạo dictionary để đếm tần suất
dem_phan_tu = {}

# Đếm từng phần tử
for phan_tu in danh_sach:
    phan_tu = phan_tu.strip()  # Loại bỏ khoảng trắng nếu có
    if phan_tu in dem_phan_tu:
        dem_phan_tu[phan_tu] += 1
    else:
        dem_phan_tu[phan_tu] = 1

# In kết quả
print("Số lần xuất hiện của mỗi phần tử:")
for key, value in dem_phan_tu.items():
    print(f"{key}: {value}")
