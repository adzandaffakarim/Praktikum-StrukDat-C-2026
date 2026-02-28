
from tabulate import tabulate
from kurs import curr
from konverter import konversi


def tampilkan_tabel():
    data = []
    for kode, nilai in curr.items():
        data.append([kode, f"{nilai:,}".replace(",", ".")])

    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))


def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")


def main():
    tampilkan_tabel()

    daftar_mata_uang = ["IDR"] + list(curr.keys())

    dari = input(f"\nDari ({'/'.join(daftar_mata_uang)}): ").upper()
    ke = input(f"Ke   ({'/'.join(daftar_mata_uang)}): ").upper()
    jumlah = float(input("Jumlah: "))

    try:
        hasil = konversi(jumlah, dari, ke)

        if ke == "IDR":
            print(f"\n{jumlah} {dari} = {format_rupiah(hasil)}")
        elif dari == "IDR":
            print(f"\n{format_rupiah(jumlah)} = {hasil:.2f} {ke}")
        else:
            print(f"\n{jumlah} {dari} = {hasil:.2f} {ke}")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()