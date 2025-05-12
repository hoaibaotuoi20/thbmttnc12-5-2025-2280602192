# Nhập danh sách từ bàn phím
dau_vao = input("Nhập các phần tử của danh sách, phân cách bằng dấu phẩy: ")

# Tạo List từ chuỗi đầu vào
danh_sach = dau_vao.split(',')

# Chuyển List thành Tuple
tuple_ket_qua = tuple(danh_sach)

# In kết quả
print("Danh sách (List) vừa nhập là:", danh_sach)
print("Tuple được tạo là:", tuple_ket_qua)
