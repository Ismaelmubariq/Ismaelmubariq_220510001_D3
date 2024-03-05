import tkinter as tk
from tkinter import messagebox

class AplikasiSewaFilmLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Aplikasi Sewa Film")

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.grid(row=2, columnspan=2, padx=5, pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Misalnya, kita akan menggunakan username "admin" dan password "1234" sebagai contoh login
        if username == "admin" and password == "1234":
            messagebox.showinfo("Login Berhasil", "Selamat datang, Admin!")
            # Di sini Anda bisa melanjutkan ke aplikasi utama setelah login berhasil
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah. Silakan coba lagi.")

if __name__ == "__main__":
    app = AplikasiSewaFilmLogin()
    app.mainloop()