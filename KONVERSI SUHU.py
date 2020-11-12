print('====================================')
print('===========KONVERSI SUHU============')
print('====================================')

#MEMBUAT RUMUS KONVERSI SUHU

#konversi celcius ke fahrenheit
def fahrenheit(a) :
	fah = float(a * 9/5)+32
	return fah
#konversi celcius ke kelvin
def kelvin(a) :
	kel = float(273 + a)
	return kel
#konversi celcius ke reamur
def reamur(a) :
	rea = float(4/5 * a)
	return rea
#menu pilihan
stop = False
while (not stop):	
	print('====================================')
	print('====silahkan pilih menu konversi====')
	print('====================================')

	print ('1. konversi celcius ke fahrenheit')
	print ('2. konversi celcius ke kelvin')
	print ('3. konversi celcius ke reamur ')

	pilihan = input('masukan angka 1/2/3 :')
	#konversi suhu

	if pilihan == '1' : 
		print('>>>konversi celcius ke fahrenheit<<<')
		a = float(input('suhu dalam celcius :'))
		fahrenheit(a)
		print('jadi suhu sekarang :' + str(fahrenheit(a)) + 'fahrenheit')
	elif pilihan == '2' :
		print('>>>konversi celcius ke kelvin<<<')
		a = float(input('suhu dalam celcius :'))
		kelvin(a)
		print('jadi suhu sekarang :' + str(kelvin(a)) + 'kelvin')
	elif pilihan == '3' :
		print('>>>konversi celcius ke reamur<<<')
		a = float(input('suhu dalam celcius :'))
		reamur(a)
		print('jadi suhu sekarang :' + str(reamur(a)) + 'reamur')
	else:
		print('maaf menu pilihan tidak ada')
	ulang = input('apakah anda ingin mengkonversi suhu ? ya/tidak :')
	if (ulang == 'tidak'):
		stop = True
print('=====terima kasih sudah menggunnakan konversi suhu====')



		