print("============================")
print("Kalkulator Advance Sederhana")
print("============================")

print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")
menu = int(input("Masukkan menu yang Anda pilih: "))

if menu == 1:
	a = float(input("Masukkan bilangan yang ingin dibagi: "))
	b = float(input("Masukkan bilangan pembagi: "))
	c = a%b
	print("Sisa hasil bagi {} dibagi dengan {} adalah {}".format(a,b,c))
	
elif menu == 2:
	d = float(input("Masukkan bilangan yang ingin dibagi: "))
	e = float(input("Masukkan bilangan pembagi: "))
	f0 = d%e
	f = (d-f0)/e
	print("Hasil pembagian {} dibagi dengan {} dibulatkan ke bawah adalah {}".format(d,e,f))

elif menu == 3:
	dd = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
	print("Akar kubik dari {} adalah {}".format(dd,dd**(1/3)))
	

else:
	print("Menu yang Anda pilih tidak tersedia")
	
	

