print("~~~ Aplikasi Manajemen Produk UMKM ~~~")
print(" Nama : Muhammad Ibrahim Kamil")
print(" NIM  : 2509116012")
print(" Prodi: Sistem Informasi kelas A")
print(" Pratikum DDP Mini Project 1")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

produk = [
    ["susu", 5000, 7500, 10, 5],
    ["kopi latte", 10000, 15000, 15, 11],
    ["teh tarik", 8000, 12000, 20, 0]]

modal = produk[0][1] + produk[1][1] + produk[2][1]

#BAGIAN MENU UTAMA!
print("~~~ Menu Utama Produksi UMKM ~~~")
print("|1. Lihat Produk")
print("|2. Tambah Produk")
print("|3. Hapus Produk")
print("|4. Catat Penjualan")
print("|5. Hitung Keuntungan")
menu = input("Pilih menu 1-5: ")

#BAGIAN LIHAT PRODUK!
if menu == "1":
    print("Daftar Produk:")
    print(" - Nama: ", produk[0][0])
    print("   Modal: Rp", produk[0][1])
    print("   Harga Jual: Rp", produk[0][2])
    print("   Stok: ", produk[0][3])
    print("   Terjual: ", produk[0][4])
    print()
    print(" - Nama: ", produk[1][0])
    print("   Modal: Rp", produk[1][1])
    print("   Harga Jual: Rp", produk[1][2])
    print("   Stok: ", produk[1][3])
    print("   Terjual: ", produk[1][4])
    print()
    print(" - Nama: ", produk[2][0])
    print("   Modal: Rp", produk[2][1])
    print("   Harga Jual: Rp", produk[2][2])
    print("   Stok: ", produk[2][3])
    print("   Terjual: ", produk[2][4])
    print()

#BAGIAN TAMBAH PRODUK!
elif menu == "2":
    nama = input("Nama Produk: ")
    modal_produk = int(input("Modal (Rp): "))
    jual = int(input("Harga Jual (Rp): "))
    stok = int(input("Jumlah Stok Awal: "))
    
    produk.append([nama, modal_produk, jual, stok, 0])
    
    modal = modal + modal_produk
    print(f"Produk: {produk[3][0]}, Modal: Rp{produk[3][1]}, Harga Jual: Rp{produk[3][2]}, Stok: {produk[3][3]}, berhasil ditambahkan 😎.")
    print(f"Total modal Anda sekarang: Rp{modal}")

#BAGIAN HAPUS PRODUK!
elif menu == "3":
    nama_hapus = input("Masukkan nama produk yang mau dihapus: ")
    if nama_hapus == produk[0][0]:
        modal = modal - produk[0][1]
        produk.pop(0)
        print("Produk berhasil dihapus🗑️")
        print(f"Sisa produk: {produk}")
        print(f"Total modal Anda sekarang: Rp{modal}")
    elif nama_hapus == produk[1][0]:
        modal = modal - produk[1][1]
        produk.pop(1)
        print("Produk berhasil dihapus🗑️")
        print(f"Sisa produk: {produk}")
        print(f"Total modal Anda sekarang: Rp{modal}")
    elif nama_hapus == produk[2][0]:
        modal = modal - produk[2][1]
        produk.pop(2)
        print("Produk berhasil dihapus🗑️")
        print(f"Sisa produk: {produk}")
        print(f"Total modal Anda sekarang: Rp{modal}")
    else:
        print("Produk tidak ditemukan")


#BAGIAN CATAT PENJUALAN!
elif menu == "4":
    nama_jual = input("Masukkan nama produk yang terjual: ")
    if nama_jual == produk[0][0]:
        jumlah = int(input("Jumlah yang terjual: "))
        produk[0][4] = produk[0][4] + jumlah
        produk[0][3] = produk[0][3] - jumlah
        print("Penjualan berhasil dicatat📝")
        print(f"Produk: {produk[0][0]}, Stok sisa: {produk[0][3]}, Terjual: {produk[0][4]}")
    elif nama_jual == produk[1][0]:
        jumlah = int(input("Jumlah yang terjual: "))
        produk[1][4] = produk[1][4] + jumlah
        produk[1][3] = produk[1][3] - jumlah
        print("Penjualan berhasil dicatat📝")
        print(f"Produk: {produk[1][0]}, Stok sisa: {produk[1][3]}, Terjual: {produk[1][4]}")
    elif nama_jual == produk[2][0]:
        jumlah = int(input("Jumlah yang terjual: "))
        produk[2][4] = produk[2][4] + jumlah
        produk[2][3] = produk[2][3] - jumlah
        print("Penjualan berhasil dicatat📝")
        print(f"Produk: {produk[2][0]}, Stok sisa: {produk[2][3]}, Terjual: {produk[2][4]}")

    else:
        print("Produk tidak ditemukan.")


#BAGIAN HITUNG KEUNTUNGAN!
elif menu == "5":
    print("~~~ Submenu Keuntungan ~~~")
    print("|a. Total Modal            |")
    print("|b. Total Keuntungan Kotor |")
    print("|c. Total Keuntungan Bersih|")
    menu_keuntungan = input("Pilih a-c: ")
    
    total_jual = (produk[0][2] * produk[0][4]) + (produk[1][2] * produk[1][4]) + (produk[2][2] * produk[2][4])
    total_modal_terjual = (produk[0][1] * produk[0][4]) + (produk[1][1] * produk[1][4]) + (produk[2][1] * produk[2][4])
    keuntungan_bersih = total_jual - total_modal_terjual

    if menu_keuntungan == "a":
        print("Total Modal: Rp", modal)
    elif menu_keuntungan == "b":
        print("Total Keuntungan Kotor: Rp", total_jual)
    elif menu_keuntungan == "c":
        print("Total Keuntungan Bersih: Rp", keuntungan_bersih)
        print("dengan total Modal: Rp", modal)
    else:
        print("Pilihan tidak valid.")

else:
    print("Pilihan tidak valid")