# validasi.py

class NominalNegatifError(Exception):
    """Exception khusus saat nominal bernilai negatif."""
    pass

def validasi_nominal(nominal):
    """Memeriksa apakah nominal valid dan tidak negatif."""
    try:
        val = float(nominal)
    except ValueError:
        raise ValueError("Nominal harus berupa angka valid!")
    
    if val < 0:
        raise NominalNegatifError("Nominal tidak boleh bernilai negatif!")
    
    return val

def validasi_teks(teks, nama_field="Field"):
    """Memastikan teks tidak kosong menggunakan assert."""
    teks_clean = teks.strip()
    assert len(teks_clean) > 0, f"{nama_field} tidak boleh kosong!"
    return teks_clean