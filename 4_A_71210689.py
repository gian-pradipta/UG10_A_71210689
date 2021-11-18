ar = input("Masukkan artikel yang ingin dipindai: ")
klub = input("Masukkan nama klub favorit Anda: ")
skor = input("Masukkan skor yang ingin dicari: ")
if skor in ar and klub in ar:
	print("Hasil pencarian ditemukan")
elif skor in ar:
	print("Hanya skor {} yang ditemukan pada artikel ini".format(skor))
elif klub in ar:
	print("Hanya kata {} yang ditemukan pada artikel ini".format(klub))
else:
	print("Hasil pencarian {} dan {} tidak ditemukan".format(klub,skor))