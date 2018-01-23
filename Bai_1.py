# Some example for use range Python
my_list = ['one','two','three','four','five']
my_list_len = len(my_list)
for i in range(0,my_list_len):
	print(my_list[i])

# Bài 1:Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5 nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi trên một dòng,cách nhau bằng dấu phẩy.
# Sử dụng range(begin,end)

j = []
for i in range(2000,3201):
	if (i%7==0) and (i%5!=0):
		j.append(str(i))
print(','.join(j))


