import string
import random

#State input user per karakter
huruf = string.ascii_letters
angka = string.digits
simbol = string.punctuation

#Ask user ingin password yang bagaimana
def choosepassword(pilihan_user):
    if pilihan_user == "mudah":
        ukuran = 8
        pakaiangka = False
        pakaisimbol = False
    elif pilihan_user == "sedang":
        ukuran = 8
        pakaiangka = True
        pakaisimbol = False
    elif pilihan_user == "rumit":
        ukuran = 10
        pakaiangka = True
        pakaisimbol = True

    #state apa saja yang akan dipakai
    karakter = huruf
    if pakaiangka:
        karakter += angka
    if pakaisimbol:
        karakter += simbol
    
    password = ""

    sesuai = False
    punyahuruf = False
    punyaangka = False
    punyasimbol = False

    while len(password) < ukuran or sesuai == False:
        karakter_baru = random.choice(karakter)
        password += karakter_baru
        if karakter_baru in huruf:
            punyahuruf = True
        elif karakter_baru in angka:
            punyaangka = True
        elif karakter_baru in simbol:
            punyasimbol = True

        if pilihan_user == "mudah" and punyahuruf:
            sesuai = True
        elif pilihan_user == "sedang" and punyahuruf and punyaangka:
            sesuai = True
        elif pilihan_user == "rumit" and punyahuruf and punyaangka and punyasimbol:
            sesuai = True

        if len(password) == ukuran and sesuai == False:
            password -= karakter_baru

    return password

    

#Make fungsi generator
