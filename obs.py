import hashlib

ogrenci_puan = {"huso": "55", "zeynep": "100", "sena": "80"}
ogrenciler = {
    "huso": hashlib.md5("555005".encode()).hexdigest(),
    "zeynep": hashlib.md5("551846".encode()).hexdigest(),
    "sena": hashlib.md5("0120223".encode()).hexdigest()
}

yoneticikulanicilar = {
    "mehmet": hashlib.md5("2016051".encode()).hexdigest(),
    "yusuf": hashlib.md5("2015785".encode()).hexdigest(),
    "ayse": hashlib.md5("10472283".encode()).hexdigest()
}


def anamenü():
    secim = input("Hangi işlemi yapmak istiyorsunuz?\n")
    print("1) Öğrenci girişi")
    print("2) Öğretim görevlisi")
    if secim == "1":
        ogrencikulanci = input("Lütfen kullanıcı adınızı giriniz: ")
        ogrencisifre = input("Lütfen şifrenizi giriniz: ")

        def ogrencigirisi():
            print(ogrencikulanci, "=", ogrenci_puan[ogrencikulanci])

        if ogrencikulanci in ogrenciler and ogrencisifre in ogrenciler[ogrencikulanci]:
            ogrencigirisi()
        else:
            print("Şifre veya kullanıcı adı yanlış, lütfen tekrar deneyin")
            feedback()
    elif secim == "2":
        kulaniciadi = input("Lütfen kullanıcı adınızı giriniz: ")
        sifre = input("Lütfen şifrenizi giriniz: ")
        if kulaniciadi in yoneticikulanicilar and sifre in yoneticikulanicilar[kulaniciadi]:
            yonetim()
        else:
            print("Şifre veya kullanıcı adı yanlış, lütfen tekrar deneyiniz")
            feedbackgorevli()
    else:
        print("Yanlış giriş... Lütfen tekrar deneyiniz")
        anamenü()


def yonetim():
    secim2 = int(input("Ne yapmak istiyorsunuz?\n1) Öğrenci puan girişleri\n2) Puan listesi görüntüleme\n3) Çıkış\n"))
    if secim2 == 1:
        puan()
    elif secim2 == 2:
        print(ogrenci_puan)
    elif secim2 == 3:
        anamenü()
    else:
        print("Lütfen tekrar deneyiniz")
        yonetim()


def puan():
    giris_ismi = input("Not girişi sağlamak istediğiniz öğrencinin ismi: ")
    for ogrenci in ogrenci_puan:
        ogrenci_puan[ogrenci] = input(f"{giris_ismi}'nin puanını giriniz: ")
        break


def feedback():
    ogrenci_kullanici = input("Lütfen kullanıcı adınızı giriniz: ")
    ogrenci_sifre = input("Lütfen şifrenizi giriniz: ")

    def ogrencigirisi():
        print(ogrenci_kullanici, "=", ogrenci_puan[ogrenci_kullanici])

    if ogrenci_kullanici in ogrenciler and ogrenci_sifre in ogrenciler[ogrenci_kullanici]:
        ogrencigirisi()
    else:
        print("Şifre veya kullanıcı adı yanlış, lütfen tekrar deneyin")
        feedback()


def feedbackgorevli():
    kulaniciadi = input("Lütfen kullanıcı adınızı giriniz: ")
    sifre = input("Lütfen şifrenizi giriniz: ")
    if kulaniciadi in yoneticikulanicilar and sifre in yoneticikulanicilar[kulaniciadi]:
        yonetim()
    else:
        print("Şifre veya kullanıcı adı yanlış, lütfen tekrar deneyiniz")


if __name__ == "__main__":
    anamenü()
