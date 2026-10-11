
# processing.py
"""Modul untuk mengolah dan menganalisis transaksi keuangan."""


class Transaksi:
    """Merepresentasikan satu transaksi keuangan."""

    def __init__(self, id_transaksi, nama, nominal, **kwargs):
        if not nama or not nama.strip():
            raise ValueError("Nama transaksi tidak boleh kosong.")

        if not isinstance(nominal, (int, float)) or isinstance(nominal, bool):
            raise ValueError("Nominal harus berupa angka.")

        if nominal < 0:
            raise ValueError("Nominal tidak boleh negatif.")

        self.id = id_transaksi
        self.nama = nama.strip()
        self.nominal = nominal
        self.kategori = kwargs.get("kategori", "Umum")
        self.catatan = kwargs.get("catatan", "")

    def to_dict(self):
        """Mengubah objek transaksi menjadi dictionary."""
        return {
            "id": self.id,
            "nama": self.nama,
            "nominal": self.nominal,
            "kategori": self.kategori
        }


class ManajerKeuangan:
    """Mengolah dan menganalisis kumpulan transaksi."""

    def __init__(self, daftar_transaksi):
        self.daftar = daftar_transaksi

    def hitung_total(self, *args):
        """Menghitung total transaksi atau angka yang diberikan."""
        if args:
            return sum(args)

        return sum(
            map(lambda transaksi: transaksi["nominal"], self.daftar)
        )

    def hitung_rata_rata(self):
        """Menghitung rata-rata nominal transaksi."""
        if not self.daftar:
            return 0.0

        return self.hitung_total() / len(self.daftar)

    def urutkan_terbesar(self):
        """Mengurutkan transaksi berdasarkan nominal terbesar."""
        return sorted(
            self.daftar,
            key=lambda transaksi: transaksi["nominal"],
            reverse=True
        )

    def filter_kategori(self, kategori_target):
        """Memilih transaksi berdasarkan kategori."""
        return list(
            filter(
                lambda transaksi:
                    transaksi["kategori"].lower()
                    == kategori_target.lower(),
                self.daftar
            )
        )

    def buat_ringkasan(self, urutkan=True):
        """Membuat laporan keuangan dalam bentuk teks."""
        total = self.hitung_total()
        rata_rata = self.hitung_rata_rata()

        # Tentukan urutan transaksi sesuai argumen pengguna.
        data_proses = (
            self.urutkan_terbesar() if urutkan else self.daftar
        )

        garis = "=" * 40
        laporan = [
            garis,
            "    LAPORAN MANAJEMEN KEUANGAN",
            garis,
            f"Total Transaksi   : {len(self.daftar)}",
            f"Total Pengeluaran : Rp {total:,.2f}",
            f"Rata-rata/Item    : Rp {rata_rata:,.2f}",
            "",
            "--- Rincian Transaksi ---"
        ]

        # Tambahkan setiap transaksi ke laporan.
        for transaksi in data_proses:
            laporan.append(
                f"[{transaksi['kategori']}] "
                f"{transaksi['nama']} - "
                f"Rp {transaksi['nominal']:,.2f}"
            )

        laporan.append(garis)
        return "\n".join(laporan)


if __name__ == "__main__":
    # Pengujian lokal ketika modul dijalankan secara langsung.
    data_dummy = [
        {
            "id": "1",
            "nama": "Makan Siang",
            "nominal": 25000.0,
            "kategori": "Makanan"
        },
        {
            "id": "2",
            "nama": "Beli Buku",
            "nominal": 75000.0,
            "kategori": "Pendidikan"
        }
    ]

    manajer = ManajerKeuangan(data_dummy)
    print(manajer.buat_ringkasan(urutkan=True))
