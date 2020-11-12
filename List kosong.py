print('Deskripsi Buku')
print('='*50)
Buku = []

Judul_buku = input('masukan judul buku :')
Jumlah_halaman = float(input('masukan jumlah halaman :'))
Tahun_rilis = int(input(' masukan tahun rilis :'))
Nama_penulis = input('Masukan nama penulis :')
Nama_penerbit = input('Masukan nama penerbit :')
Warna_cover = input ('Masukan warna cover :')

print('='*50)

#proses input
Buku.append(Judul_buku)
Buku.append(Jumlah_halaman) 
Buku.append(Tahun_rilis)
Buku.append(Nama_penulis)
Buku.append(Nama_penerbit)
Buku.append(Warna_cover)

print(Buku)
print('='*50)
 