def hitung_persegi():
    try:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        if sisi <= 0:
            print("Panjang sisi tidak valid")
        else:
            luas = sisi ** 2
            keliling = 4 * sisi
            print(f"Luas persegi adalah {luas}")
            print(f"Keliling persegi adalah {keliling}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka")

# Memanggil fungsi
hitung_persegi()
