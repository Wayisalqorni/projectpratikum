# projectpratikum
# Tugas ini untuk melengkapi pertemuan ke 6<br> 

#Dan menjelaskan project<br> 

![upb](poto/upb.PNG)

**Nama  :Wayis Al Qorni TS**<br> 
**Nim   :312010169**<br> 
**Kelas :TI.A1.20** <br>
**Tugas :Bahasa Pemrogramman**<br>

# Pertemuan 5 - Tugas<br>

Pada pertemuan 5 Bahasa Pemrograman saya akan membuat Aplikasi Biodata Python (seperti Gambar dibawah ini) 

![tugas5](poto/tugas5.PNG)

Saat ini saya akan menjelaskan hasil dari tugas tersebut. 
Berikut source code nya atau Klik Link berikut (pertemuan5 python):


print("==============================") <br>
print("= NAMA    : Wayis Al Qorni TS ") <br>
print("= NIM     : 312010169         ") <br>
print("= KELAS   : TI.20 A.1         ") <br>
print("==============================") <br>

`print("Please enter your full name : Wayis Al Qorni TS")` <br> 
`fullname=input()` <br>
`print("Please enter nickname : Wayis")` <br> 
`nickname=input()` <br>
`print("Please enter your NPM : 312010169")` <br> 
`npm=input()` <br>
`print("Please enter place of birth : BEKASI")` <br> 
`pob=input()` <br>
`print("Please enter date of birth : 19")` <br> 
`date=input()` <br>
`print("Please enter your month of birth : Februari")` <br> 
`month=input()` <br>
`print("Please enter year of birth : 2001")` <br> 
`year=input()` <br>
`print("Please enter your phone number : 08210142289")` <br>
`phone=input()` <br>
`print("Please enter your address : Kp.Rawa julang")` <br> 
`address=input()` <br>

`dob=input("2020-year")` <br>

`print("\n\n Assalamu'alaikum. ")` <br>
`print("f\n Let me introduce my self, my name is {Wayis Al Qorni TS}, but you can call me {Wayis}, my NPM {312010169}, I was born in {BEKASI} and iam {2020} years old, I am very glad if you want to invite my house in {Kp.Rawa julang}, So don't forget to call me before with the number {08210142289}, \n\n Thanks you very much ")` <br>
Berikut Penjelasannya :

print("please enter your full name : ") <br>
``` <br>
Source code diatas berfungsi untuk mencetak hasil / output berupa **Please enter your full name :** ". <br>
 Untuk menampilkan output string, saya menggunakan *tanda petik dua* didalam fungsi print(), sedangkan jika saya ingin menampilkan output atau hasil berupa angka atau interger saya tidak perlu menggunakan *tanda petik dua*. Contohnya : <br>

``` 

print("Nama saya adalah...") <br>
print(1234567) <br>

(Seperti gambar dibawah ini)

![biodata](poto/biodata.PNG)

* Untuk source code berikutnya adalah inputan atau membuat variable. seperti syntax dibawah ini :

`fullname=input()` <br>
``` <br>
**Keterangan** : <br> 
`>Variable adalah sebuah wadah penyimpanan data pada program yang akan akan digunakan selama program itu berjalan. yang berfungsi sebagai variable dalam source code diatas adalah **fullname** . <br>
`>Fungsi **input()** adalah untuk memasukan nilai dari layar console di command prompt, lalu kemudian mengembalikan nilai saat kita menekan tombol enter *(newline)* <br> 
`*(newline)*` <br>

[poto](poto/input.png)<br>

pada gambar di atas, hasil dari inputan tersebut berwarna *hijau* <br>

* Untuk memasukan perintah lain seperti *Nikname, NPM, Place Of Birth, Date Of Birth, Year Of Birth, Phone Number, and Addres* mengikuti perintah sama seperti memasukan *fullname* <br>

* Untuk menghitung rumus saya menggunakan variable *DOB* yaitu 2020 (Tahun sekarang) dikurangin dengan Year of Birt, pada source code berikut : <br>
``` python 



dob=input("2020-year") <br>



``` <br>
Pada syntax/source diatas, saya menggunakan variable (dob) dimana untuk menghitung umur (variable **age** pada output), yaitu dengan rumus pada variable *dob=input("2020-year")* <br>

* langkah kali ini saya akan menampilkan output yang diminta oleh dosen.output pertama yang diminta Dosen adalah menampilkan salam, yaitu dengan mengetikkan syntax/source code berikut : <br>

``` python
print("\n\n Assalamu'alaikum. ")` <br>
``` <br>

``` 

Keterangan : <br>
1. Fungsi **\n** pada source code di atas adalah untuk memberi baris baru / enter / *(newline)* <br>

2. Fungsi print() seperti dijelaskan pada point **Output** diatas
Hasil dari source code diatas adalah seperti gambar dibawah ini : <br>

![biodata2](poto/biodata2.PNG)

print(f"Let me introduce my self, my name is {fullname}, but you can call me {nickname}, my NPM {npm}, I was born in {pob} and iam {dob} years old, I am very glad if you want to invite my house in {address}, So don't forget to call me before with the number {phone}, \n\n Thanks you ")

Keterangan :

* Fungsi huruf f pada perintah print(f"....") adalah fungsi print atau bisa memudahkan programer dalam mencetak statement dalam satu baris dibandingkan dengan metode yang lama yaitu memisahkan string dan variable dengan simbol koma( , ) atau plus ( + )
* sedangkan fungsi {} pada output tersebut adalah untuk menampilkan hasil dari variable
Hasil dari output tersebut seperti berikut :

![biodata3](poto/biodata3.PNG)

# Pertemuan 6 - Lab 1

Pada halaman ini (Tugas Pertemuan 6 - Lab 1) saya diberikan tugas oleh Dosen yaitu mempelajari operator aritmatika menggunakan bahasa Pemrograman pyhton. Berikut source code yang di berikan oleh dosen : 

#penggunaan end
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('z')

#penggunaan separator

`w, x, y, z = 10, 15, 20, 25`
`print(w, x, y, z)`
`print(w, x, y, z, sep=',')`
`print(w, x, y, z, sep='')`
`print(w, x, y, z, sep=':')`
`print(w, x, y, z, sep='.....')`

Oke, kali ini saya akan menjelaskan tentang materi yang di berikan oleh Dosen.

* Penggunaan END Penggunaan end digunakan untuk menambahkan karakter yang dicetak di akhir baris. secara default penggunaan end adalah untuk ganti baris. 

`print('A', end='')`
`print('B', end='')`
`print('C', end='')`
> Penggunaan print () digunakan untuk mencetak output, seperti syntax dibawah ini :

`print()`
>Syntax dibawah ini digunakan untuk menampilkan output berupa string

`print('X')`
`print('Y')`
`print('z')`

Hasil dari source code tersebut seperti gambar dibawah ini :

![end](poto/end.PNG)

* Penggunaan separator
>Pendeklarasian beberapa variable beserta nilainya

w,x,y,z=10,15,20,25
>Menampilkan hasil dari variable tiap-tiap variable

`print(w,x,y,z)`
>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah : (koma)

`print(w,x,y,z,sep=",")`
>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah

`print(w,x,y,z,sep="")`
>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah : (titik dua)

`print(w,x,y,z,sep=":")`
>Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemisah

`print(w,x,y,z,sep="-----")`

* hasil dari syntax / source code diatas adalah seperti berikut ini : 

![variabel](poto/variabel.PNG)

# Pertemuan 6 - Lab 1-2
* String Format
String formatting atau pemformatan string memungkinan kita menyuntikkan item kedalam string dari pada kita mencoba menggabungkan string menggunakan koma atau string concatenation.

* Penggunaan source code yang di berikan oleh dosen seperti berikut : 

![variabel2](poto/variabel2.PNG)

#string format 1
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**5)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

#string format 1
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))

Saat ini saya akan membahas satu persatu dari syntax.
* String Format 1 
Pada syntax / source code strring format satu akan menampilkan output berupa 2 outputan.
Yang pertama (sebelah kiri) akan menampilkan angka urut dari angka 0 hingga 10, sedangkan untuk sebelah kanan akan menampilkan Operasi Aritmatika Pangkat.
Dengan ketentuan sebagai berikut, Operasi pangkat dengan angka kiri sebagai pokok (Rumus : ** [bintang dua] )
Hasil dari syntax tersebut adalah 10 pangkat 0, hingga 10 pangkat 10, dengan output sebagai berikut :

![format](poto/format.PNG)

* String Format 2 

Pada syntax atau source code string format dua akan menampilkan output berupa 2 output'an juga (seperti String Format 1, yaitu kanan dan kiri )
Dengan ketentuan sebagai berikut :

secara Default, .format() menggunakan rata kiri, angka ke kanan. kita dapat menggunakan opsi opsional <,^, atau > untuk mengatur perataan kiri, tengah, atau kanan. Contoh lain dalam penggunaan .format() sebagai berikut :

`print('{0:8} | {1:9}'.format('Nama orang','Jumlah'))`
`print('{0:8} | {1:9}'.format('Sasa',3.))`
`print('{0:8} | {1:9}'.format('Nila',10))`

Hasil dari source code contoh diatas akan seperti berikut :

![sasa](poto/sasa.PNG)

Secara Default,.format() menggunakan rata text ke kiri, angka ke kanan, kita dapat menggunakan opsi opsional<,^,atau > untuk mengatur perataan kiri, tengah, atau kanan. Contoh lain dalam penggunaan .format() sebagai berikut : 

`print('{:<30}{:30}{:>30}'.format('motor','kereta','kapal'))`
`print('{:<30}{:30}{:>30}'.format(10,20,15))`

Hasil dari source code contoh diatas akan muncul seperti ini :

![motor](poto/motor.PNG)

# Konversi Nilai Variable Untuk pembahasan terakhir, yaitu konversi Nilai Variable Tugas lab 2

![lab2](poto/lab2.PNG)

* String Format 2

Variabel adalah tempat menyimpan data
menaruh / assignment nilai
a = 10 x = 5 panjang = 1000 print(0, 10**0)

pemanggilan pertama
print("Nilai a =", a) print("Nilai x =", x) print("Nilai panjang = ",panjang)

penamaan
nilai_y = 15 # dengan menggunakan underscore juta10 = 1000000 # ini boleh nilaiZ = 17.5 # ini boleh

pemanggilan kedua
print("Nilai a = ", a) a = 7 print("Nilai b = ", a)

assignment indirect
b = a print("Nilai b = ",b)

a=int(input("masukkan nilai a:")) b=int(input("masukkan nilai b:")) print("variable a=",a) print("variable b=",b) print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

konversi nilai variable
a=int(a) b=int(b) print("hasil pejumlahan {1}+{0}=%d".format(a,b) %(a+b)) print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))

![apa](poto/apa.PNG)

Untuk hasil dari String Format 2 adalah :










