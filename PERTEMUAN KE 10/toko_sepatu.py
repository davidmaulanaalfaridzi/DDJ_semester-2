import tkinter as tk

class KasirApp:
    def __init__(self, master):
        self.master = master
        master.title("TOKO SEPATU")

        # Variabel untuk menyimpan daftar belanja
        self.shopping_cart = []

        # Daftar barang (nama, harga)
        self.items = [
            ("NIKE", 100000),
            ("ADIDAS", 150000),
            ("PUMA", 200000),
            ("NEW BALANCE", 250000),
            ("VANS", 300000),
            ("CONVERSE", 350000),
            ("REEBOK", 50000),
            ("SKETCHERS.", 60000),
        ]

        # Membuat label
        self.label = tk.Label(master, text="SELAMAT DATANG DI TOKO SEPATU")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


        # Label dan entry untuk harga barang
        self.price_label = tk.Label(master, text="JUMLAH BARANG:")
        self.price_label.grid(row=6, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=6, column=1, padx=10, pady=5)

        # Membuat label
        self.label = tk.Label(master, text="PILIH BARANG")
        self.label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Daftar belanja
        self.shopping_listbox = tk.Listbox(master)
        self.shopping_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Tombol untuk checkout
        self.checkout_button = tk.Button(master, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

         # Membuat label
        self.label = tk.Label(master, text="KELOMPOK RIFKI,RAPI,DAVID")
        self.label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)


        

        # Menampilkan daftar barang
        self.show_items()

    def show_items(self):
        # Menampilkan daftar barang
        for item in self.items:
            item_info = f"{item[0]} - Rp{item[1]}"
            self.shopping_listbox.insert(tk.END, item_info)

    def add_to_cart(self):
        # Mendapatkan informasi barang dari input pengguna
        item = self.item_entry.get()
        price = float(self.price_entry.get())

        # Menambahkan barang ke keranjang belanja
        self.shopping_cart.append((item, price))

        # Menampilkan barang yang ditambahkan ke daftar belanja
        self.shopping_listbox.insert(tk.END, f"{item} - Rp{price}")

        # Mengosongkan input
        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def checkout(self):
        total_price = sum(price for _, price in self.shopping_cart)
        tk.messagebox.showinfo("Checkout", f"Total harga yang harus dibayar: Rp{total_price}")
        self.shopping_cart = []
        self.shopping_listbox.delete(0, tk.END)

# Fungsi utama
def main():
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
