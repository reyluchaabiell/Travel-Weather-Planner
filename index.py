# =========================
# INPUT DATA DARI USER
# =========================

# Ambil jarak perjalanan dari user (diubah jadi angka desimal)
distance_mi = float(input("Masukkan jarak (mil): "))

# Cek apakah sedang hujan
# .strip() → hapus spasi
# .lower() → ubah ke huruf kecil
# == "yes" → hasilnya True atau False
is_raining = input("Apakah sedang hujan? (yes/no): ").strip().lower() == "yes"

# Cek apakah user punya sepeda
has_bike = input("Apakah punya sepeda? (yes/no): ").strip().lower() == "yes"

# Cek apakah user punya mobil
has_car = input("Apakah punya mobil? (yes/no): ").strip().lower() == "yes"

# Cek apakah user punya aplikasi ride (ojek online)
has_ride_share_app = input("Apakah punya aplikasi ride? (yes/no): ").strip().lower() == "yes"


# =========================
# VARIABEL HASIL
# =========================

# Default: anggap tidak bisa pergi
can_travel = False

# Untuk menyimpan cara pergi (jalan kaki, sepeda, mobil, dll)
transport_mode = ""

# Untuk menyimpan alasan kalau tidak bisa pergi
reason = ""


# =========================
# LOGIKA UTAMA
# =========================

# Kalau jarak tidak valid (0 atau negatif)
if distance_mi <= 0:
    can_travel = False
    reason = "Jarak tidak valid."


# Kalau sedang hujan
elif is_raining:
    # Kalau punya mobil → bisa pergi
    if has_car:
        can_travel = True
        transport_mode = "mobil"
    
    # Kalau tidak punya mobil tapi punya ride share → bisa
    elif has_ride_share_app:
        can_travel = True
        transport_mode = "ride share"
    
    # Kalau tidak punya keduanya → tidak bisa
    else:
        can_travel = False
        reason = "Sedang hujan dan tidak ada transportasi tertutup."


# Kalau tidak hujan
else:
    # Jarak sangat dekat → jalan kaki
    if distance_mi <= 1:
        can_travel = True
        transport_mode = "jalan kaki"
    
    # Jarak menengah
    elif distance_mi <= 6:
        # Prioritas: sepeda
        if has_bike:
            can_travel = True
            transport_mode = "sepeda"
        
        # Kalau tidak ada sepeda, coba mobil
        elif has_car:
            can_travel = True
            transport_mode = "mobil"
        
        # Kalau tidak ada mobil, coba ride share
        elif has_ride_share_app:
            can_travel = True
            transport_mode = "ride share"
        
        # Kalau tidak ada semua → tidak bisa
        else:
            can_travel = False
            reason = "Jarak menengah, tapi tidak ada kendaraan yang tersedia."
    
    # Jarak jauh (> 6 mil)
    else:
        # Harus pakai mobil atau ride share
        if has_car:
            can_travel = True
            transport_mode = "mobil"
        
        elif has_ride_share_app:
            can_travel = True
            transport_mode = "ride share"
        
        else:
            can_travel = False
            reason = "Jarak jauh, tapi tidak ada mobil atau ride share."


# =========================
# OUTPUT KE USER
# =========================

# Kalau bisa pergi
if can_travel:
    print("Perjalanan bisa dilakukan ✅")
    print(f"Saran transportasi: {transport_mode}")

# Kalau tidak bisa
else:
    print("Perjalanan tidak bisa dilakukan ❌")
    print(f"Alasan: {reason}")