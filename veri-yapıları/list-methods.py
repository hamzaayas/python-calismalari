sayilar = [1,2,3,4,5,46]
harfler = ['a','b','y','s','c']

sonuc = min(sayilar) # sayının en düşük degerini alir.
sonuc = max(sayilar) # sayinin en büyük degerini alır.
sonuc = min(harfler) # alfabetik harflere göre en düşük veya en büyük degeri alir. 
sonuc = max(harfler) 

# ekleme
sayilar.append(10) # listeye ekleme yapar.
sonuc = sayilar
sayilar.insert(3,5) # listenin 3.sayısını 5 e degiştirir.
sayilar.insert(-1,40) # listenin sonundaki sayıyı degiştirir.
sayilar.insert(len(sayilar),150) # listenin sonuna ekleme yapar.
# silme 
sayilar.pop() # listenin sonundaki şeyi siler.
sayilar.remove(46) # bu şekilde sayilar içindeki belirttiginiz degeri siler.
harfler.remove("a") # bu şekilde harflerin içinde belirttiginz degeri siler.
# sıralama
sayilar.sort() # bu şekilde sayiları sırasıyla yazabilirsiniz.
harfler.sort() # bu şekilde harfleri alfabetik sıraya göre sıralarsınız.
sayilar.reverse() # bu şekilde sayıları veya harfleri tersten yazarsınız.
sayilar.count(5)


print(sayilar.count(5)) # listenin içinde kaç tane sayı var yazar.
print(harfler.count("b")) # listenin içinde kaç tane harf var yazar.

index = sayilar.index(3) # bu şekilde deger hangi sırada bulabilirz.
print(index)

sayilar.clear() # bu şekilde listedeki bütün karekterleri silersiniz.







