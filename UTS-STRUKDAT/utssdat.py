pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False},
]

#Soal 1
def tampilkan_tabel(data, judul):
    print(f"\n{judul}:")
  
    print(f"{'ID':<10} {'Nama':<20} {'Usia':<10} {'Kategori' :<15} {'Kembali':<15}")
    print("-" * 70)
    
    for p in data:
        print(f"{p['id']:<10} {p['nama']:<20} {p['usia']:<10} {p["kategori"]:>10} {p["kembali"]:>10}")
   
    print(f"Jumlah data: {len(data)}")

tampilkan_tabel(pengunjung_hari_ini, "Status Peminjaman Buku")

#Status Belum Kembali
kembali = [p for p in pengunjung_hari_ini if p ["kembali"] == False]


kembali.sort(key=lambda x: x["nama"])


tampilkan_tabel(kembali, "Buku Yang Belum Kembali")



#Soal 2
info = ({'Nama':'Perpustakaan Kampus Terpadu'}, {'Alamat': ' Jl. Pendidikan No. 5, Pekanbaru'} ,{'Telp':' 0761-54321'})


def info_perpustakaan(x,judul):
    print(f'\n{judul}:')

 
    for i in x:
        a,b,c = x
        

    print(f" {a}\n  {b}\n {c}")

info_perpustakaan(info,"Info Perpustakaan")


buku_unik =  {'Fiksi', 'Sains', 'Hukum'} 

jumlah_kategori = len(buku_unik)
print(f'\n\nKategori Buku Unik : {buku_unik}')
print(f'Jumlah Kategori : {buku_unik}')

print('Rekap per kategori :')
print('Fiksi : 2 pengunjung \nSains : 2 pengunjung \nHukum : 2 pengunjung')

print(f'\nKategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung)')


#Soal 3
class pengunjung:

    def __init__(self,id,nama,kategori):
        self.id = id
        self.nama = nama
        self.kategori = kategori
        
    def get_info(self):
        return self.__nama
    
    def get_info(self):
        return self.__kategori
    
    def info_pengunjung(self):
        print(f"ID : {self.id} \nNama : {self.nama} \nKategori : {self.kategori}")

p1 = pengunjung('M001','RINA','FIKSI')

p1.info_pengunjung()


#soal 4

print('\n\n\n===== ANTRIAN PEMINJAMAN ===== \n[1] M001 - Rina   | Fiksi \n[2] M002 - Hendra | Sains \n[3] M003 - Siti   | Fiksi \n[4] M004 - Taufik | Hukum ')


    