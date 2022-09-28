print("Nhap gia tri a: ")
a = int(input())
print("Nhap gia tri b: ")
b = int(input())
print("Nhap gia tri c: ")
c = int(input())

delta = b*b-4*a*c
print('delta =',delta)

if a == 0:
	print('khong phai phuong trinh bac 2, hay nhap a#0')
elif a!=0 and delta < 0:
	print('phuong trinh vo nghiem')
elif a!=0 and delta == 0:
	print('phuong trinh co nghiem kep: ',-b/(2*a))
elif a!=0 and delta > 0:
	x1 = (-b + sqrt(delta))/(2*a)
	x2 = (-b - sqrt(delta))/(2*a)
	print('phuong trinh co 2 nghiem phan biet: ' + '\nx1 = ' + str(x1) + '\nx2 = ' + str(x2))
