a = float(input("masukkan angka pertama: "))
b = float(input("maukkan angka kedua: "))
c = float(input("masukkan angka ketiga: "))

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c 
else:
    largest = print("Tidak ada angka terbesar")

print("Angka terbesar adalah:", largest)