# Hàm tính tổng các số chẵn trong danh sách
def tong_so_chan(danh_sach):
    tong = 0
    for so in danh_sach:
        if so % 2 == 0:
            tong += so
    return tong

# Nhập danh sách số từ người dùng (cách 1: nhập dưới dạng chuỗi và tách)
dau_vao = input("Nhập các số, phân cách bằng dấu phẩy: ")
danh_sach_so = [int(x) for x in dau_vao.split(',')]

# Tính và in kết quả
tong_chan = tong_so_chan(danh_sach_so)
print("Tổng các số chẵn trong danh sách là:", tong_chan)
