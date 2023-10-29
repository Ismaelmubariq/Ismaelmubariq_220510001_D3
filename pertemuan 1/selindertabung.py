import math

# Menghitung luas permukaan silinder/tabung
def hitung_luas_permukaan_silinder(jari_jari, tinggi):
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return luas_permukaan

# Menghitung volume silinder/tabung
def hitung_volume_silinder(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    return volume

# Dimensi silinder/tabung (dalam cm)
jari_jari = 5
tinggi = 10

# Menghitung luas permukaan dan volume
luas_permukaan_silinder = hitung_luas_permukaan_silinder(jari_jari, tinggi)
volume_silinder = hitung_volume_silinder(jari_jari, tinggi)

# Menampilkan hasil
print(f"Luas permukaan silinder/tabung dengan jari-jari {jari_jari} cm dan tinggi {tinggi} cm adalah {luas_permukaan_silinder:.2f} cm^2")
print(f"Volume silinder/tabung dengan jari-jari {jari_jari} cm dan tinggi {tinggi} cm adalah {volume_silinder:.2f} cm^3")