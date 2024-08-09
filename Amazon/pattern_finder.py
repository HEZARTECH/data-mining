# -*- coding: utf-8 -*-
import re

with open("b0.txt", 'r') as file:
    x = file.read()
    file.close()

pattern = r'B0\w+'
cekme = re.findall(pattern, x)
#Amazon'da urun kodlari B0 ile baslayan dizlier halinde saklanir.
#Bu regex komutu Bestseller bolumunden cekilen html dizisinin bir bolumunde B0 iceren butun urun idlerini bulmayi saglar.
kume = set(cekme)
cekme = list(kume)
#Burada ayni elemanlardan birkac kez kaydetmemesi icin ilk kume haline getirilip sonra tekrar listeye cevrilir.

for i in cekme:
    with open("urunid.txt", 'a') as file:
        file.write(i + "\n")
        file.close()
#Burada cekilen urun idleri txt dosyasina yazdirir.