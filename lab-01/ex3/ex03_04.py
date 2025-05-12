# Nhập tuple từ bàn phím dưới dạng chuỗi, cách nhau bằng dấu phẩy
dau_vao = input("Nhập các phần tử của tuple, phân cách bằng dấu phẩy: ")

# Chuyển thành danh sách, sau đó chuyển sang tuple
tuple_nguoi_dung = tuple(dau_vao.split(','))

# Kiểm tra nếu tuple không rỗng
if len(tuple_nguoi_dung) > 0:
    print("Phần tử đầu tiên:", tuple_nguoi_dung[0])
    print("Phần tử cuối cùng:", tuple_nguoi_dung[-1])
else:
    print("Tuple rỗng, không có phần tử để truy cập.")
