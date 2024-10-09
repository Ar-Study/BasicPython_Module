# Function untuk menyimpan suatu fungsi tertentu 
# Dasar Membuat Function
# def <namafunction>() :
# <code yang ingin dijalankan>

# 

# # Memanggil sebuah function
# buat()
# Function dengan Parameter
# def summon(parameter) :
#     print(parameter)

# summon("Rimuru Tempest")
# summon("Veldora")

# # Project 
# def luas_segitiga(alas, tinggi):
#     luas = (alas * tinggi) / 2
#     print ("Luas segitiga: %f" % luas)
# # # Pemanggilan fungsi
# luas_segitiga(4, 6)
# Fungsi yang mengembalikan nilai
# def <namafunction>():
# <codeyangdijalankan>
# return <hasil yang inginditampilkan>
def luas_persegi(sisi):
    luas = sisi * sisi
    keliling= sisi*4
    return luas

print(luas_persegi(4))
# # pemanggilan fungsi
# print ("Luas persegi: %d" % luas_persegi(6))


# Variabel Global dan Lokal

