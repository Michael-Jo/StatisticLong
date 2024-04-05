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
while y.lower() == "y":
    ulang += 1
    print("-"*15, "NILAI MEAN", "-"*15)
    n.append(int(input("Masukan Angka : ")))
    y = input("Lanjut ? (y/t) : ")
    if y.lower() == "y":
        os.system( "cls" )
    else:
        # def mean(*n): # tidak bisa digunakan diluar bagian 'else' ini jika fungsinya disini
        #     hasil = sum(*n) / ulang
        #     return hasil
        print(f"MEAN : {mean(n)}")
        break