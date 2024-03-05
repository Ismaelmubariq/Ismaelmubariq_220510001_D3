import sqlite3

class Film:
    def __init__(self, judul, tahun, genre, stok):
        self.judul = judul
        self.tahun = tahun
        self.genre = genre
        self.stok = stok
        self.dipinjam = 0

    def dipinjamkan(self):
        if self.stok > 0:
            self.stok -= 1
            self.dipinjam += 1
            return True
        else:
            return False

    def dikembalikan(self):
        if self.dipinjam > 0:
            self.stok += 1
            self.dipinjam -= 1
            return True
        else:
            return False

class AplikasiSewaFilm:
    def __init__(self):
        self.daftar_film = []
        self.conn = sqlite3.connect('sewa_film.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS film (
                            judul TEXT,
                            tahun INTEGER,
                            genre TEXT,
                            stok INTEGER,
                            dipinjam INTEGER
                            )''')
        self.conn.commit()

    def tambah_film(self, film):
        self.daftar_film.append(film)
        self.cursor.execute("INSERT INTO film VALUES (?, ?, ?, ?, ?)",
                            (film.judul, film.tahun, film.genre, film.stok, film.dipinjam))
        self.conn.commit()

    def pinjam_film(self, judul):
        for film in self.daftar_film:
            if film.judul == judul:
                return film.dipinjamkan()
        return False

    def kembalikan_film(self, judul):
        for film in self.daftar_film:
            if film.judul == judul:
                return film.dikembalikan()
        return False

    def tampilkan_daftar_film(self):
        self.cursor.execute("SELECT * FROM film")
        daftar_film = self.cursor.fetchall()
        print("Daftar Film:")
        for film in daftar_film:
            print(f"{film[0]} ({film[1]}) - {film[2]} - Stok: {film[3]}")

# Contoh penggunaan:
if __name__ == "__main__":
    aplikasi = AplikasiSewaFilm()

    # Menampilkan daftar film
    aplikasi.tampilkan_daftar_film()

    # Meminjam dan mengembalikan film
    judul_film = input("Masukkan judul film yang ingin dipinjam: ")
    if aplikasi.pinjam_film(judul_film):
        print(f"Film {judul_film} berhasil dipinjam.")
    else:
        print(f"Maaf, film {judul_film} tidak tersedia.")

    aplikasi.tampilkan_daftar_film()

    if aplikasi.kembalikan_film(judul_film):
        print(f"Film {judul_film} berhasil dikembalikan.")
    else:
        print(f"Tidak ada film {judul_film} yang sedang dipinjam.")

    aplikasi.tampilkan_daftar_film()