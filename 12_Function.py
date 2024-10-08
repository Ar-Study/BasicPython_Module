# Dasar Membuat Function
def buat() :
    print("Hellow World")

buat()
# Function dengan Parameter
def salam(parameter) :
    print(parameter)

# Project 
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("Luas segitiga: %f" % luas)
# Pemanggilan fungsi
luas_segitiga(4, 6)


# Fungsi yang mengembalikan nilai

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# pemanggilan fungsi
print ("Luas persegi: %d" % luas_persegi(6))


# Variabel Global dan Lokal

