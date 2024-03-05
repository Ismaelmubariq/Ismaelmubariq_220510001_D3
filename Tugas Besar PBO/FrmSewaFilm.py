import tkinter as tk
from tkinter import ttk

class AplikasiSewaFilmForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Sewa Film")

        self.label_judul = ttk.Label(self, text="Judul Film:")
        self.label_judul.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_judul = ttk.Entry(self)
        self.entry_judul.grid(row=0, column=1, padx=5, pady=5)

        self.label_tahun = ttk.Label(self, text="Tahun Rilis:")
        self.label_tahun.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_tahun = ttk.Entry(self)
        self.entry_tahun.grid(row=1, column=1, padx=5, pady=5)

        self.label_genre = ttk.Label(self, text="Genre:")
        self.label_genre.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_genre = ttk.Entry(self)
        self.entry_genre.grid(row=2, column=1, padx=5, pady=5)

        self.label_stok = ttk.Label(self, text="Stok:")
        self.label_stok.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_stok = ttk.Entry(self)
        self.entry_stok.grid(row=3, column=1, padx=5, pady=5)

        self.button_submit = ttk.Button(self, text="Tambah Film", command=self.submit_form)
        self.button_submit.grid(row=4, columnspan=2, padx=5, pady=5)

    def submit_form(self):
        judul = self.entry_judul.get()
        tahun = self.entry_tahun.get()
        genre = self.entry_genre.get()
        stok = self.entry_stok.get()

        # Lakukan sesuatu dengan data yang dimasukkan, misalnya menyimpan ke database

        # Setelah data diproses, kosongkan input field
        self.entry_judul.delete(0, tk.END)
        self.entry_tahun.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_stok.delete(0, tk.END)

if __name__ == "__main__":
    app = AplikasiSewaFilmForm()
    app.mainloop()