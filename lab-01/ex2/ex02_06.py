# Nhập giá trị X và Y
X = int(input("Nhập số hàng (X): "))
Y = int(input("Nhập số cột (Y): "))

# Tạo mảng 2 chiều
mang_2_chieu = []

for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    mang_2_chieu.append(hang)

# In ra mảng kết quả
print("Mảng 2 chiều là:")
print(mang_2_chieu)
