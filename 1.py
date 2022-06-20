HimaTI = [
    {
        "nama": "Pande Priatama",
        "nim": "42130090",
        "jurusan": "Teknologi Informasi"
    },
    {
        "nama": "Bagus Maulidan",
        "nim": "421313249",
        "jurusan": "Teknologi Informasi"
    },
    {
        "nama": "Adi Saputra",
        "nim": "42130086",
        "jurusan": "Teknologi Informasi"
    }

]
print("Pilih Nama HimaTi Berikut : ")
print("1. Pande Priatama")
print("2. Bagus Maulidan")
print("3. Adi Saputra")

input = input("\nMasukkan Angka 1-3 :")

if input == '1':
    print("Nama = ", HimaTI[0]['nama'])
    print("Nim = ", HimaTI[0]['nim'])
    print("Jurusan = ", HimaTI[0]['jurusan'])
elif input == '2':
    print("Nama = ", HimaTI[1]['nama'])
    print("Nim = ", HimaTI[1]['nim'])
    print("Jurusan = ", HimaTI[1]['jurusan'])
else:
    print("Nama = ", HimaTI[2]['nama'])
    print("Nim = ", HimaTI[2]['nim'])
    print("Jurusan = ", HimaTI[2]['jurusan'])
