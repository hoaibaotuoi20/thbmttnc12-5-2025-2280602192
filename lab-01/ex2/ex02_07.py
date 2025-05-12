print("Nhập các dòng văn bản (nhấn Enter để kết thúc nhập):")

danh_sach_dong = []

while True:
    dong = input()
    if dong == "":  # Khi người dùng nhấn Enter mà không nhập gì
        break
    danh_sach_dong.append(dong.upper())  # Chuyển đổi chữ thường thành chữ hoa

print("\nCác dòng sau khi chuyển thành chữ hoa:")
for dong in danh_sach_dong:
    print(dong)
