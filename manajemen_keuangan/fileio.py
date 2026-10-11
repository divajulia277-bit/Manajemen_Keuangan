
# fileio.py
from pathlib import Path

# Nama file default untuk menyimpan transaksi.
FILE_DEFAULT = "pengeluaran.txt"


def inisialisasi_file(nama_file=FILE_DEFAULT):
    """Membuat file transaksi baru tanpa menimpa file lama."""
    try:
        with open(nama_file, "x", encoding="utf-8") as file:
            file.write("id;nama;nominal;kategori\n")
        print(f"File '{nama_file}' berhasil dibuat.")
        return True

    except FileExistsError:
        # File sudah ada, jadi isi lama tetap dipertahankan.
        return False


def tambah_transaksi_file(transaksi, nama_file=FILE_DEFAULT):
    """Menambahkan satu transaksi ke akhir file."""
    inisialisasi_file(nama_file)

    # Memastikan data transaksi memiliki atribut yang diperlukan.
    kolom_wajib = ("id", "nama", "nominal", "kategori")

    for kolom in kolom_wajib:
        if kolom not in transaksi:
            raise ValueError(f"Atribut transaksi '{kolom}' tidak tersedia.")

    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(
            f"{transaksi['id']};{transaksi['nama']};"
            f"{transaksi['nominal']};{transaksi['kategori']}\n"
        )


def baca_semua_transaksi(nama_file=FILE_DEFAULT):
    """Membaca transaksi valid dan melewati baris yang rusak."""
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            # Baris pertama berisi nama kolom.
            next(file, None)

            for nomor_baris, baris in enumerate(file, start=2):
                if not baris.strip():
                    continue

                try:
                    bagian = baris.strip().split(";")

                    if len(bagian) != 4:
                        raise ValueError("Jumlah kolom harus 4.")

                    id_transaksi, nama, nominal_teks, kategori = bagian

                    if not all(
                        nilai.strip()
                        for nilai in (
                            id_transaksi, nama, nominal_teks, kategori
                        )
                    ):
                        raise ValueError("Ada kolom yang kosong.")

                    nominal = float(nominal_teks)

                    if nominal < 0:
                        raise ValueError("Nominal tidak boleh negatif.")

                    data.append({
                        "id": id_transaksi.strip(),
                        "nama": nama.strip(),
                        "nominal": nominal,
                        "kategori": kategori.strip()
                    })

                except ValueError as error:
                    # Baris bermasalah dilewati; pembacaan berlanjut.
                    print(
                        f"Peringatan baris {nomor_baris} dilewati: "
                        f"{error}"
                    )

    except FileNotFoundError:
        print(
            f"Peringatan: File '{nama_file}' tidak ditemukan. "
            "Silakan tambahkan transaksi terlebih dahulu."
        )

    return data


def tulis_laporan_file(
    teks_laporan,
    nama_file="laporan_keuangan.txt"
):
    """Menulis laporan baru dan menggantikan isi laporan lama."""
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(teks_laporan)

    print(f"Laporan berhasil ditulis ke '{nama_file}'.")


if __name__ == "__main__":
    # Pengujian lokal untuk memeriksa fungsi pembacaan file.
    hasil = baca_semua_transaksi()
    assert isinstance(hasil, list), "Hasil pembacaan harus berupa list."
    print(f"Jumlah transaksi valid: {len(hasil)}")
