# Membuat tuple awal dengan data siswa
students = (
    ("Alice", 20, 85),
    ("Bob", 22, 90),
    ("Charlie", 19, 78)
)

# Fungsi untuk menampilkan data siswa
def display_students(students):
    print("Data Siswa:")
    for i in students:
        print(f"Nama: {i[0]}, Umur: {i[1]}, Nilai: {i[2]}")

# Fungsi untuk menambahkan siswa baru
# def add_student(students, name, age, grade):
#     new_student = (name, age, grade)
#     students = students + (new_student,)
#     return students

# # Fungsi untuk menghapus siswa berdasarkan nama
# def remove_student(students, name):
#     students = tuple(student for student in students if student[0] != name)
#     return students

# # Menampilkan data siswa awal
display_students(students)
# 
# # Menambahkan siswa baru
# students = add_student(students, "David", 21, 88)
# print("\nSetelah menambahkan David:")
# display_students(students)

# # Menghapus siswa bernama Bob
# students = remove_student(students, "Bob")
# print("\nSetelah menghapus Bob:")
# display_students(students)
