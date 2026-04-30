data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

d1, d2, d3, d4 = data_aktivitas

for x in data_aktivitas:
    nama, poin = x

    if poin>80:
        print(f'{nama} mendapatkan predikat Gold')
    elif 50>=poin<=80:
        print(f'{nama} medapatkan predikat Silver')
    else:
        print(f'{nama} mendapatkan predikat Bronze')








