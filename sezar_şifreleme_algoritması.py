sifre=input("sifrelenmis metni giriniz=")
uzunluk=len(sifre)
sifre_liste=list(sifre)

with open("dosya.txt","w") as dosya:
    for anahtar in range(1,27):
        dosya.write(str(anahtar)+". ")
        for eleman in sifre_liste:
            ascii_karsilik=ord(eleman)
            if ascii_karsilik+anahtar>122:
                eklenecek_anahtar=anahtar-(123-ascii_karsilik)
                ascii_karsilik=97
                yeni_harf=chr(ascii_karsilik+eklenecek_anahtar)
            else:
                yeni_harf = chr(ord(eleman)+anahtar)
            dosya.write(yeni_harf)
        dosya.write("\n")        
print("\n\n\nisleminiz tamamlandi\n\n\n")
"# python"
