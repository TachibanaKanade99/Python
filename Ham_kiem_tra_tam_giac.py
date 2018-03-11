def tamgiac(a,b,c):
	if ((a==0) or (b==0) or (c==0)):
		return 0
	elif ((a+b>c) and (b+c>a) and (a+c>b)):
		return 1
	else:
		print("Không phải là tam giác")
a = float(input("Nhập vào số a:"))
b = float(input("Nhập vào số b:"))
c = float(input("Nhập vào số c:"))
if tamgiac(a,b,c) == 1:
	print("Là tam giác")
	P = a + b + c
	print("Chu vi của tam giác là:",P)


