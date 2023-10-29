# Menghitung luas alas segitiga
def hitung_luas_alas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

# Menghitung luas permukaan prisma segitiga
def hitung_luas_permukaan_prisma(alas, tinggi, tinggi_prisma):
    luas_alas = hitung_luas_alas_segitiga(alas, tinggi)
    luas_segitiga = 3 * luas_alas
    luas_permukaan_prisma = 2 * luas_alas + luas_segitiga * tinggi_prisma
    return luas_permukaan_prisma

# Menghitung volume prisma segitiga
def hitung_volume_prisma(alas, tinggi, tinggi_prisma):
    luas_alas = hitung_luas_alas_segitiga(alas, tinggi)
    volume = luas_alas * tinggi_prisma
    return volume

# Dimensi prisma segitiga (dalam cm)
alas_segitiga = 6
tinggi_segitiga = 8
tinggi_prisma = 10

# Menghitung luas permukaan dan volume
luas_permukaan_prisma = hitung_luas_permukaan_prisma(alas_segitiga, tinggi_segitiga, tinggi_prisma)
volume_prisma = hitung_volume_prisma(alas_segitiga, tinggi_segitiga, tinggi_prisma)

# Menampilkan hasil
print(f"Luas permukaan prisma segitiga dengan alas {alas_segitiga} cm, tinggi {tinggi_segitiga} cm, dan tinggi prisma {tinggi_prisma} cm adalah {luas_permukaan_prisma} cm^2")
print(f"Volume prisma segitiga dengan alas {alas_segitiga} cm, tinggi {tinggi_segitiga} cm, dan tinggi prisma {tinggi_prisma} cm adalah {volume_prisma} cm^3")