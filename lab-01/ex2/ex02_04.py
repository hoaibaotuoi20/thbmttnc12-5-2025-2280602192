# Tạo danh sách chứa các số thỏa điều kiện
ket_qua = []

for so in range(2000, 3201):  # bao gồm 3200
    if so % 7 == 0 and so % 5 != 0:
        ket_qua.append(str(so))  # chuyển sang chuỗi để in dễ dàng

# In ra kết quả, ngăn cách bằng dấu phẩy
print(",".join(ket_qua))
