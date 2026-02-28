

from kurs import curr


def idr_ke_mata_uang(jumlah_idr, kode_tujuan):
    """Konversi dari IDR ke mata uang lain."""
    if kode_tujuan in curr:
        return jumlah_idr / curr[kode_tujuan]
    else:
        raise ValueError("Kode mata uang tidak valid")


def mata_uang_ke_idr(jumlah, kode_asal):
    """Konversi dari mata uang lain ke IDR."""
    if kode_asal in curr:
        return jumlah * curr[kode_asal]
    else:
        raise ValueError("Kode mata uang tidak valid")


def konversi(jumlah, dari, ke):
    """Fungsi konversi umum."""
    if dari == "IDR" and ke != "IDR":
        return idr_ke_mata_uang(jumlah, ke)

    elif dari != "IDR" and ke == "IDR":
        return mata_uang_ke_idr(jumlah, dari)

    elif dari != "IDR" and ke != "IDR":
        # Konversi via IDR dulu
        idr = mata_uang_ke_idr(jumlah, dari)
        return idr_ke_mata_uang(idr, ke)

    else:
        return jumlah

 