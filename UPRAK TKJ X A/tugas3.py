belanja = [
    {"produk":"apel","harga":5000*10},
    {"produk":"jeruk","harga":3000*5},
    {"produk":"mangga","harga":7000*7},
    {"produk":"pisang","harga":2000*20},
    {"produk":"semangka","harga":15000*1},
    ]    

total_belanjaan = 0
for item in belanja :
    total_belanjaan += item ["harga"]

print("total belanja :", total_belanjaan)