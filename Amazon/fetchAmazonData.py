import requests
from bs4 import BeautifulSoup
import time

baslangic = time.time()
besyildizurl = ""
biryildizurl = ""
dortyildizurl = ""
with open('besyildizurl.txt', 'r', encoding='windows-1254') as file:
    besyildizurl= file.read()
    file.close()
with open('biryildizurl.txt', 'r', encoding='windows-1254') as file:
    biryildizurl= file.read()
    file.close()
with open('dortyildizurl.txt', 'r', encoding='windows-1254') as file:
    dortyildizurl = file.read()
    file.close()
#Urllerin saklandigi txt dosyasindan cekilen metinler string variablea atanir.

besYildizList = list(besyildizurl.split("\n"))
birYildizList = list(biryildizurl.split("\n"))
dortYildizList = list(dortyildizurl.split("\n"))
urlsayisi= 1
def txtkayit(url_yildiz):
    global urlsayisi
    bestseller = requests.get(url_yildiz)
    html = bestseller.text
    parsedHtml = BeautifulSoup(html, "html.parser")
    spanlar = parsedHtml.find_all('span', class_='a-size-base review-text review-text-content')
    #bs4 ile cekilen html metni parselanir.
    with open("hotel.txt", 'r') as file:
        veri_str = file.readline().strip()
        satir = int(veri_str)
        #Kacinci satirda oldugunu txt dosyasinda saklar.
    for i in spanlar:
        span = i.text
        temizlenmisSpan = span.replace('\n', '')
        #Cekilen spandeki bosluklari temizler.
        with open('dosya.txt', 'a', encoding='utf-8') as file:
            file.write("1, " + temizlenmisSpan + "\n")
            file.close()
        #Yorumlari kaydeden txt dosyasina yazdirir.
        satir = satir + 1
    urlsayisi = urlsayisi + 1
    with open("hotel.txt", 'w') as file:
        file.write(str(satir))
        file.close()
    #Bir sonraki calistirma icin satir sayisini kaydeder.
for i in birYildizList:
    txtkayit(i)
#Secilen listeden def fonksiyonu calistirilir.
#5 yildiz ve 4 yildiz icin de program ayri ayri calistirildi.
bitis = time.time()
sure = bitis - baslangic
print("Kodun calisma suresi: " + str(sure))
#Kodun calisma suresini olcer :D
