
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
    if not re.search("[a-z]", password):
        return False, "Password harus mengandung setidaknya satu huruf kecil"
    if not re.search("[A-Z]", password):
        return False, "Password harus mengandung setidaknya satu huruf besar"
    if not re.search("[0-9]", password):
        return False, "Password harus mengandung setidaknya satu angka"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password harus mengandung setidaknya satu simbol"

    return True, "Input valid"

# penggunaan dan pengujian 

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
    if (is_valid and message == data["hasil_diharapkan"]) or (not is_valid and message == data["hasil_diharapkan"]):
        print(f"Kasus Uji {i+1}: Lulus")
    else:
        print(f"Kasus Uji {i+1}: Gagal - Diharapkan: '{data['hasil_diharapkan']}', Diterima: '{message}'")

# Kasus uji dengan nama dan password yang salah
# Nama tidak sesuai kriteria
result, message = validasi_pendaftaran("Risal", "email_risal@gmai.com", "Rahasiaa1.")
if result:
    print("Registrasi berhasil!")
else:
    print("Registrasi gagal:", message)
