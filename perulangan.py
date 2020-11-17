#materi: perulangan
stop = False
while(not stop) :

    n = int(input('masukan nilai n :'))
    x = 0
    while (x < n) :
        if (10** x > n) :
            break
        else:
            x += 1
    print ('nilai terkecil dari 10^x>n adalah', 10**x)
    ulang = input('Apakah Kamu ingin mengulang lagi ? ya/tidak :')
    if (ulang == 'tidak'):
        stop = True
print('=== Terima kasih ===')
     