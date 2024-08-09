with open("urunid.txt", 'r') as file:
    x = file.read()
    file.close()
#Burada urun idleri cekilir.

yildiz_bes = []
bes_list= list(x.split("\n"))
#Burada iki id arasini ayirip listeye atayan komut yazilir.

for i in bes_list:
    url_bes = "https://www.amazon.com.tr/product-reviews/" + i + "/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar"
    yildiz_bes.append(url_bes)
#Amazonda farkli urunlerin linklerinde sadece urun idleri ve yorumlarin listelendigi yildiz sayisi degistigi icin cekilen urun idleri urlye cevirecek kod yazilir.,

bes_string = "\n".join(yildiz_bes)
with open("besyildizurl.txt", 'w') as file:
    file.write(bes_string)
    file.close()
#Urlleri text dosyasina yazdirir.
#1 yildiz ve 4 yildizda da ayni kod asagida yazilmistir.

yildiz_bir = []
bir_list= list(x.split("\n"))

for i in bir_list:
    url_bir = "https://www.amazon.com.tr/product-reviews/" + i + "/ref=acr_dp_hist_5?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews#reviews-filter-bar"
    yildiz_bir.append(url_bir)

bir_string = "\n".join(yildiz_bir)
with open("biryildizurl.txt", 'w') as file:
    file.write(bir_string)
    file.close()

yildiz_dort = []
dort_list= list(x.split("\n"))

for i in dort_list:
    url_dort = "https://www.amazon.com.tr/product-reviews/" + i + "/ref=acr_dp_hist_5?ie=UTF8&filterByStar=four_star&reviewerType=all_reviews#reviews-filter-bar"
    yildiz_dort.append(url_dort)

dort_string = "\n".join(yildiz_dort)
with open("dortyildizurl.txt", 'w') as file:
    file.write(dort_string)
    file.close()