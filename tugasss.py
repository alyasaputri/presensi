# Data mahasiswa
mahasiswa = [
    ["Andi", "Tinggi", "Lengkap"],
    ["Budi", "Rendah", "Tidak Lengkap"],
    ["Citra", "Tinggi", "Tidak Lengkap"],
    ["Deni", "Rendah", "Lengkap"],
    ["Alya", "Tinggi", "Lengkap"]
]

# Warna
UNGU = "\033[35m"
HIJAU = "\033[92m"
MERAH = "\033[91m"
RESET = "\033[0m"

# Variabel Rekap
aktif = 0
tidak_aktif = 0
bonus_ya = 0

print(UNGU + "=" * 70)
print("SISTEM PRESENSI MAHASISWA - DECISION TREE SEDERHANA")
print("=" * 70 + RESET)

print(f"{'Nama':<10} {'Kehadiran':<15} {'Tugas':<18} {'Status':<15} {'Bonus'}")
print(UNGU + "-" * 70 + RESET)

for data in mahasiswa:
    nama = data[0]
    kehadiran = data[1]
    tugas = data[2]

    # Decision Tree
    if kehadiran == "Tinggi":
        status = "Aktif"
        warna_status = HIJAU
        aktif += 1
    else:
        status = "Tidak Aktif"
        warna_status = MERAH
        tidak_aktif += 1

    # Fitur Bonus
    if kehadiran == "Tinggi" and tugas == "Lengkap":
        bonus = "Ya"
        bonus_ya += 1
    else:
        bonus = "Tidak"

    print(
        f"{nama:<10} "
        f"{kehadiran:<15} "
        f"{tugas:<18} "
        f"{warna_status}{status:<15}{RESET} "
        f"{bonus}"
    )

print(UNGU + "-" * 70 + RESET)

# Rekap Data
print("\n" + UNGU + "=" * 70)
print("REKAP DATA MAHASISWA")
print("=" * 70 + RESET)

print("Jumlah Mahasiswa      :", len(mahasiswa))
print("Mahasiswa Aktif       :", aktif)
print("Mahasiswa Tidak Aktif :", tidak_aktif)
print("Penerima Bonus        :", bonus_ya)

print(UNGU + "=" * 70 + RESET)

print("\nProgram selesai.")