def hosgeldin():
    print("""
Vücut kitle indeksi hesaplama programına hoşgeldin!
""")

hosgeldin()


def hesaplama():
    devamet = input("""
Devam etmek için DEVAM yaz!

""")
    if devamet.upper() == "DEVAM":
        boy = float(input("Boyunuz kaçtır?(ör/1.75): "))
        kilo = float(input("Kilonuz kaçtır?(ör/70): "))
        indeks = kilo/(boy**2)
        print("Sizin vücut kütle indeksiniz {}".format(indeks))
    if indeks >= 30:
        print("İstatistiklere göre siz obezsiniz!")
    elif indeks >= 25 and indeks <= 29.9:
        print("İstatistiklere göre siz hafif kilolusunuz!")
    elif indeks >= 18.5 and indeks <= 24.9:
        print("İstatistiklere göre siz normal kilodasınız!")
    elif indeks <= 18.8:
        print("İstatistiklere göre siz zayıfsınız!")


    tekrar()
def tekrar():

    tekraret = input("""
Tekrar hesaplama yapmak istiyormusun?
Lütfen yapmak istiyor isen E
Yapmamak istiyor isen H yaz.

""")
    if tekraret.upper() == "E":
        hesaplama()
    elif tekraret.upper() == "H":
        print("Daha sonra görüşürüz...")
    else:
        print("Lütfen geçerli bir harf giriniz!")
        tekrar()
    
hesaplama()
