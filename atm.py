_kartsifresi="1707"
_bakiye=2500
_denemehakki=3
print("""
-------------------------------------------
TalayBank'a Hosgeldiniz!! 


***Gelecegin Bankasi***
-------------------------------------------
""")

_islemdurumu=True
_kartislemdurumu=True

while _islemdurumu:
    _girilensifre=input("Kart Sifrenizi Giriniz: ")
    if _girilensifre != _kartsifresi:
        print("Yanlis Sifre Girdiniz.Lütfen Tekrar Deneyiniz")
        _denemehakki -=1
        print(_denemehakki,"Deneme Hakkiniz Kaldi")
        if _denemehakki==0:
            print("Kartiniz Bloklanmistir.Lütfen Banka ile Görüsün.")
            _islemdurumu=False
    else:
        print("Giris Yapildi")
        print(""" 
        Yapilacak Islemi Seciniz 
        -------------------------------
        1-Para Çekme
        2-Para Yatirma
        3-Bakiye Sorgulama
        4-Kart İade
        --------------------------------
        """) 
        
        while _kartislemdurumu:
            print("-----------------------------------------")
            _islemNo=input("Islem Numarasini Giriniz: ")
            if _islemNo == "4":
                print("Cikis Yapildi.Yine Bekleriz..")
                _islemdurumu=False
                _kartislemdurumu=False
            
            elif _islemNo=="3":
                print("Toplam Bakiyeniz: ",_bakiye,"₺")
            elif _islemNo=="2":
                _yatirilacakMiktar=int(input("Yatirilacak Tutari Giriniz: "))
                _bakiye += _yatirilacakMiktar
                print("İslem Basariyla Gerceklesti")
            elif _islemNo=="1":
                _cekilecekTutar=int(input("Cekilecek Tutari Giriniz:"))
                if _bakiye >= _cekilecekTutar:
                    _bakiye -= _cekilecekTutar
                    print("Isleminiz Basariyla Gerceklesti")
                else: 
                    print("Yetersiz Bakiye")




            

