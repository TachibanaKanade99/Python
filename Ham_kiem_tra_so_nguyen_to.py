def ktsnt(k):
	if k <2:
		return 0
	elif k == 2:
		return 1
	else:
		for i in range(2, k):
			if k%i == 0:
				return 0 
			else:
				return 1
k = int(input("Nhập vào k:"))
if ktsnt(k) == 1:
	print(k,"là số nguyên tố")
else:
	print(k,"không phải là số nguyên tố")