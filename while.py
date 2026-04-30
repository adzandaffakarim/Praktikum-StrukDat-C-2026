#1
# List menu (nama menu dan harga)
menu = [
    ["Nasi Goreng", 15000],
    ["Mie Goreng", 14000],
    ["Ayam Goreng", 18000],
    ["Es Teh", 5000],
    ["Es Jeruk", 7000]
]

print("=== MENU WARUNG BAROKAH ===")

# menampilkan menu
for i in range(len(menu)):
    print(i+1, ".", menu[i][0], "- Rp", menu[i][1])

# input pilihan
pilihan = int(input("Pilih nomor menu: "))

# validasi input
if pilihan >= 1 and pilihan <= len(menu):
    nama = menu[pilihan-1][0]
    harga = menu[pilihan-1][1]
    print("Anda memilih:", nama)
    print("Harga:", harga)
else:
    print("Nomor menu tidak valid")









#2
menu = [
    ["Nasi Goreng", 15000],
    ["Mie Goreng", 14000],
    ["Ayam Goreng", 18000],
    ["Es Teh", 5000],
    ["Es Jeruk", 7000]
]

pesanan = []

print("=== MENU ===")
for i in range(len(menu)):
    print(i+1, ".", menu[i][0], "-", menu[i][1])

while True:
    pilih = int(input("Pilih menu (0 untuk selesai): "))

    if pilih == 0:
        break

    if pilih >= 1 and pilih <= len(menu):
        jumlah = int(input("Jumlah porsi: "))
        pesanan.append([menu[pilih-1][0], menu[pilih-1][1], jumlah])
    else:
        print("Menu tidak valid")

total = 0

print("\n=== DAFTAR PESANAN ===")
for item in pesanan:
    nama = item[0]
    harga = item[1]
    jumlah = item[2]
    subtotal = harga * jumlah
    total += subtotal

    print(nama, "x", jumlah, "=", subtotal)

print("Total Belanja:", total)






#3
total = int(input("Masukkan total belanja: "))

while True:
    bayar = int(input("Masukkan uang pembayaran: "))

    if bayar < total:
        print("Uang tidak cukup, masukkan lagi")
    else:
        break

kembalian = bayar - total

print("\n=== STRUK ===")
print("Total Belanja:", total)
print("Uang Dibayar:", bayar)

if kembalian == 0:
    print("Uang pas, tidak ada kembalian")
else:
    print("Kembalian Anda:", kembalian)









#4
hari = int(input("Jumlah hari: "))
menu = int(input("Jumlah menu: "))

data = []

# input data
for i in range(hari):
    baris = []
    print("Hari ke-", i+1)

    for j in range(menu):
        jumlah = int(input("Menu ke-" + str(j+1) + ": "))
        baris.append(jumlah)

    data.append(baris)

print("\n=== DATA PENJUALAN ===")
for row in data:
    print(row)

# total per hari
print("\nTotal per hari")
for i in range(hari):
    print("Hari", i+1, "=", sum(data[i]))

# total per menu
print("\nTotal per menu")
for j in range(menu):
    total = 0
    for i in range(hari):
        total += data[i][j]

    print("Menu", j+1, "=", total)














#5
class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan(self):
        print(self.nama, "- Rp", self.harga)


class Transaksi:
    def __init__(self):
        self.total = 0

    def tambah(self, menu, jumlah):
        self.total += menu.harga * jumlah

    def struk(self):
        print("Total Belanja:", self.total)


# membuat objek menu
m1 = Menu("Nasi Goreng", 15000)
m2 = Menu("Mie Goreng", 14000)
m3 = Menu("Es Teh", 5000)

daftar_menu = [m1, m2, m3]

print("=== MENU ===")
for i in range(len(daftar_menu)):
    print(i+1, end=". ")
    daftar_menu[i].tampilkan()

transaksi = Transaksi()

pilih = int(input("Pilih menu: "))
jumlah = int(input("Jumlah: "))

menu_dipilih = daftar_menu[pilih-1]

transaksi.tambah(menu_dipilih, jumlah)

print("\n=== STRUK ===")
transaksi.struk()