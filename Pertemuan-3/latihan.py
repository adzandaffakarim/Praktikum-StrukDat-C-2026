class Sepatu:
    def __init__(self,warna, ukuran, fungsi):
        self.warna=warna
        self.ukuran=ukuran
        self.fungsi=fungsi


    def introduce_self(self):
        print(f'Sepatu warna {self.warna} dengan warna {self.warna} dan ukuran {self.ukuran}')


    def change_ukuran(self, new_ukuran):
        self.ukuran=new_ukuran
        print(f"Ukuran setekah menyusut {self.ukuran}")

shockwave=Sepatu("Hitam", 43, "Basket")
runstar=Sepatu("Putih", 42, "Jalan")
crocs=Sepatu("Hijau", 42, "Santai")
        
        
shockwave.introduce_self()
runstar.introduce_self()
crocs.introduce_self()

shockwave.change_ukuran(42)