#Bai 3:Viết phương trình bậc 2 nhập vào hệ số a,b,c và cho ra nghiệm x của phương trình:
#VD: input: a=1,b=-2,c=1 ; output:x=1
import math as ma

a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
c = int(input("Nhập số c:"))

if a == 0:
	if b == 0:
		print("Phương trình vô nghiệm")
	else:
		x = -c/b
		print("Nghiệm của phương trình là:",x)
else:
	D = b**2 - 4*a*c
	if D < 0:
		print("Phương trình vô nghiệm")
	else:
		if D == 0:
			x = -b/(2*a)
			print("Phương trình có nghiệm kép:",float(x))
		else:
			print("Phương trình có 2 nghiệm phân biệt")
			x1 = (-b + ma.sqrt(D))/2*a
			print("Nghiệm thứ nhất của phương trình là:",float(x1))
			x2 = -(-b + ma.sqrt(D))/2*a
			print("Nghiệm thứ 2 của phương trình là:",float(x2))