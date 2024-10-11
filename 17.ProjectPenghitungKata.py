# Program Penghitung Kata

def hitung_kata(teks):
    # Memisahkan teks berdasarkan spasi dan menghitung jumlah elemen dalam daftar
    kata_list = teks.split()
    return len(kata_list)

def main():
    teks = input("Masukkan teks: ")
    jumlah_kata = hitung_kata(teks)
    print(f"Jumlah kata dalam teks adalah: {jumlah_kata}")

main()
# if __name__ == "__main__":
#     main()
