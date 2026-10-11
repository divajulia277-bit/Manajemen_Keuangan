
# validasi.py
"""Modul untuk memvalidasi input transaksi keuangan."""


class NominalNegatifError(Exception):
    """Exception khusus ketika nominal bernilai negatif."""
    pass


def validasi_nominal(nominal):
    """Memastikan nominal berupa angka valid dan tidak negatif."""
    try:
        nilai = float(nominal)
    except (ValueError, TypeError):
        raise ValueError("Nominal harus berupa angka yang valid!")

    if nilai < 0:
        raise NominalNegatifError(
            "Nominal tidak boleh bernilai negatif!"
        )

    return nilai


def validasi_teks(teks, nama_field="Field"):
    """Memastikan teks tidak kosong menggunakan assert."""
    if not isinstance(teks, str):
        raise TypeError(f"{nama_field} harus berupa teks!")

    teks_bersih = teks.strip()

    assert teks_bersih, f"{nama_field} tidak boleh kosong!"

    return teks_bersih


if __name__ == "__main__":
    # Pengujian lokal modul validasi.
    assert validasi_nominal(25000) == 25000.0
    assert validasi_teks("  Makan  ") == "Makan"

    try:
        validasi_nominal(-5000)
    except NominalNegatifError as error:
        print(f"Validasi berhasil: {error}")

    print("Pengujian validasi selesai.")
