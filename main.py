import json
import os

# Nama file untuk menyimpan data
NAMA_FILE = "data_keuangan.json"

# Inisialisasi saldo awal
saldo = 0

def muat_data():
    """Mencoba memuat saldo dari file JSON saat program dimulai"""
    global saldo
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as file:
            data = json.load(file)
            saldo = data.get("saldo", 0)
    else:
        saldo = 0

def simpan_data():
    """Menyimpan saldo saat ini ke file JSON"""
    data = {"saldo": saldo}
    with open(NAMA_FILE, "w") as file:
        json.dump(data, file)

def tambah_pemasukan():
    global saldo
    try:
        jumlah = int(input("Masukkan jumlah pemasukan: Rp "))
        if jumlah > 0:
            saldo += jumlah
            simpan_data() # Simpan otomatis setelah perubahan
            print(f"Berhasil! Pemasukan Rp {jumlah:,} ditambahkan.")
        else:
            print("Jumlah harus lebih dari 0.")
    except ValueError:
        print("Input harus berupa angka!")

def tambah_pengeluaran():
    global saldo
    try:
        jumlah = int(input("Masukkan jumlah pengeluaran: Rp "))
        
        # Cek apakah saldo cukup
        if jumlah > saldo:
            print("!!! GAGAL: Saldo tidak cukup !!!")
        elif jumlah <= 0:
            print("Jumlah pengeluaran harus lebih dari 0.")
        else:
            saldo -= jumlah
            simpan_data() # Simpan otomatis setelah perubahan
            print(f"Berhasil! Pengeluaran Rp {jumlah:,} dicatat.")
            
    except ValueError:
        print("Input harus berupa angka!")

def lihat_saldo():
    # Menampilkan saldo dengan pemisah ribuan (contoh: 10,000)
    print(f"\nSisa Saldo Anda: Rp {saldo:,}")

def menu():
    print("\n=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

# --- PROGRAM UTAMA ---

# 1. Load data dulu sebelum masuk menu
muat_data()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih! Data Anda telah tersimpan aman.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")