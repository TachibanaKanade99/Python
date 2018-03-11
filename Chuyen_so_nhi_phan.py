n = int((input("Nhập số n:")))
sodu = n % 2
ketqua = ""
while n > 0:
	if sodu == 0:
		ketqua = "0" + ketqua
	elif sodu == 1:	
		ketqua = "1" + ketqua
	n = n // 2
	sodu = n % 2 
print("Số nhị phân là:",str(ketqua))

