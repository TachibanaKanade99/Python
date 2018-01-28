n = int(input("Nhập số:"))
if n == 1:
	print("1 không phải là số nguyên tố")
else:
	if n == 2:
		print(n,"là số nguyên tố")
	else:
		for i in range(2, n):
			if (n % i == 0):
				print(n,"không phải là số nguyên tố")
				break
			else:
				print(n,"là số nguyên tố")
				break