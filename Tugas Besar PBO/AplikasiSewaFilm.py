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

    def tambah_film(self, film):
        self.daftar_film.append(film)

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
        print("Daftar Film:")
        for film in self.daftar_film:
            print(f"{film.judul} ({film.tahun}) - {film.genre} - Stok: {film.stok}")

# Contoh penggunaan:
if __name__ == "__main__":
    aplikasi = AplikasiSewaFilm()

    # Menambahkan film ke dalam aplikasi
    film1 = Film("Inception", 2010, "Sci-Fi", 5)
    film2 = Film("The Shawshank Redemption", 1994, "Drama", 3)
    film3 = Film("The Godfather", 1972, "Crime", 2)

    aplikasi.tambah_film(film1)
    aplikasi.tambah_film(film2)
    aplikasi.tambah_film(film3)

    # Menampilkan daftar film
    aplikasi.tampilkan_daftar_film()

    # Meminjam dan mengembalikan film
    judul_film = "Inception"
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