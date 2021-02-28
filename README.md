# Penyusunan Rencana Kuliah dengan *Topological Sort* (Penerapan *Decrease and Conquer*)

> Program sederhana ini merupakan aplikasi dari materi *Decrease and Conquer* yang telah dipelajari di kuliah IF2211 Strategi Algoritma. Program ini dapat menyusun
rencana pengambilan kuliah dan penyusunan
rencana kuliah tersebut diimplementasikan dengan menggunakan pendekatan *Topological Sorting*. 

## Pengaturan dan instalasi
Pastikan python3 (versi yang direkomendasikan) sudah terinstall di PC anda. Pembuat menggunakan Python versi 3.7.4.

## Cara menggunakan program
* Arahkan direktori anda menuju folder src
* Jalankan program di terminal dengan memasukkan perintah `python3 13519082.py`
* Masukkan nama <i>file</i> .txt yang berisi daftar mata kuliah yang ingin diambil. Telah disediakan 8 <i>file</i> .txt untuk dicoba pada folder test. Apabila ingin menambahkan soal lain, dapat menambahkan <i>file</i> .txt baru di folder tersebut. Pastikan format sesuai dengan format berikut:
```
<kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.
<kode_kuliah_2>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>.
<kode_kuliah_3>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>, <kode kuliah prasyarat - 4>.
<kode_kuliah_4>.
dst.
```
* Program akan langsung menunjukkan mata kuliah apa saja yang harus diambil setiap semester.

## Identitas
Dibuat oleh Jeanne D'Arc Amara Hanieka (13519082)
untuk mata kuliah IF2211 Strategi Algoritma tahun 2020/2021

Kontak yang dapat dihubungi:  
* E-mail: 13519082@std.stei.itb.ac.id
