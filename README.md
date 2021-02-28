# Tugas Kecil II IF2211 Strategi Algoritma
Penyusunan Rencana Kuliah dengan Topological Sort

## Deskripsi Singkat
Program ini dapat menyusun rencana pengambilan kuliah dengan memanfaatkan algoritma Decrease and Conquer, lebih tepatnya dengan pendekatan Topological Sort.
Misal didapat masukan seperti berikut:
```
C1, C3.
C2, C1, C4.
C3.
C4, C1, C3.
C5, C2, C4.
```
Hasil penyusunannnya adalah:
```
Semester I : C3
Semester II : C1
Semester III : C4
Semester IV : C2
Semester V : C5.
```


## Requirements
* Python 3.6.x or higher

## Instalasi & Cara Penggunaan
```
git clone https://github.com/rayfazt/stima-toposort.git
cd stima-toposort && cd src
python 13519039.py
```
Saat diminta input, pastikan input berupa nama file tanpa ekstensi .txt (contoh: test1) <br/>

## Author
Made with :sob: by Rayhan Alghifari (13519039) @ Feb 2021 <br/>
Reach me at [Twitter](https://twitter.com/rayalghi) or [Linkedin](https://linkedin.com/in/rayhanfauzta)
