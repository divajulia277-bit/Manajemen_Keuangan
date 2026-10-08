# fileio.py
import os

def inisialisasi_file(nama_file="pengeluaran.txt"):
    """Membuat file baru menggunakan mode 'x'."""
    try:
        with open(nama_file, "x") as f:
            f.write("id;nama;nominal;kategori\n")
        print(f"File '{nama_file}' berhasil dibuat untuk pertama kali.")
    except FileExistsError:
        pass

def tambah_transaksi_file(transaksi, nama_file="pengeluaran.txt"):
    """Menambahkan baris data transaksi baru menggunakan mode 'a'."""
    inisialisasi_file(nama_file)
    with open(nama_file, "a") as f:
        f.write(f"{transaksi['id']};{transaksi['nama']};{transaksi['nominal']};{transaksi['kategori']}\n")

def baca_semua_transaksi(nama_file="pengeluaran.txt"):
    """Membaca data transaksi dari file menggunakan mode 'r'."""
    data = []
    try:
        with open(nama_file, "r") as f:
            header = next(f, None)  # Lewati header
            for baris in f:
                if baris.strip():
                    parts = baris.strip().split(";")
                    if len(parts) == 4:
                        data.append({
                            "id": parts[0],
                            "nama": parts[1],
                            "nominal": float(parts[2]),
                            "kategori": parts[3]
                        })
    except FileNotFoundError:
        print(f"Peringatan: File '{nama_file}' tidak ditemukan!")
        return []
    return data

def tulis_laporan_file(teks_laporan, nama_file="laporan_keuangan.txt"):
    """Menulis ringkasan laporan keuangan menggunakan mode 'w'."""
    with open(nama_file, "w") as f:
        f.write(teks_laporan)
    print(f"Laporan berhasil ditulis ke '{nama_file}'.")