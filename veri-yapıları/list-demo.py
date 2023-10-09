
#1 "samsung s5,samsung s6,samsung s7,samsung s8" elamanlarına sahip bir liste oluşturun.
telefonlar = ['samsung s5','samsung s6','samsung s7','samsung s8']
#2 liste kaç elamanlıdır ? 
sonuc =len(telefonlar) # cevabı bu şekilde 4 olarak alırız.

#3 listenın ilk ve son elamnı nedir.
sonuc = telefonlar[1],telefonlar[-1] # bu şekilde bulabilirz.

#4 'samsung s5' degerini 'samsung s9'ile degiştirin.
telefonlar[0]='samsung s9'# bu şekilde 'samsung s5' degerini degiştirebilirsiniz.

#5 'samsuns s6' listesinin bir elamanı mıdır ?
# if 'samsung s6' in telefonlar: # bu şekilde cevabı alırsınız.
         # print('evet listenin bir elemanidir')

#6 listenın -3 indeksindeki deger nedir.
sonuc = telefonlar[-3]
print(sonuc)
#7 listenin ilk 2 elemanını alın.
sonuc = telefonlar[:2]
print(sonuc)
#8 listenın son 2 elemanının yerine 'samsung s9 ve 'samsung s10' degerlerini ekleyin.
telefonlar[-2:] = ['samsung s11','samsung s10'] 
print(telefonlar)
#9 listenin üzerine "iphone x" ve "iphone xr" degerlerini ekleyin.
sonuc = telefonlar + ["iphone x","İphone xr"]
print(sonuc)
#10 listenın son elemanını silin.
del telefonlar[-1]
print(telefonlar)
#11 liste elemanlarını tersten yazdırınız.
sonuc = telefonlar[::-1]
print(sonuc)

#12 aşagıdaki verileri bir liste içinde saklayınız.

    # kullanıcıA: yigit bilgi 2010, (70,60,70)
    # kullanıcıB: sena turan 1999,  (80,80,70)
    # kullanıcıC: ahmet turan 1998, (80,70,90)
ogrenciA: ["yigit","bilgi",2010[70,60,70]]
ogrenciB: ["sena","turan",1999[80,80,70]]
ogrenciC: ["ahmet","turan",1998[80,70,90]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]

for ogrenci in ogrenciler:
    print(ogrenciler)

# lise elemanlarını ekrana yazdırınız.
 # for a in telefonlar:
    # print(a)








