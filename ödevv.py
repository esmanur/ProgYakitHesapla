import bs4 as bs
import urllib.request as urlReq
ilce_listesi=[]

for i in range(1,26):
    adres=''
    adres='http://www.izmir-vho.org/klinikler.php?sayfa='+str(i)+'&ilcesecim=0'
    src=urlReq.urlopen(adres)
    sayfa=bs.BeautifulSoup(src,'lxml')

    for j in sayfa.findAll('td'):
        ilce_listesi.append(j.string)

print("Aliağa'da",ilce_listesi.count("Aliağa"),"tane Veteriner Kliniği bulunmaktadır.")
print("Balçova'da",ilce_listesi.count("Balçova"),"tane Veteriner Kliniği bulunmaktadır.")
print("Bayındır'da",ilce_listesi.count("Bayındır"),"tane Veteriner Kliniği bulunmaktadır.")
print("Bayraklı'da",ilce_listesi.count("Bayraklı"),"tane Veteriner Kliniği bulunmaktadır.")
print("Bergama'da",ilce_listesi.count("Bergama"),"tane Veteriner Kliniği bulunmaktadır.")
print("Beydağ'da",ilce_listesi.count("Beydağ"),"tane Veteriner Kliniği bulunmaktadır.")
print("Bornova'da",ilce_listesi.count("Bornova"),"tane Veteriner Kliniği bulunmaktadır.")
print("Buca'da",ilce_listesi.count("Buca"),"tane Veteriner Kliniği bulunmaktadır.")
print("Çeşme'de",ilce_listesi.count("Çeşme"),"tane Veteriner Kliniği bulunmaktadır.")
print("Çiğli'de",ilce_listesi.count("Çiğli"),"tane Veteriner Kliniği bulunmaktadır.")
print("Dikili'de",ilce_listesi.count("Dikili"),"tane Veteriner Kliniği bulunmaktadır.")
print("Foça'da",ilce_listesi.count("Foça"),"tane Veteriner Kliniği bulunmaktadır.")
print("Gaziemir'de",ilce_listesi.count("Gaziemir"),"tane Veteriner Kliniği bulunmaktadır.")
print("Güzelbahçe'de",ilce_listesi.count("Güzelbahçe"),"tane Veteriner Kliniği bulunmaktadır.")
print("Karabağlar'da",ilce_listesi.count("Karabağlar"),"tane Veteriner Kliniği bulunmaktadır.")
print("Karaburun'da",ilce_listesi.count("Karaburun"),"tane Veteriner Kliniği bulunmaktadır.")
print("Karşıyaka'da",ilce_listesi.count("Karşıyaka"),"tane Veteriner Kliniği bulunmaktadır.")
print("Kemalpaşa'da",ilce_listesi.count("Kemalpaşa"),"tane Veteriner Kliniği bulunmaktadır.")
print("Kınık'ta",ilce_listesi.count("Kınık"),"tane Veteriner Kliniği bulunmaktadır.")
print("Kiraz'da",ilce_listesi.count("Kiraz"),"tane Veteriner Kliniği bulunmaktadır.")
print("Konak'ta",ilce_listesi.count("Konak"),"tane Veteriner Kliniği  bulunmaktadır.")
print("Menderes'te",ilce_listesi.count("Menderes"),"tane Veteriner Kliniği bulunmaktadır.")
print("Menemen'de",ilce_listesi.count("Menemen"),"tane Veteriner Kliniği bulunmaktadır.")
print("Narlıdere'de",ilce_listesi.count("Narlıdere"),"tane Veteriner Kliniği  bulunmaktadır.")
print("Ödemiş'te",ilce_listesi.count("Ödemiş"),"tane Veteriner Kliniği bulunmaktadır.")
print("Seferihisar'da",ilce_listesi.count("Seferihisar"),"tane Veteriner Kliniği bulunmaktadır.")
print("Selçuk'ta",ilce_listesi.count("Selçuk"),"tane Veteriner Kliniği bulunmaktadır.")
print("Tire'de",ilce_listesi.count("Tire"),"tane Veteriner Kliniği bulunmaktadır.")
print("Torbalı'da",ilce_listesi.count("Torbalı"),"tane Veteriner Kliniği bulunmaktadır.")
print("Urla'da",ilce_listesi.count("Urla"),"tane Veteriner Kliniği bulunmaktadır.")

#listenin tüm elemanlarını bastrıp test etmek için..
#for p in ilce_listesi:
#    print(p)

