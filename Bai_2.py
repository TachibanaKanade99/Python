# Bài 2: Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
#Ví dụ: Số cho trước là 8 thì kết quả phải là 40320
#Gợi ý: TRong trường hợp dữ liệu đầu vào được cung cấp, bạn hãy chọn cách để người dùng nhập vào.

x = int(input("Nhập số cần tính giai thừa:"))
def giaithua(x):
	if x == 0:
		return 1
	else:
		return x * giaithua(x-1)
print(giaithua(x))
