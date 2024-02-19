data_pejualan = [
    {"produk":"baju", "jumlah": 20},
    {"produk" :"baju", "jumlah": 20},
    {"produk" :"baju", "jumlah": 20},

]
total_penjualan = 0
for item in data_pejualan:
    total_penjualan += item["jumlah"]
print("total penjualan : ",total_penjualan)