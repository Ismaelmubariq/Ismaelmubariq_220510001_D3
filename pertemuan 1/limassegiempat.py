# Menghitung luas permukaan limas segiempat
def hitung_luas_limas_segiempat(panjang_alas, lebar_alas, tinggi_limas):
    luas_alas = panjang_alas * lebar_alas
    luas_tutup = 0.5 * (panjang_alas * lebar_alas)
    luas_permukaan_limas = luas_alas + 4 * luas_tutup
    return luas_permukaan_limas

# Menghitung volume limas segiempat
def hitung_volume_limas_segiempat(panjang_alas, lebar_alas, tinggi_limas):
    volume = (1/3)  * panjang_alas * tinggi_limas 
    return volume

# Dimensi limas segiempat (dalam cm)
panjang_alas = 6
lebar_alas = 8
tinggi_limas = 10

# Menghitung luas dan volume
luas_permukaan_limas = hitung_luas_limas_segiempat(panjang_alas, lebar_alas, tinggi_limas)
volume_limas = hitung_volume_limas_segiempat(panjang_alas, lebar_alas, tinggi_limas)

# Menampilkan hasil
print(f"Luas permukaan limas segiempat dengan panjang alas {panjang_alas} cm, lebar alas {lebar_alas} cm, dan tinggi {tinggi_limas} cm adalah {luas_permukaan_limas} cm^2")
print(f"Volume limas segiempat dengan panjang alas {panjang_alas} cm, lebar alas {lebar_alas} cm, dan tinggi {tinggi_limas} cm adalah {volume_limas} cm^3")
