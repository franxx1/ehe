print('==================================')
print('===SELAMAT DATANG DI TAKOYAKI DESUU====')
print('==================================')

print('Hari ini kita ada promo ni kaka')
print(' 1. Untuk Varian 1 beli 10 pcs diskon 10%')
print('2. Untuk varian 2  beli 8 pcs diskom 8%')
print (' *promo terbatas ya untuk varian 1 hanya untuk 4 pembeli pertama, untuk varian 2 hanya untuk 5 pembeli pertama* ')

def menu():
    print ('1. varian 1 >>> Rp.2000/pcs')
    print ('2. Varian 2 >>> Rp.2500/pcs')
    
diskon = lambda total : 10/100 *total

stop = False
while(not stop):
    print('Silahkan pilih varian')
    menu()

    pilihan = int(input('Masukan menu pilihan anda :'))
    porsi = int(input('Masukan jumlah pcs yang anda inginkan:'))
    if pilihan == 1:
        total1 = porsi * 2000
        print(total1)
        if porsi == 10 :
            print('selamat anda mendapatkan diskon')
            var1 = diskon(total1)
            total1 = (porsi * 2000) - (var1)
        elif porsi !=10:
            print('anda tidak mendapatkan diskon')
            print('jadi total yang harus anda bayar :' + str(total1))
            print('silahakan melakukan pembayaran')
            nominal = int(input('masukan nominal pembayaran :'))
            bayar = nominal - total1
            if bayar == 0 :
                print('Anda telah membayar, silahkan menunggu orderan anda')
            elif bayar > 0 :
                print('sisa uang anda : ' + str(bayar))
                print('Anda telah membayar, silahkan menunggu orderan anda')
        else :
            print('uang anda pas')

    elif pilihan == 2 :
        total2 = porsi * 2500
        print(total2)
        if porsi == 8 :
            print('selamat anda mendapatkan diskon')
            var2 = diskon(total2)
            total2 = (porsi * 2500) - (var2)
        elif porsi != 8:
            print('anda tidak mendapatkan diskon')
            print('jadi total yang harus anda bayar  :' + str(total2))
            print('silahakan melakukan pembayaran')
            nominal = int(input('masukan nominal pembayaran :'))
            bayar = nominal - total2
            if bayar == 0 :
                print('Anda telah membayar, silahkan menunggu orderan anda')
            elif bayar > 0 :
                print('sisa uang anda : ' + str(bayar))
                print('Anda telah membayar, silahkan menunggu orderan anda')
        else :
            print('uang anda pas')
    ulang = input('Apakah kaka mau oreder takoyaki lagi ? ya/tidak :')
    if (ulang == 'tidak'):
        stop = True
print('====Terima ksaih sudah order kakak====')
print('====Jangan lupa senyum hari ini ======')    
