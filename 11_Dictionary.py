# Dictonary
# nama_dict = {
#     "key": "value"
# }

# Cara membuat dictionary
# Cara 1
# namavariabel = {"Key ": "Value"}
pak_tani = {
    "nama": "Coding First",
    "umur": 22,
    "hobi": ["coding", "membaca", "cocok tanam"],
    "menikah": False,
    "sosmed": {
        "instagram": "codingfirst"
    }
}

# print(pak_tani)

# # Cara 2
# warna_buah = dict(jeruk="orange", apel="merah", pisang="kuning")

# # Cara memanggil dictionary
# # Cara 1
# print(pak_tani["nama"])
# # Cara 2
# print(pak_tani.get("nama"))

# Memberikan nilai item dictionary
pak_tani["nama"] = "CF"                             
print(pak_tani)


# Menghapus nilai item pada dictionary
del pak_tani["nama", ""]
print(pak_tani)

pak_tani.pop("umur")
print(pak_tani)

# Menambahkan item pada Dictionary
pak_tani.update({"name": "CodingF"})
# Mengambil Panjang 
print(len(pak_tani))