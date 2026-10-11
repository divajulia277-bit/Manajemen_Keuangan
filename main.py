
# main.py
"""Program utama aplikasi Manajemen Keuangan Pribadi."""

from manajemen_keuangan.fileio import (
    tambah_transaksi_file,
    baca_semua_transaksi,
    tulis_laporan_file,
    inisialisasi_file
)
from manajemen_keuangan.processing import Transaksi, ManajerKeuangan
from manajemen_keuangan.validasi import (
    validasi_nominal,
    validasi_teks,
    NominalNegatifError
)


def menu_utama():
    """Menampilkan menu dan menjalankan aplikasi."""
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
                # Meminta dan memvalidasi nama pengeluaran.
                nama = input("Masukkan nama pengeluaran : ")
                nama_valid = validasi_teks(nama, "Nama pengeluaran")

                # Memastikan nominal berupa angka dan tidak negatif.
                nom_str = input("Masukkan nominal (Rp)     : ")
                nom_valid = validasi_nominal(nom_str)

                # Memvalidasi kategori transaksi.
                kategori = input("Masukkan kategori          : ")
                kategori_valid = validasi_teks(
                    kategori, "Kategori"
                )

                # Menentukan ID baru berdasarkan data transaksi.
                data_lama = baca_semua_transaksi()
                next_id = str(
                    max(
                        (int(d["id"]) for d in data_lama
                         if d["id"].isdigit()),
                        default=0
                    ) + 1
                )

                transaksi = Transaksi(
                    next_id,
                    nama_valid,
                    nom_valid,
                    kategori=kategori_valid
                )

                tambah_transaksi_file(transaksi.to_dict())
                print("\n[BERHASIL] Transaksi berhasil disimpan!")

            except (ValueError, TypeError, NominalNegatifError,
                    AssertionError) as error:
                print(f"\n[ERROR] Input tidak valid: {error}")

        elif pilihan == "2":
            # Membaca dan menampilkan seluruh transaksi.
            data = baca_semua_transaksi()

            if not data:
                print("\nBelum ada data transaksi.")
            else:
                print("\n--- DAFTAR TRANSAKSI ---")
                for transaksi in data:
                    print(
                        f"ID: {transaksi['id']} | "
                        f"[{transaksi['kategori']}] "
                        f"{transaksi['nama']} - "
                        f"Rp {transaksi['nominal']:,.2f}"
                    )

        elif pilihan == "3":
            # Membuat ringkasan dan menyimpannya ke file laporan.
            data = baca_semua_transaksi()

            if not data:
                print("\nTidak ada data untuk dilaporkan.")
            else:
                manajer = ManajerKeuangan(data)
                teks_laporan = manajer.buat_ringkasan(urutkan=True)

                print("\n" + teks_laporan)
                tulis_laporan_file(teks_laporan)

        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan aplikasi ini!")
            break

        else:
            print("\nPilihan tidak valid! Masukkan angka 1-4.")


if __name__ == "__main__":
    # Menjalankan aplikasi hanya jika file utama dieksekusi.
    menu_utama()
