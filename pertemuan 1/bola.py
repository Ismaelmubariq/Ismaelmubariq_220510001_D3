import math

# Menghitung luas permukaan bola
def hitung_luas_permukaan_bola(jari_jari):
    luas_permukaan = 4 * math.pi * jari_jari**2
    return luas_permukaan

# Menghitung volume bola
def hitung_volume_bola(jari_jari):
    volume = (4/3) * math.pi * jari_jari**3
    return volume

# Jari-jari bola (dalam cm)
jari_jari = 5

# Menghitung luas permukaan dan volume
luas_permukaan_bola = hitung_luas_permukaan_bola(jari_jari)
volume_bola = hitung_volume_bola(jari_jari)

# Menampilkan hasil
print(f"Luas permukaan bola dengan jari-jari {jari_jari} cm adalah {luas_permukaan_bola:.2f} cm^2")
print(f"Volume bola dengan jari-jari {jari_jari} cm adalah {volume_bola:.2f} cm^3")