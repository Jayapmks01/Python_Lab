# print()
# print('=== 1. Program Perhitungan Jarak Tempuh ===')
# print()

nama_kendaraan = input ('masukan nama kendaraan ? ')
jenis_bensin = input ('masukan jenis bensin ? ').lower()
kota = input ('masukan kota ? ').lower()

if jenis_bensin == 'pertalite':
    harga = 10000
    jarak_tempuh = 12
elif jenis_bensin == 'pertamax':
    harga = 14000
    jarak_tempuh = 13 
elif jenis_bensin == 'pertamax turbo':
    harga = 17000
    jarak_tempuh = 13.5
else :
    print('salah masukan bahan bakar')


if kota == 'jakarta':
    jarak = 20
elif kota == 'bekasi':
    jarak = 35.7
elif kota == 'depok':
    jarak = 5
elif kota == 'tangerang':
    jarak = 99
elif kota == 'bogor':
    jarak = 120.6
else :
    print('salah masukan kota')

pemakaian_bensin = jarak / jarak_tempuh
total_harga = pemakaian_bensin * harga

print('nama kendaraan ',nama_kendaraan)
print('jenis bensin ', jenis_bensin)
print('kota yang dituju ',kota)
print('pemakaian bensin ', "{:.2f}".format(pemakaian_bensin), 'liter')
print('total harga bensin Rp.', "{:,.2f}".format(total_harga), 'rupiah')



print()
print('=== 2. Program Pemesanan Menu Makanan dan Minuman ===')
print()

nama = input('Masukan Nama Kamu: ')
nomer = input('Masukan nomer HP pemesan: ')
menu = int(input('Masukan angka pilihan menu (1 = Makanan dan 2 = Minuman): '))
match menu:
    case 1:
        print()
        print ("""Kamu memilih menu makanan, Silahkan pilih salah satu makanan dibawah ini:
        1. Nasi Goreng, Harga Rp. 15.000.-
        2. Mie Goreng, Harga Rp. 12.000.-
        3. Ayam Geprek, Harga RP. 18.000.-
        """)
        
        makanan = int(input('Masukan nomer pilihan pesan makanan (1, 2, dan 3): '))
        harga = int(input('Masukan harga menu: '))
        uang = int(input('Masukan uang pembayaran kamu: '))
        jumlah_pesanan = int(input('Masukan jumlah pesanan kamu: '))
        print()
        if makanan == 1:
            pembayaran = (harga * jumlah_pesanan)
            kembalian = (uang - pembayaran)
            print('Pesanan atas nama',nama,'dengan nomer HP',nomer,'Memilih Menu 1 yaitu nasi goreng dengan total harga', pembayaran)
            print('Uang kembalian kamu adalah', kembalian)
        elif makanan == 2:
            pembayaran = (harga * jumlah_pesanan)
            kembalian = (uang - pembayaran)
            print('Pesanan atas nama',nama,'dengan nomer HP',nomer,'Memilih Menu 2 yaitu mie goreng dengan total harga', pembayaran)
            print('Uang kembalian kamu adalah', kembalian)
        elif makanan == 3:
            pembayaran = (harga * jumlah_pesanan)
            kembalian = (uang - pembayaran)
            print('Pesanan atas nama',nama,'dengan nomer HP',nomer,'Memilih Menu 3 yaitu ayam Geprek dengan total harga', pembayaran)
            print('Uang kembalian kamu adalah', kembalian)
        else:
            print('Masukan pilihan menu dengan benar')

    case 2:
        print()
        print ("""Kamu memilih menu minuman, Silahkan pilih salah satu minuman dibawah ini:
        1. Aneka Jus, Harga Rp. 15.000.-
        2. Soft Drink, Harga Rp. 10.000.-
        3. Sweet Ice Tea, Harga RP. 5.000.-
        """)
        
        minuman = int(input('Masukan nomer pilihan pesan minuman (1, 2, dan 3): '))
        harga = int(input('Masukan harga menu: '))
        uang = int(input('Masukan uang pembayaran kamu: '))
        jumlah_pesanan=int(input('Masukan jumlah pesanan kamu: '))
        print()
        if minuman == 1:
            pembayaran = (harga * jumlah_pesanan)
            kembalian = (uang - pembayaran)
            print('Pesanan atas nama',nama,'dengan nomer HP',nomer,'Memilih Menu 1 yaitu aneka jus dengan total harga', pembayaran)
            print('Uang kembalian kamu adalah', kembalian)
        elif minuman == 2:
            pembayaran = (harga * jumlah_pesanan)
            kembalian = (uang - pembayaran)
            print('Pesanan atas nama',nama,'dengan nomer HP',nomer,'Memilih Menu 2 yaitu soft drink dengan total harga', pembayaran)
            print('Uang kembalian kamu adalah', kembalian)
        elif minuman == 3:
            pembayaran = (harga * jumlah_pesanan)
            kembalian = (uang - pembayaran)
            print('Pesanan atas nama',nama,'dengan nomer HP',nomer,'Memilih Menu 3 yaitu sweet ice tea dengan total harga', pembayaran)
            print('Uang kembalian kamu adalah', kembalian)
        
        else:
            print('Masukan pilihan menu dengan benar')

    case _:
        print('Pilihan menu yang kamu masukan belum benar!')
        

print()
print('=== 3. Program Bilangan Ganjil "STT Nurul Fikri" ===')
print()

bilangan = [i for i in range(1, 21)]
i = 0
while i < len(bilangan):
    if bilangan[i] % 3 == 0:
        print("STT Terpadu Nurul Fikri")
    else:
        print(bilangan[i])
    i += 1


