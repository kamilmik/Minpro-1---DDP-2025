# Mini Project 1 DDP-2025

# Profil

Nama : Muhammad Ibrahim Kamil \
NIM : 2509116012 \
Sistem Informasi A'2025 

# Flowchart
berikut adalah Flowchart dari program :

![DDP1 MINPRO-2](https://github.com/user-attachments/assets/b27b7e0b-ed25-4adc-9341-1b2663e6415c)

# Alur Program
*Menu :* \
    Pada awal run program, program akan menampilkan menu awal berupa pilihan menu dan user diminta untuk menginput nilai sesuai pilihan, terdapat 5 pilihan : 1. Lihat produk, 2. Tambah Produk, 3. Hapus Produk, 4. Catat Penjualan, dan 5. Hitung Keuntungan. Jika User menginput diluar dari angka 1-5 maka program akan memberi output "input tidak valid" seperti contoh gambar berikut:

<img width="310" height="168" alt="Menu awal1" src="https://github.com/user-attachments/assets/b8dc9b67-cbc1-4fe6-a035-3cc46a1092b3" />

*- Lihat Produk (input 1)* \
  Pilihan Lihat (READ) untuk membuka daftar catatan produk. Fungsinya untuk melihat semua produk yang sudah ada dari list produk. Program akan menampilkan rincian dari setiap produk, mulai dari nama, modal, harga jual, jumlah stok, dan berapa banyak yang sudah terjual.
  
<img width="318" height="414" alt="Lihat Produk" src="https://github.com/user-attachments/assets/3749e9ad-e674-43ab-b38c-7b916767188a" />

*- Tambah Produk (input 2)* \
  Pilihan Tambah (ADD) berfungsi untuk menambah Produk Baru ke list Produk. Program akan meminta User memasukkan nama produk, modal (biaya produksi), harga jual, dan jumlah stok awal, kecuali jumlah terjual, akan otomatis terstatement nol.
  Setelah User memasukkan semua data, program akan menyimpan produk baru tersebut ke dalam daftar. User akan melihat pesan konfirmasi bahwa produk berhasil ditambahkan, lengkap dengan rincian data produk tersebut serta total modal.
  
<img width="945" height="150" alt="Tambah Produk" src="https://github.com/user-attachments/assets/0bd76227-d348-4df0-bce0-4064ac1344d2" />

*- Hapus Produk (input 3)* \
  Pilihan Hapus (DELETE). User akan diminta input nama produk yang ingin dihapus, Jika nama produk yang User masukkan cocok dengan yang ada di daftar, produk tersebut akan dihapus. Program akan menampilkan konfirmasi bahwa produk telah terhapus dan menunjukkan sisa produk yang ada di daftar serta menampilkan total modal yang sudah dikurang produk dihapus.
  Jika nama produk tidak ditemukan, program akan memberi tahu Anda bahwa produk tidak ada di daftar.

<img width="743" height="137" alt="Hapus Produk" src="https://github.com/user-attachments/assets/3ca60bc7-d6f9-4eb0-9ba2-3e075e6799ee" />

*- Catat Penjualan (Input 4)* \
   Fitur ini digunakan setiap kali ada produk yang laku terjual. Fungsinya untuk mencatat transaksi penjualan dan memperbarui stok barang. Program akan meminta User memasukkan nama produk yang terjual lalu jumlah yang laku.
  Jika produk ditemukan, program akan mengurangi jumlah stok dan menambahkan jumlah yang terjual. User akan melihat pesan konfirmasi bahwa penjualan berhasil dicatat, beserta jumlah stok terbaru.
  Jika produk tidak ditemukan, program akan menampilkan pesan Produk tidak ditemukan.

<img width="406" height="104" alt="Catat Penjualan" src="https://github.com/user-attachments/assets/30661d32-c54c-4d99-a181-8085b2c29ebd" />

*- Hitung Keuntungan (Input 5)* \
   fitur Hitung keuntungan untuk menghitung seberapa untung bisnis UMKM User, juga untuk melacak total modal dan total pendapatan. Setelah User memilih opsi ini, program akan menampilkan submenu dengan tiga pilihan:

   <img width="265" height="108" alt="Submenu-5" src="https://github.com/user-attachments/assets/9e74cac5-13a6-4310-861c-4108be1100ee" />

a. Total Modal: Menghitung dan menampilkan total biaya produksi dari semua produk yang ada.

<img width="288" height="150" alt="a" src="https://github.com/user-attachments/assets/7c48ff4c-7dcc-4197-860d-8de6593ad13e" />

b. Total Keuntungan Kotor: Menghitung dan menampilkan total pendapatan dari semua produk yang sudah terjual (harga jual dikalikan jumlah yang laku), tanpa dikurangi modal.

<img width="317" height="155" alt="b" src="https://github.com/user-attachments/assets/70cd3cdf-c188-4593-9cb1-997b5123191d" />

c. Total Keuntungan Bersih: Menghitung dan menampilkan keuntungan murni yang didapat, yaitu total keuntungan kotor dikurangi total modal yang telah dikeluarkan untuk produk yang terjual.

<img width="340" height="172" alt="c" src="https://github.com/user-attachments/assets/bbd74660-1049-4e0d-bf4c-853d2aa70a24" />

dan jika user memasukkan input selain a/b/c maka program akan menampilkan output pilihan tidak valid 

<img width="268" height="152" alt="5invalid" src="https://github.com/user-attachments/assets/2f53192b-e26c-4efc-8f6d-14e83f1a60c6" />

jika semua input pada menu awal salah atau tidak memenuhi kondisi, maka program akan memberi notifikasi jika input tidak valid dan memberhentikan program. 

<img width="310" height="168" alt="Menu awal1" src="https://github.com/user-attachments/assets/2965d611-0922-4089-b15d-87702bdecca2" />



