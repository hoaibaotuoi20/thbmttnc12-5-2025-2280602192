# Nhập số giờ làm và mức lương theo giờ
so_gio = float(input("Nhập số giờ làm việc trong tuần: "))
luong_gio = float(input("Nhập mức lương theo giờ: "))

# Giờ chuẩn mỗi tuần
gio_chuan = 44

# Tính lương
if so_gio <= gio_chuan:
    luong = so_gio * luong_gio
else:
    gio_them = so_gio - gio_chuan
    luong = (gio_chuan * luong_gio) + (gio_them * luong_gio * 1.5)

# In ra lương thực nhận
print("Lương thực nhận trong tuần là: {:.1f}".format(luong))
