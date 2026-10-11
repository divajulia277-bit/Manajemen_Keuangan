
# testing.py
import unittest

from manajemen_keuangan.processing import ManajerKeuangan
from manajemen_keuangan.validasi import (
    validasi_nominal,
    NominalNegatifError,
    validasi_teks
)


class TestManajemenKeuangan(unittest.TestCase):
    """Menguji fungsi perhitungan dan validasi keuangan."""

    def setUp(self):
        # Menyiapkan data transaksi untuk setiap pengujian.
        self.data_test = [
            {
                "id": "1",
                "nama": "Makan",
                "nominal": 20000.0,
                "kategori": "Makanan"
            },
            {
                "id": "2",
                "nama": "Bensin",
                "nominal": 50000.0,
                "kategori": "Transport"
            },
            {
                "id": "3",
                "nama": "Snack",
                "nominal": 10000.0,
                "kategori": "Makanan"
            }
        ]
        self.manajer = ManajerKeuangan(self.data_test)

    def test_hitung_total(self):
        """Memastikan total transaksi dihitung dengan benar."""
        self.assertEqual(self.manajer.hitung_total(), 80000.0)

    def test_hitung_rata_rata(self):
        """Memastikan rata-rata transaksi benar."""
        self.assertAlmostEqual(
            self.manajer.hitung_rata_rata(),
            26666.67,
            places=2
        )

    def test_urutkan_terbesar(self):
        """Memastikan transaksi diurutkan dari terbesar."""
        hasil = self.manajer.urutkan_terbesar()
        self.assertEqual(hasil[0]["nama"], "Bensin")
        self.assertEqual(hasil[-1]["nama"], "Snack")

    def test_validasi_nominal_negatif(self):
        """Memastikan nominal negatif ditolak."""
        with self.assertRaises(NominalNegatifError):
            validasi_nominal(-5000)

    def test_validasi_teks_kosong(self):
        """Memastikan teks kosong ditolak."""
        with self.assertRaises(AssertionError):
            validasi_teks("   ", "Nama Transaksi")

    def test_validasi_nominal_positif(self):
        """Memastikan nominal positif diterima."""
        hasil = validasi_nominal(25000)
        self.assertEqual(hasil, 25000)

    def test_data_transaksi_kosong(self):
        """Memastikan total transaksi kosong adalah nol."""
        manajer_kosong = ManajerKeuangan([])
        self.assertEqual(manajer_kosong.hitung_total(), 0)

    def test_hitung_rata_rata_kosong(self):
        """Memastikan rata-rata data kosong tidak menyebabkan error."""
        manajer_kosong = ManajerKeuangan([])
        self.assertEqual(manajer_kosong.hitung_rata_rata(), 0)


if __name__ == "__main__":
    # Menjalankan seluruh pengujian saat modul dipanggil langsung.
    unittest.main()
