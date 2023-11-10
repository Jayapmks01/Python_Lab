# a=8
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(8%2)

# print('---Logical Operator---')
# bil_1=11
# bil_2=20
# print(bil_1 > bil_2 and bil_1 < bil_2)


# print (not(11 > 20 and 11 < 20))

print('----identity Operator----')
x=4
y=5
print(x is not y)

print('----Membership Operator----')
penumpang_bis=['budi', 'ucup', 'joko', 'asep']
print('ucup' not in penumpang_bis)

print('----Bitwise Operator----')
var_a=10
var_b=12
print(var_a & var_b)
print(var_a | var_b)
print(var_a ^ var_b)
print(~var_a)
print(var_a << 1)
print(var_a >> 1)

print('----Bitwise Operator----')
bil_a=10
bil_b=20

if bil_a > bil_b:
    print('bilangan a lebih besar dari bilangan b')
elif bil_a > bil_b:
    print('bilangan a lebih kecil dari bilangan b')
else:
    print('hasil tidak ditemukan')


print('----Short hand Operator----')
if 20>10:print("salah")

print('---- Latihan Praktikum 4----')
print('----Soal Latihan Praktikum ----')

# Soal 1 
# Mencari nilai Ganjil dan genap menggunakan if else elif dan input nilai 
# yang nilai nya integer

# Soal 2
# Mencari nilai negatif dan positif menggunakan if else elif dan input nilai 

# Soal 3
# Games batu, gunting, kertas if else elif dan input niai


 
print('##  Program Python Menentukan Ganjil-Genap  ##')
print('=====================================================')
print()
 
bil = int(input("Masukan Bilangan :"))

if bil % 2 == 0:
    print(bil,"Merupakan Bilangan Genap")
else:
    print(bil,"Merupakan Bilangan Ganjil")

print('##  Program Python Menentukan negatif dan positif  ##')
print('=====================================================')
print()

num = int(input("Masukan angka: "))
if num>0:
    print("bilangan positif")
elif num==0:
    print(0)
else:
    print("bilangan negatif")

print('##  Program Python Menentukan batu gunting kertas  ##')
print('=====================================================')
print()

player1 = str(input("Masukan pilihan player 1: "))
player2 = str(input("Masukan pilihan player 2: "))

if (player1 == 'Batu' and player2 == 'Gunting'):
    print ("Player 1 Menang.")

elif (player1 == 'Batu' and player2 == 'Batu'):
    print ("Seri")

elif (player1 == 'Gunting' and player2 == 'Kertas'):
    print ("Player 1 Menang.")

elif (player2 == 'Gunting' and player2 == 'Gunting'):
    print ("Seri")

elif (player1 == 'Kertas' and player2 == 'Kertas'):
    print ("Seri")

elif (player1 == 'Kertas' and player2 == 'Gunting'):
    print ("Player 2 Menang")

elif (player1 == 'Batu'and player2 == 'Kertas'):
    print ("Player 2 Menang")

elif (player1 == 'Kertas' and player2 == 'Batu'):
    print ("Player 2 Menang")

elif (player1 == 'Gunting' and player2 == 'Batu'):
    print ("Player 2 Menang")
else:
    print ("Masukan inputan yang benar")

