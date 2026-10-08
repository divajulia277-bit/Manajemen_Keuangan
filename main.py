# main.py
import sys
from manajemen_keuangan.fileio import (
    tambah_transaksi_file, 
    baca_semua_transaksi, 
    tulis_laporan_file,
    inisialisasi_file
)
from manajemen_keuangan.processing import Transaksi, ManajerKeuangan
from manajemen_keuangan.validasi import validasi_nominal, validasi_teks, NominalNegatifError

def menu_utama():
    inisialisasi_file()
    while True:
        print("\n=== APLIKASI MANAJEMEN KEUANGAN PRIBADI ===")
        print("1. Tambah Transaksi Pengeluaran")
        print("2. Lihat Semua Transaksi")
        print("3. Buat & Simpan Laporan Keuangan")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == "1":
            try:
                nama = input("Masukkan nama pengeluaran : ")
                nama_valid = validasi_teks(nama, "Nama pengeluaran")
                
                nom_str = input("Masukkan nominal (Rp)     : ")
                nom_valid = validasi_nominal(nom_str)
                
                kat = input("Masukkan kategori          : ")
                kat_valid = validasi_teks(kat, "Kategori")
                
                data_lama = baca_semua_transaksi()
                next_id = str(len(data_lama) + 1)
                t = Transaksi(next_id, nama_valid, nom_valid, kategori=kat_valid)
                
                tambah_transaksi_file(t.to_dict())
                print("\n[BERHASIL] Transaksi berhasil disimpan!")
                
            except (ValueError, NominalNegatifError, AssertionError) as e:
                print(f"\n[ERROR] Input tidak valid: {e}. Baris data dilewati.")
                
        elif pilihan == "2":
            data = baca_semua_transaksi()
            if not data:
                print("\nBelum ada data transaksi.")
            else:
                print("\n--- DAFTAR TRANSAKSI ---")
                for d in data:
                    print(f"ID: {d['id']} | [{d['kategori']}] {d['nama']} - Rp {d['nominal']:,.2f}")
                    
        elif pilihan == "3":
            data = baca_semua_transaksi()
            if not data:
                print("\nTidak ada data untuk dilaporkan.")
            else:
                mk = ManajerKeuangan(data)
                teks_lap = mk.buat_ringkasan(urutkan=True)
                print("\n" + teks_lap)
                tulis_laporan_file(teks_lap)
                
        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("\nPilihan tidak valid! Silakan masukkan angka 1-4.")

if __name__ == "__main__":
    menu_utama()