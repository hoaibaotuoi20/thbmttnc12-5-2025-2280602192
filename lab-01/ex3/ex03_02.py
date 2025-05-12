# Hàm đảo ngược danh sách
def dao_nguoc_danh_sach(danh_sach):
    return danh_sach[::-1]  # Dùng slicing để đảo ngược

# Nhập danh sách từ người dùng
dau_vao = input("Nhập các phần tử trong danh sách, phân cách bằng dấu phẩy: ")

# Tách và chuyển sang danh sách
danh_sach = dau_vao.split(',')

# Đảo ngược danh sách
danh_sach_dao = dao_nguoc_danh_sach(danh_sach)

# In kết quả
print("Danh sách sau khi đảo ngược là:", danh_sach_dao)
