





def registrasi_gadget(merk, tipe, harga, sn):
   
     
    if harga < 1000000 :
        print('ERROR')
        return None
    
    if len(sn)<5 :
        print('ERROR')
        return None
    
    return {'Merk': merk,
            'Tipe': tipe,
            'Harga': harga,
            'SN': sn,
            'Status': 'Tersedia'}

inventaris= []
for i in range(3):
     
    merk= input('Merk: ')
    tipe= input('Tipe: ')
    harga= input('Harga:')
    sn= input('SN: ')

    regis= registrasi_gadget
    if regis:
        inventaris.append(regis)
    
    else:
        'Gagal'

    for x in inventaris:
        print(regis)
    