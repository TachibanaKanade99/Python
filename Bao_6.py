''' Bài 6: In ra m số nguyên tố đầu tiên
Input: Nhập vào số nguyên m
Process: 
- Viết hàm kiểm tra tính nguyên tố của nguyên tố k
	+ Nếu k < 2:không phải số nguyên tố 
	+ Lặp biến i từ 2 đến căn bậc hai của k, nếu k chia hết cho i thì k không phải là số nguyên tố:
- In ra các số nguyên tố:
	+ Gán biến dem = 0 ; k = 0
	+ Lặp: trong khi dem < m thì nếu k là số nguyên tố in k, tăng dem++, tăng k++
'''

def kiem_tra_so_nguyen_to(k):
		if k < 2:
			return 0
		elif k == 2:
			return 1
		else:
			for i in range(2, k):
				if k % i == 0:
					return 0
				else:
					return 1
m = int(input("Nhập vào m:"))
dem = k = 0
while dem < m:
	if kiem_tra_so_nguyen_to(k) == 1:
		print(k)
		dem = dem +1
	k = k+1
