import random
import time

# Fungsi pembungkus untuk mengukur waktu eksekusi
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Running time: {end_time - start_time:.6f} detik")
    return result

# Fungsi Insertion Sort Iteratif
def insertion_sort_iterative(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Fungsi Insertion Sort Rekursif
def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

# Fungsi untuk menampilkan daftar NIM dan loker
def tampilkan_daftar_nim_loker(nim_list, nim_to_loker):
    for i, nim in enumerate(nim_list):
        print(f"{i+1}. NIM: {nim}, Loker: {nim_to_loker[nim]}")

# Main Program
nim_list = []
loker_tersisa = list(range(1, 101))
nim_to_loker = {}

while True:
    print("\n=== Sistem Reservasi Perpustakaan ===")
    print("1. Tambahkan NIM dan Dapatkan Loker")
    print("2. Tampilkan Daftar NIM dan Loker")
    print("3. Keluar")

    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == '1':
        if len(loker_tersisa) == 0:
            print("Maaf, semua loker telah terisi!")
        else:
            try:
                jumlah = int(input("Masukkan jumlah NIM yang akan diinput: "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0.")
                    continue
                for _ in range(jumlah):
                    if len(loker_tersisa) == 0:
                        print("Maaf, semua loker telah terisi!")
                        break
                    nim = input("Masukkan NIM Anda: ")
                    if nim in nim_list:
                        print("NIM sudah terdaftar, silakan masukkan NIM lain.")
                    else:
                        nim_list.append(nim)
                        loker = random.choice(loker_tersisa)
                        loker_tersisa.remove(loker)
                        nim_to_loker[nim] = loker
                        print(f"NIM {nim} mendapatkan loker nomor {loker}.")
            except ValueError:
                print("Masukkan angka yang valid untuk jumlah NIM.")
    elif pilihan == '2':
        if not nim_list:
            print("Belum ada NIM yang terdaftar.")
        else:
            print("\n=== Submenu Tampilkan Daftar ===")
            print("1. Urutkan menggunakan Insertion Sort (Iteratif)")
            print("2. Urutkan menggunakan Insertion Sort (Rekursif)")
            sub_pilihan = input("Pilih opsi (1/2): ")

            if sub_pilihan == '1':
                nim_list_sorted = measure_time(insertion_sort_iterative, nim_list.copy())
                print("\n=== Daftar NIM dan Loker (Iteratif) ===")
                tampilkan_daftar_nim_loker(nim_list_sorted, nim_to_loker)
            elif sub_pilihan == '2':
                nim_list_sorted = nim_list.copy()
                measure_time(insertion_sort_recursive, nim_list_sorted, len(nim_list_sorted))
                print("\n=== Daftar NIM dan Loker (Rekursif) ===")
                tampilkan_daftar_nim_loker(nim_list_sorted, nim_to_loker)
            else:
                print("Pilihan tidak valid di submenu.")
    elif pilihan == '3':
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
