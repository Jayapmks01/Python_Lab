angka = [1,2,3]
angka.pop()
angka.append(12)
print(angka)

bilangan = [4,5,6]
bilangan.append(7)
bilangan.append(20)
bilangan.append(2)
bilangan.pop(1)
print(bilangan)

set = {8,9,11,7}
set.add(5)
set.add(12)
set.remove(7)
print(set.pop())
print(set)


set1={1,2,3}
set2={6,5,4}
set3={7,8,9}
set1.update(set3,set2,set1)
print(set1)

data_diri={
  'nama':'fikri',
  'umur': 20
}
data_diri['nama'] = 'fahri'
data_diri['semester'] = 'semester 8'
data_diri.pop('semester')
print(data_diri['nama'])
print(data_diri['umur'])
print(data_diri)

data_peserta = {'nama':'fahri', 'nilai':[100,90,80]}
hasil_akhir = [
  {'nama':'fikri','nilai':100},
  {'nama':'gilang','nilai':90},
  {'nama':'amin','nilai':80}
]
print(hasil_akhir[1]['nilai'])
print(data_peserta['nilai'])

buah2an = ['pepaya','mangga','pisang','durian','jambu']
buah2an[-1]
print(buah2an)

print()

hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

print()

for siswa in hasil_akhir:
  if siswa['nilai'] >= 65:
    print(siswa['nama'], end=" ")

print()

daftar_buah = ["Pepaya", "Mangga", "Pisang", "Durian", "Jambu"]
buah_terbalik = []
for a in reversed(daftar_buah):
  buah_terbalik.append(a)
print(buah_terbalik)

print()
buah_duplikasi = []
for buah in daftar_buah:
  buah_duplikasi.append(buah)
  buah_duplikasi.append(buah)
print(buah_duplikasi)

kampus = "Nurul Fikri"
print(kampus[::2].replace('i','r'))
