# Nhập chuỗi các số nhị phân phân cách bởi dấu phẩy
chuoi_nhi_phan = input("Nhập chuỗi các số nhị phân 4 chữ số, phân cách bằng dấu phẩy: ")

# Tách chuỗi nhập vào thành danh sách các số nhị phân
danh_sach_nhi_phan = chuoi_nhi_phan.split(',')

# Danh sách để lưu các số nhị phân chia hết cho 5
so_chia_het_cho_5 = []

# Kiểm tra từng số nhị phân
for so in danh_sach_nhi_phan:
    # Chuyển số nhị phân thành số thập phân
    so_thap_phan = int(so, 2)
    
    # Kiểm tra xem số thập phân có chia hết cho 5 không
    if so_thap_phan % 5 == 0:
        so_chia_het_cho_5.append(so)

# In kết quả các số nhị phân thỏa mãn điều kiện, phân tách bằng dấu phẩy
print("SO chia het 5 : ",",".join(so_chia_het_cho_5))
