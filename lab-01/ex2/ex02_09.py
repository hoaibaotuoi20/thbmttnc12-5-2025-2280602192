import math

# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False  # Số nhỏ hơn hoặc bằng 1 không phải là số nguyên tố
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # Nếu n chia hết cho i thì n không phải là số nguyên tố
    return True  # Nếu không chia hết cho bất kỳ số nào thì n là số nguyên tố

# Nhập số từ người dùng
so = int(input("Nhập một số để kiểm tra: "))

# Kiểm tra và in kết quả
if kiem_tra_so_nguyen_to(so):
    print(f"{so} là số nguyên tố.")
else:
    print(f"{so} không phải là số nguyên tố.")
