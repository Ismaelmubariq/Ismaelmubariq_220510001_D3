# Menghitung luas alas segitiga
def hitung_luas_alas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

# Menghitung luas permukaan limas segitiga
def hitung_luas_permukaan_limas(alas, tinggi_limas):
    luas_alas = hitung_luas_alas_segitiga(alas, tinggi_limas)
    luas_permukaan_limas = luas_alas + 3 * (0.5 * alas * tinggi_limas)
    return luas_permukaan_limas

# Menghitung volume limas segitiga
def hitung_volume_limas(alas, tinggi_limas):
    luas_alas = hitung_luas_alas_segitiga(alas, tinggi_limas)
    volume = (1/3) * luas_alas * tinggi_limas
    return volume

# Dimensi limas segitiga (dalam cm)
alas_segitiga = 6
tinggi_segitiga = 8
tinggi_limas = 10

# Menghitung luas permukaan dan volume
luas_permukaan_limas = hitung_luas_permukaan_limas(alas_segitiga, tinggi_limas)
volume_limas = hitung_volume_limas(alas_segitiga, tinggi_limas)

# Menampilkan hasil
print(f"Luas permukaan limas segitiga dengan alas {alas_segitiga} cm, tinggi segitiga {tinggi_segitiga} cm, dan tinggi limas {tinggi_limas} cm adalah {luas_permukaan_limas} cm^2")
print(f"Volume limas segitiga dengan alas {alas_segitiga} cm, tinggi limas {tinggi_limas} cm adalah {volume_limas} cm^3")