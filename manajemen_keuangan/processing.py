# processing.py

class Transaksi:
    """Class untuk merepresentasikan objek Transaksi tunggal."""
    def __init__(self, id_transaksi, nama, nominal, **kwargs):
        self.id = id_transaksi
        self.nama = nama
        self.nominal = nominal
        self.kategori = kwargs.get("kategori", "Umum")
        self.catatan = kwargs.get("catatan", "")

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "nominal": self.nominal,
            "kategori": self.kategori
        }

class ManajerKeuangan:
    """Class untuk mengolah dan menganalisis kumpulan data transaksi."""
    def __init__(self, daftar_transaksi):
        self.daftar = daftar_transaksi

    def hitung_total(self, *args):
        """Menghitung total nominal menggunakan *args."""
        if args:
            return sum(args)
        return sum(map(lambda x: x["nominal"], self.daftar))

    def hitung_rata_rata(self):
        if not self.daftar:
            return 0.0
        return self.hitung_total() / len(self.daftar)

    def urutkan_terbesar(self):
        """Mengurutkan transaksi dari nominal terbesar memakai lambda."""
        return sorted(self.daftar, key=lambda x: x["nominal"], reverse=True)

    def filter_kategori(self, kategori_target):
        """Filter data berdasarkan kategori memakai filter & lambda."""
        return list(filter(lambda x: x["kategori"].lower() == kategori_target.lower(), self.daftar))

    def buat_ringkasan(self, urutkan=True):
        """Membuat teks ringkasan laporan menggunakan keyword argument."""
        total = self.hitung_total()
        rata = self.hitung_rata_rata()
        data_proses = self.urutkan_terbesar() if urutkan else self.daftar

        garis = "=" * 40
        laporan = [garis, "    LAPORAN MANAJEMEN KEUANGAN", garis]
        laporan.append(f"Total Transaksi   : {len(self.daftar)}")
        laporan.append(f"Total Pengeluaran : Rp {total:,.2f}")
        laporan.append(f"Rata-rata/Item    : Rp {rata:,.2f}\n")
        laporan.append("--- Rincian Transaksi (Terbesar) ---")
        
        for item in data_proses:
            laporan.append(f"[{item['kategori']}] {item['nama']} - Rp {item['nominal']:,.2f}")
        laporan.append(garis)
        
        return "\n".join(laporan)

if __name__ == '__main__':
    # Testing lokal fungsi modul processing
    d_dummy = [
        {"id": "1", "nama": "Makan Siang", "nominal": 25000.0, "kategori": "Makanan"},
        {"id": "2", "nama": "Beli Buku", "nominal": 75000.0, "kategori": "Pendidikan"}
    ]
    mk = ManajerKeuangan(d_dummy)
    print(mk.buat_ringkasan(urutkan=True))