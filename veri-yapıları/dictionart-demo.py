# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldıgımız bilgilerle dictionary içinde saklayınız.
# 2- ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

ürünler = { 
       '100': {'ad': 'iphone 8', 'fiyat': '5000'},
       '101': {'ad': 'iphone 9', 'fiyat': '6000'},
       '102': {'ad': 'iphone 10', 'fiyat': '6000'}
}

# id = input('id: ')
# ad = input('ad: ')
# fiyat = input('fiyat: ')


#ürünler[id]= {
 #   "ad": ad, 
  #  "fiyat": fiyat,
#}

#id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')


#ürünler[id]= {
 #   "ad": ad, 
  #  "fiyat": fiyat,
#}

#id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')


#ürünler[id]= {
#    "ad": ad, 
#    "fiyat": fiyat,
#}

###########################################################################

id = input('aramak istediginiz ürün id: ')
ürün = ürünler[id]
print(f'id: {id} ürün adi: {ürün["ad"]} ürün fiyati: {ürün["fiyat"]}')

































