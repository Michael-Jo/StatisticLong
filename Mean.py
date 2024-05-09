import os
import string
n = []
y = "y"
ulang = 0
# data = { # idk why this is here
#     "n" : ""
# }
# datas = dict.fromkeys( data.keys() )
def mean(*n):
    hasil = sum(*n) / ulang
    return hasil
# def median(*n): # extra point's spaghetti code
def median(*n):
    s_n = sorted(*n)
    if (ulang % 2 == 1):
        hasil = s_n[round(ulang / 2) - 1]
    else:
        hasil = (s_n[round((ulang / 2) - 1)] + s_n[round((ulang / 2))]) / 2
    return hasil
import statistics
def modus(**n):
    h_modus = statistics.multimode( n['modus'] )
    return h_modus
#     hasil = 0
#     count = len(*n)
#     for i in len(n):
#           if n[i] = max*n:
#               hasil++
#     return hasil
while y.lower() == "y":
    ulang += 1
    print("-"*15, "NILAI MEAN, MEDIAN, MODUS", "-"*15)
    n.append(int(input("Masukan Angka : ")))
    y = input("Lanjut ? (y/t) : ")
    if y.lower() == "y":
        os.system( "cls" )
    else:
        # def mean(*n): # tidak bisa digunakan diluar bagian 'else' ini jika fungsinya disini
        #     hasil = sum(*n) / ulang
        #     return hasil
        print(f"Deret Angka : {sorted(n)}")
        print(f"MEAN : {mean(n)}")
        # Extra point
        print(f"MEDIAN : {median(n)}")
        # print(f"MODUS : {modus(n)}")
        hasil_modus = modus( modus = n )
        print(f"MODUS : {hasil_modus}")
        break