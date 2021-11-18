ug=float(input("Masukkan nilai rata-rata UG Anda: "))
tts=float(input("Masukkan nilai TTS Anda: "))
tas=float(input("Masukkan nilai TAS Anda: "))
print("===========================")
print("Nilai Anda: ", ug*70/100+tts*15/100+tas*15/100)
nilai = ug*70/100+tts*15/100+tas*15/100

if nilai >= 85:
	nh = "A"
elif nilai >= 80:
	nh = "A-"
elif nilai >= 75:
	nh = "B+"
elif nilai >= 70:
	nh = "B"
elif nilai >= 65:
	nh = "B-"
elif nilai >= 60:
	nh = "C+"
elif nilai >= 55:
	nh = "C"
elif nilai >= 45:
	nh = "D"
else:
	nh = "E"

print("Nilai huruf Anda: "+nh)
