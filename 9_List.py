
# Linear Data Struktur atau Terurut
# <namavariabel> = [<value1>, <value2> , ...]

# Penulisan List Kosong
# x=[]
# print(x)

# # 
# x = [1, 2, 3, 4, 5]
# # x[2] = "kelapa"
# # print(x)
# # print(x[0])

# # Menambahkan Item Ke List
# # x.append("manggis")
# # x.insert(2, "duren")
# # del x[3]
# x=[1,2,3,4,5,6,7,8,9,10]
# x [1]="opm"
# x[2]="ror"
# x[3]="Gjnfhhgdjkudjjydhhjijfudrkmolwesa8u67ryhtfbg5jdbmlrk,6578rb87950luy,hkmfer456wh7y8mu,kwjlv3r5"


# x.append('light yagami vs saitama')
# x.insert(2,'vermeil vs genos')
# print (x)

# Death Note 
tasks = []
while True:
    print("\nMenu:")
    print("1. Tambah Kematian")
    print("2. Hapus Kematian")
    print("3. Tampilkan Semua Daftar Kematian")
    print("4. Keluar")
    
    choice = input("Pilih opsi (1/2/3/4): ")
    
    if choice == '1':
        task = input("Masukkan Perintah: ")
        tasks.append(task)
        print("Kematian berhasil ditambahkan!")
    elif choice == '2':
        task = input("Masukkan kematian yang ingin dihapus: ")
        if task in tasks:
            tasks.remove(task)
            print("Kematian berhasil dihapus!")
        else:
            print("Daftar kematian tidak ditemukan.")
    elif choice == '3':
        if tasks:
            print("Daftar Kematian:")          
            for  i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Tidak ada nama kematian dalam daftar.")
    elif choice == '4':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# deth note
# tax=[]
# while True:
#     print("/menu:")
#     print ("1.tambah korban:")
#     print ("2.hapus korban")
#     print("3.tampilkan")
#     print("4.keluar")
#     pilihan=input('opsi 1/2/3/4:')

#     if pilihan =='1':
#         taks=input("tambahkan korban:")
#         tax.append(taks)
#         print(tax)
    # if pilihan == '2':
        # if tax in taks:
            
        # tax.remove(taks)


    
