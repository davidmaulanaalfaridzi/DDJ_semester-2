import tkinter as tk

def tambah_ke_keranjang():
    item = entry_nama.get()
    harga = entry_harga.get()
    listbox_keranjang.insert(tk.END, f"{item} - Rp{harga}")

def hapus_dari_keranjang():
    index = listbox_keranjang.curselection()
    if index:
        listbox_keranjang.delete(index)

# Buat jendela
root = tk.Tk()
root.title("Toko Sepatu RRD")

# Buat label dan input field
label_nama = tk.Label(root, text="NAMA SEPATU:")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

label_harga = tk.Label(root, text="HARGA:")
label_harga.grid(row=1, column=0)
entry_harga = tk.Entry(root)
entry_harga.grid(row=1, column=1)

# Tombol untuk menambahkan ke keranjang
button_tambah = tk.Button(root, text="Tambah ke Keranjang", command=tambah_ke_keranjang)
button_tambah.grid(row=2, column=0, columnspan=2, sticky="we")

# Listbox untuk menampilkan keranjang
listbox_keranjang = tk.Listbox(root)
listbox_keranjang.grid(row=3, column=0, columnspan=2, sticky="nsew")

# Tombol untuk menghapus dari keranjang
button_hapus = tk.Button(root, text="Hapus dari Keranjang", command=hapus_dari_keranjang)
button_hapus.grid(row=4, column=0, columnspan=2, sticky="we")

root.mainloop()
