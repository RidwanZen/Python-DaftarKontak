# Program Management Kontak
# Daftar Kontak
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("================")
        print(f"Nama : {kontak['nama']}")
        print(f"Umur : {kontak['umur']}")
        print(f"Telepon : {kontak['telepon']}")

# Tambah Kontak
def new_kontak():
    nama = input("Nama : ")
    umur = input("Umur : ")
    telepon = input("Telepon : ")
    kontak = {
        "nama" : nama,
        "umur" : umur,
        "telepon" : telepon
    }
    return kontak

# Hapus Kontak
def hapus_kontak(daftar_kontak):
    #print("===Pilih data yang akan dihapus===")    
    #print("1. Nama")
    #print("2. Telepon")
    #pilih = input("Pilihan : ")
    #if pilih == "1":
    #    nama = input("Nama yang akan dihapus : ")
    #elif pilih == "2":
    #    telepon = input("Telepon yang akan dihapus : ")
    nama = input("Nama yang akan dihapus : ")
    
    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if nama == kontak["nama"]:
            index = i
            break
        
    if index == -1:
        print("Data kontak tidak ditemukan")
    else :
        del daftar_kontak[index]
        print("Data kontak berhasil dihapus")

#Cari Kontak
def cari_kontak(daftar_kontak):
    nama_cari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_cari.lower()) != -1:
            print("================")
            print(f"Nama : {kontak['nama']}")
            print(f"Umur : {kontak['umur']}")
            print(f"Telepon : {kontak['telepon']}")