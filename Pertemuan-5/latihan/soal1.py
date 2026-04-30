stok_barang = [15, 40, 30, 10, 25]


stok_barang[3]= 50
stok_barang.append(5)
stok_barang.sort(reverse=True)
total=sum(stok_barang)

rata= total/len(stok_barang)
print('aman') if rata>20 else print("waspada")


print(stok_barang)
print(total)