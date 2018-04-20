
import getpass
from perhitungan.penilaian_mahasiswa import nilai_mahasiswa
from perhitungan.pembayaran_mahasiswa import pembayaran
from perhitungan.kalkulator import menu_kalkulator


def menu():
    print("\n\t----Pilihan-----")
    print("\t1. Penilaian Mahasiswa")
    print("\t2. Pembayaran Mahasiswa")
    print("\t3. Kalkulator")

    pilih = input("\n\tSilahkan pilih : ")
    if pilih == "1" :
        nilai_mahasiswa()
    elif pilih == "2" :
        pembayaran()
    elif pilih == "3" :
        menu_kalkulator()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y/n) ?")
    if tanya == "y":
        menu()
    elif tanya == "n":
        exit
    else:
        print("\n\tSalah Input !!")
        
username = input("\nUsername : ")
password = getpass.getpass()
print("======================================================")

if username == "fr" and password == "24021998" :
    menu()

else :
    print("Maaf username atau password kamu salah")



