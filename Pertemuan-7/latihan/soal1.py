plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

listPlat = plat[0].split(" ")
angkaAkhir = int (listPlat[1])
for i in plat:
    listPlat = i.split(" ")
    angkaAkhir = int(listPlat[1])
    if angkaAkhir % 2==0:
        print (f'{i} adalah plat genap')
    else:
        print (f'{i} adalah plat ganjil')
