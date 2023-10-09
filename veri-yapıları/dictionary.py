# key - value


# 41 = Kocaeli
# 34 = İstanbul

# şehirler = ['Kocaeli','İstanbul']
# plakalar = [41,34]
# print(plakalar[0],şehirler[0])
# print(plakalar[1],şehirler[1])

# print(plakalar[şehirler.index('Kocaeli')])
# print(plakalar[şehirler.index('İstanbul')])

# plakalar = {'kocaeli':41,'istanbul':34}
# print(plakalar['kocaeli'])"""
# plakalar['rize'] = 53
# plakalar['izmir'] = 35
# plakalar['izmir'] = 36 # 35 to 36 
# print(plakalar)

ogrenciler = {
    100:{
  "ad": "çinar",
   "soyad": "turan",
    "yas":4,
    "notlar": [70,80,70]
 },
 101:{
    "ad":"ada",
    "soyad":"bilgi",
    "yas":10
   }
 }
sonuc = (ogrenciler[100]["notlar"] [0] + ogrenciler[100]["notlar"] [1] + ogrenciler[100]["notlar"] [2]) / 3
print(sonuc)

sonuc = ogrenciler [100]["ad"] # ["ad"] şeklinde ekleme yaptıgımız zaman sadece "ad" yazdırır.
sonuc = ogrenciler[101]["yas"] # ["yas"] şeklinde ekleme yaptıgınız zaman sadece "yas" yazdırır.











