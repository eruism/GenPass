import passgen

def mainprompt():
    pilihan = ['mudah', 'sedang', 'rumit']
    print("Password seperti apa yang anda inginkan?")
    pilihan_user = input("Ketik Pilihan (mudah,sedang,rumit) : ")
    if pilihan_user in pilihan:
        pwd = passgen.choosepassword(pilihan_user)
    else:
        print("Pilih pilihan yang sudah disediakan \n (mudah, sedang, rumit)")
        return False
    print("Password anda telah digenerate")
    print("Password : "+pwd)

mainprompt()
    