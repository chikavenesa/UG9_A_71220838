import math
panjang = int(input('Masukkan panjang: '))
lebar = int(input('Masukkan lebar: '))
jari = int(input('Masukkan jari-jari: '))
luassetengah = float((3.14*(jari**2)/2))
luasper = float(panjang*lebar)
cat = float(((luassetengah+luasper)/15))
print("Area tersebut membutuhkan",math.ceil(cat),"Kaleng cat")