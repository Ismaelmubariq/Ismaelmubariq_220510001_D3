# Menghitung luas balok
def hitung_luas_balok(panjang, lebar, tinggi):
    luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return luas

# Menghitung volume balok
def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

# Dimensi balok (dalam cm)
panjang = 10
lebar = 15
tinggi = 5

# Menghitung luas dan volume
luas_balok = hitung_luas_balok(panjang, lebar, tinggi)
volume_balok = hitung_volume_balok(panjang, lebar, tinggi)

# Menampilkan hasil
print(f"Luas balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {luas_balok} cm^2")
print(f"Volume balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {volume_balok} cm^3")