Berikut adalah langkah-langkah untuk menjalankan program yang telah diberikan:

cara menjalankan code 
"python app.py"

1. **Pastikan Anda memiliki Python terpasang di komputer Anda.**
   Jika belum terpasang, unduh dan pasang Python dari [python.org](https://www.python.org/).

2. **Buka visual studio**
   Anda bisa menggunakan editor teks seperti Notepad, VSCode, PyCharm, atau editor lainnya sesuai preferensi Anda.

3. **Salin kode yang diberikan ke dalam editor teks Anda.**

4. **Simpan file dengan ekstensi `.py`.**
   Contoh: `validasi_pendaftaran.py`

5. **Buka terminal atau command prompt.**
   - Di Windows: Tekan `Win + R`, ketik `cmd`, lalu tekan `Enter`.
   - Di MacOS: Buka aplikasi Terminal.
   - Di Linux: Buka aplikasi Terminal.

6. **Navigasi ke direktori tempat Anda menyimpan file `validasi_pendaftaran.py`.**
   Gunakan perintah `cd` untuk berpindah direktori.
   ```bash
   cd path\to\your\directory
   ```

7. **Jalankan program Python.**
   Ketik perintah berikut di terminal atau command prompt:
   ```bash
   python validasi_pendaftaran.py
   ```

8. **Lihat hasilnya.**
   Output dari program akan ditampilkan di terminal atau command prompt, menunjukkan apakah setiap kasus uji lulus atau gagal.

Berikut adalah kode lengkap yang bisa Anda salin dan jalankan:

```python
import re

def validasi_pendaftaran(nama, email, password):
    if not nama:
        return False, "Nama wajib diisi"
    if not re.match("^[a-zA-Z ]+$", nama):
        return False, "Nama hanya boleh berisi huruf alfabet dan spasi"
    if not email or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return False, "Format email salah"
    if len(password) < 8:
        return False, "Password minimal 8 karakter"
    if tidak re.search("[a-z]", password):
        return False, "Password harus mengandung setidaknya satu huruf kecil"
    if tidak re.search("[A-Z]", password):
        return False, "Password harus mengandung setidaknya satu huruf besar"
    if tidak re.search("[0-9]", password):
        return False, "Password harus mengandung setidaknya satu angka"
    if tidak re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password harus mengandung setidaknya satu simbol"

    return True, "Input valid"

# Contoh penggunaan dan pengujian
data_uji = [
    {"nama": "", "email": "johndoe.com", "password": "pass123", "hasil_diharapkan": "Nama wajib diisi"},
    {"nama": "John Doe", "email": "johndoe.com", "password": "pass123", "hasil_diharapkan": "Format email salah"},
    {"nama": "John Doe", "email": "john.doe@example.com", "password": "pass123", "hasil_diharapkan": "Password minimal 8 karakter"},
    {"nama": "John Doe", "email": "john.doe@example.com", "password": "Password", "hasil_diharapkan": "Password harus mengandung setidaknya satu angka"},
    {"nama": "John Doe", "email": "john.doe@example.com", "password": "Pass1234", "hasil_diharapkan": "Password harus mengandung setidaknya satu simbol"},
    {"nama": "John Doe", "email": "john.doe@example.com", "password": "S4mpl3P@ssw0rd", "hasil_diharapkan": "Input valid"},
    {"nama": "John123", "email": "john.doe@example.com", "password": "S4mpl3P@ssw0rd", "hasil_diharapkan": "Nama hanya boleh berisi huruf alfabet dan spasi"},
]

for i, data in enumerate(data_uji):
    is_valid, message = validasi_pendaftaran(data["nama"], data["email"], data["password"])
    if (is_valid and message == data["hasil_diharapkan"]) atau (tidak is_valid dan message == data["hasil_diharapkan"]):
        print(f"Kasus Uji {i+1}: Lulus")
    else:
        print(f"Kasus Uji {i+1}: Gagal - Diharapkan: '{data['hasil_diharapkan']}', Diterima: '{message}'")
```

Setelah mengikuti langkah-langkah di atas, Anda akan melihat hasil pengujian validasi pendaftaran di terminal atau command prompt.