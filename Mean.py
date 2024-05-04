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
#     if (ulang % 2 == 1):
#         hasil = n[round(ulang / 2)]
#     else:
#         hasil = (n[round((ulang / 2) - 0.5)] + n[round((ulang / 2) + 0.5)]) / 2
#     return hasil
# def modus(*n):
#     hasil = 
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
        print(f"Deret Angka : {n}")
        print(f"MEAN : {mean(n)}")
        # Extra point
        # print(f"MEDIAN : {median(n)}")
        # print(f"MODUS : {modus(n)}")
        break