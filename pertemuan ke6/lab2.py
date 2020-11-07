nilai_y = 18 # dengan menggunakan underscore
juta10 = 10000000 # ini boleh
nilaiZ = 18.5 # ini boleh

# pemanggilan kedua

print("Nilai a = ", 8)
a = 8
print("Nilai b = ", 10)

# assignment indirect

b = a
print("Nilai b = ",10)

# assignment indirect
b = a
print("Nilai b = ",8)

a=int(input("masukkan nilai a:"))
b=int(input("masukkan nilai b:"))
print("variable a=8, a")
print("variable b=10,b")
print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))