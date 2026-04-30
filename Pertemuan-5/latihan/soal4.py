gudang_pc = [
 {"item": "Monitor", "harga": 1500000, "stok": 5},
 {"item": "Keyboard", "harga": 400000, "stok": 12},
 {"item": "Mouse", "harga": 250000, "stok": 20}
]
 

gudang_pc[1]['kategori']= 'Aksesoris'

print(gudang_pc[1])

gudang_pc.append({'item ': 'Headset', 'harga' :35000, 'stok' : 8})

for x in gudang_pc:
    total= x['harga']*x['stok']
    print(f'Item : {x["harga"]} | Total Aset : Rp{total}')
