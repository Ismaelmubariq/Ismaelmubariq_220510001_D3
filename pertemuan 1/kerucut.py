import math

# Menghitung luas permukaan kerucut
def hitung_luas_permukaan_kerucut(jari_jari, tinggi):
    garis_pelukis = math.sqrt(jari_jari**2 + tinggi**2)
    luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
    return luas_permukaan

# Menghitung volume kerucut
def hitung_volume_kerucut(jari_jari, tinggi):
    volume = (1/3) * math.pi * jari_jari**2 * tinggi
    return volume

# Dimensi kerucut (dalam cm)
jari_jari = 4
tinggi = 8

# Menghitung luas permukaan dan volume
luas_permukaan_kerucut = hitung_luas_permukaan_kerucut(jari_jari, tinggi)
volume_kerucut = hitung_volume_kerucut(jari_jari, tinggi)

# Menampilkan hasil
print(f"Luas permukaan kerucut dengan jari-jari {jari_jari} cm dan tinggi {tinggi} cm adalah {luas_permukaan_kerucut:.2f} cm^2")
print(f"Volume kerucut dengan jari-jari {jari_jari} cm dan tinggi {tinggi} cm adalah {volume_kerucut:.2f} cm^3")