from prettytable import PrettyTable
import mysql.connector

koneksi = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gudang"
)

active = True

while active:
    gudang = koneksi.cursor()

    gudang.execute('select*from barang')

    data = gudang.fetchall()
    t = PrettyTable(['kode_brg', 'nama_brg', 'harga_brg', 'stok'])

    for row in data:
        t.add_row(row)
    print(t)

    print("Pilih Aksi : ")
    print("1. Tambah Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Exit")
    inputuser = input("\nPilihan : ")

    if inputuser == '1':
        kode_brg = input("Masukkan kode Barang : ")
        nama_brg = input("Masukkan nama barang : ")
        harga_brg = input("Masukkan harga barang: ")
        stok = input("Masukkan stok : ")
        koneksiTest = koneksi.cursor()

        koneksiTest.execute(
            "insert into barang (kode_brg, nama_brg, harga_brg, stok) VALUES (%s, %s, %s, %s)", (kode_brg, nama_brg, harga_brg, stok))

        koneksi.commit()

        print("Data Berhasil Ditambahkan")
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) :")
        if cek == 'No':
            active = False2
            
    if inputuser == '4':
        active = False
