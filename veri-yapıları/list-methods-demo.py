isimler = ['ada','yigit','hasan','beril']
yaslar = [1998, 2000, 1998, 1987]

#1 "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")
print(isimler)
#2 "sena" degerini listenin başına ekleyiniz.
isimler.insert(0,"sena")
print(isimler)
#3 "yigit" ismini listeden kaldırınız.
isimler.remove("yigit")
print(isimler)
#4 "yigit" isminin indexi nedir.
index = isimler.index("beril")
print(index)
#5 "beril" listenin bir elemanımıdır.
if "beril" in isimler:
    print("evet elemanidir")
#6 liste elemanlarını ters çevirin.
isimler.reverse()
print(isimler)
#7 liste elemanlarını alfabetik olarak sıralayınız.
isimler.sort()
print(isimler)
#8 years listesini rakamsal olarak sıralayınız.
yaslar.sort()
print(yaslar)
#9 str = "iphone x","iphone xr" karekter dizisini listeye çeviriniz.
s = "iphone x","iphone xr"
sonuc = s.split(',')
print(sonuc)
#10 yaslar dizisinin en büyük ve en kücük elemanı nedir ?
print(min(yaslar))
print(max(yaslar))
#11 yaşlar dizisinde kaç tane 1998 degeri vardır.
print(yaslar.count(1998))

#12 yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()

#13 kullanıcıdan aldıgımı 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka: ")
markalar.append(marka)


marka = input("marka: ")
markalar.append(marka)


marka = input("marka: ")
markalar.append(marka)   

# print(markalar)















