import random

nim_list = []
loker_tersisa = list(range(1, 41))

while True:
    print("\n=== Sistem Penugasan Loker ===")
    print("1. Tambahkan NIM dan Dapatkan Loker")
    print("2. Tampilkan Daftar NIM dan Loker")
    print("3. Keluar")
    
    pilihan = input("Pilih opsi (1/2/3): ")
    
    if pilihan == '1':
        if len(loker_tersisa) == 0:
            print("Maaf, semua loker telah terisi!")
        else:
            nim = input("Masukkan NIM Anda: ")
            if nim in nim_list:
                print("NIM sudah terdaftar, silakan masukkan NIM lain.")
            else:
                nim_list.append(nim)
                loker = random.choice(loker_tersisa)
                loker_tersisa.remove(loker)
                print(f"NIM {nim} mendapatkan loker nomor {loker}.")
    elif pilihan == '2':
        print("\n=== Daftar NIM dan Loker ===")
        if not nim_list:
            print("Belum ada NIM yang terdaftar.")
        else:
            for i, nim in enumerate(nim_list):
                print(f"{i+1}. NIM: {nim}")
            print(f"\nLoker tersisa: {loker_tersisa}")
    elif pilihan == '3':
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
