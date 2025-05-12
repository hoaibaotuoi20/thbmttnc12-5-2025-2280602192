# Hàm đảo ngược chuỗi
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]  # Cắt chuỗi từ cuối đến đầu

# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhập một chuỗi để đảo ngược: ")

# Đảo ngược chuỗi và in ra
chuoi_dao_nguoc = dao_nguoc_chuoi(chuoi_nhap)
print(f"Chuỗi sau khi đảo ngược là: {chuoi_dao_nguoc}")
