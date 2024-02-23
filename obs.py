import hashlib
ogrenci_puan={"huso":"55","zeynep":"100","sena":"80"}
ogrenciler = {"huso": hashlib.md5("555005".encode()).hexdigest(),
                 "zeynep": hashlib.md5("551846".encode()).hexdigest(),
                 "sena": hashlib.md5("0120223".encode()).hexdigest()}

yoneticikulanicilar = {"mehmet": hashlib.md5("2016051".encode()).hexdigest(),
                       "yusuf": hashlib.md5("2015785".encode()).hexdigest(),
                       "ayse": hashlib.md5("10472283".encode()).hexdigest()}
def anamenü():
    secim=input(" hangii islemi yapmak istiyorsunu \n")
    print("1)ogrenci girisi")
    print(" 2)ogretim gorevlisi")  
    if secim=="ogrenci":
            ogrencikulanci=input("lütfen kulanici adinizi giriniz:")
            ogrencisifre=input("lütfen sifrenizi giriniz:")
            def ogrencigirisi():
                 print(ogrencikulanci,"=",ogrenci_puan[ogrencikulanci])
            if ogrencikulanci in ogrenciler & ogrencisifre in ogrenciler[ogrencikulanci]:
                ogrencigirisi()
            else:
                print("sifre veya kulanici adi yanlis lütfen tekrar deneyin")
                feedback()
    elif secim== "gorevli":
        
        kulaniciadi=input("lütfen kulanici adiniz giriniz:")
        sifre=input("lütfen sifrenizi giriniz:")
        if kulaniciadi in yoneticikulanicilar and sifre in yoneticikulanicilar[kulaniciadi]:
            yonetim()
        else:
            print("sifre veya kulainici adi yanlis lütfen tekrar deneyiniz")
            feedbackgorevli()      
    else:
        print("yanlis giris... lütfen tekrar deneyiniz")
        anamenü()
def yonetim():
    secim2=int(input("ne yapmak istiyorsunuz"))
    print("1) ogrenci puan girisleri")
    print("2) puan listesi goruntuleme")
    print("3)cikis ")
    if secim2==1:
        puan()
    elif secim2==2:
        print(ogrenci_puan)
    elif secim2==3:
        anamenü()
    else:
        print("lütfen tekrar deneyiniz")
        yonetim()
def puan():
    girisisim=input("not girisi saglamak istediginizö ogrenicinin ismi")
    for girisisim in ogrenci_puan:
         ogrenci_puan[girisisim]=input("puani giriniz")
         break
def feedback():
            
            ogrencikulanci=input("lütfen kulanici adinizi giriniz:")
            ogrencisifre=input("lütfen sifrenizi giriniz:")
            def ogrencigirisi():
                 print(ogrencikulanci,"=",ogrenci_puan[ogrencikulanci])
            if ogrencikulanci in ogrencigirisi & ogrencisifre in ogrencigirisi[ogrencikulanci]:
                ogrencigirisi()
            else:
                print("sifre veya kulanici adi yanlis lütfen tekrar deneyin")
                feedback()
def feedbackgorevli():
        kulaniciadi=input("lütfen kulanici adiniz giriniz")
        sifre=input("lütfen sifrenizi giriniz")
        if kulaniciadi in yoneticikulanicilar & sifre in yoneticikulanicilar[kulaniciadi]:
            yonetim()
        else:
            print("sifre veya kulainici adi yanlis lütfen tekrar deneyiniz")
if __name__ == "__main__":
    anamenü()