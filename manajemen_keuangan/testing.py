# testing.py
import unittest
from manajemen_keuangan.processing import ManajerKeuangan
from manajemen_keuangan.validasi import validasi_nominal, NominalNegatifError, validasi_teks

class TestManajemenKeuangan(unittest.TestCase):
    def setUp(self):
        self.data_test = [
            {"id": "1", "nama": "Makan", "nominal": 20000.0, "kategori": "Makanan"},
            {"id": "2", "nama": "Bensin", "nominal": 50000.0, "kategori": "Transport"},
            {"id": "3", "nama": "Snack", "nominal": 10000.0, "kategori": "Makanan"}
        ]
        self.manajer = ManajerKeuangan(self.data_test)

    def test_hitung_total(self):
        self.assertEqual(self.manajer.hitung_total(), 80000.0)

    def test_hitung_rata_rata(self):
        self.assertAlmostEqual(self.manajer.hitung_rata_rata(), 26666.67, places=2)

    def test_urutkan_terbesar(self):
        hasil = self.manajer.urutkan_terbesar()
        self.assertEqual(hasil[0]["nama"], "Bensin")
        self.assertEqual(hasil[-1]["nama"], "Snack")

    def test_validasi_nominal_negatif(self):
        with self.assertRaises(NominalNegatifError):
            validasi_nominal(-5000)

    def test_validasi_teks_kosong(self):
        with self.assertRaises(AssertionError):
            validasi_teks("   ", "Nama Transaksi")

if __name__ == "__main__":
    unittest.main()