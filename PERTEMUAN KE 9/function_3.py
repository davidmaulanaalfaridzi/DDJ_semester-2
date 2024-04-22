def berangkat_sekolah(pakaian, buku):
    if pakaian == "seragam" and buku == "bawa":
        print("Berangkat sekolah")
    else:
        print("pergi main")

def nama_siswa(nama):
    print(nama)

print(nama_siswa("Raihan"), berangkat_sekolah("seragam", "bawa"))
print(nama_siswa("Murti"), berangkat_sekolah("Jeans", "tidak membawa buku"))
print(nama_siswa("Adi"),berangkat_sekolah("seragam", "tidak membawa buku"))