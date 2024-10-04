# Menghitung jumlah bilangan dari input pengguna hingga 0
total = 0
number = int(input("Masukkan bilangan (0 untuk berhenti): "))

while number != 0:
    total += number
    print("Hasilnya  : ", total)
    number = int(input("Masukkan bilangan (0 untuk berhenti): "))
  

print("Jumlah total bilangan yang dimasukkan adalah:", total)
