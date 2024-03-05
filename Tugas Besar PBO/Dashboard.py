import tkinter as tk
from tkinter import ttk

class AplikasiSewaFilmDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Dashboard Aplikasi Sewa Film")

        self.label = tk.Label(master, text="Selamat datang di Aplikasi Sewa Film")
        self.label.pack()

        self.tombol_tampilkan = tk.Button(master, text="Tampilkan Daftar Film", command=self.tampilkan_daftar_film)
        self.tombol_tampilkan.pack()

        self.tombol_pinjam = tk.Button(master, text="Pinjam Film", command=self.pinjam_film)
        self.tombol_pinjam.pack()

        self.tombol_kembalikan = tk.Button(master, text="Kembalikan Film", command=self.kembalikan_film)
        self.tombol_kembalikan.pack()

        self.tombol_keluar = tk.Button(master, text="Keluar", command=master.quit)
        self.tombol_keluar.pack()

    def tampilkan_daftar_film(self):
        # Implementasi fungsi tampilkan_daftar_film
        pass

    def pinjam_film(self):
        # Implementasi fungsi pinjam_film
        pass

    def kembalikan_film(self):
        # Implementasi fungsi kembalikan_film
        pass

root = tk.Tk()
app = AplikasiSewaFilmDashboard(root)
root.mainloop()