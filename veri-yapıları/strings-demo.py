website ="http://www.sadikturan.com"
kursAdi ="python dersleri: Sifirdan ileri seviye python programlama."

# kursAdi' karekter dizisnde kaç karekter bulunmaktatır.?
sonuc = len(kursAdi)
print(sonuc)

# website içinden www karekterlerını alın.
sonuc = website
print(website[7:10])

# website içinden com karekterlerını alın.
sonuc = website
print(website[22:26])


# kursAdi içinden ilk 15 ve son 15 karekterlerını alın.
sonuc = kursAdi
print(kursAdi[0:15])


# kursAdi ifadesındeki karekterlerı tersten yazdırın.
sonuc = kursAdi
print(kursAdi[::-1])

# 'hello word' kelimesındeki w buyuk (W) olarak yazdırınız.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

# 'abc' yan yana 3 defa yazdırın.
sonuc = 'abc'
print('abc ' *3)

name, surname, age, job = 'hamza', 'ayas', 22, 'futbolcu'

# yukarıda verilen degişkenler ile ekrana aşagıdaki ifadeyi yazdırınız.
#              "benım adım hamza ayas yaşım 22 ve meslegim futbolcu."

# ilk seçenek..
print(f"benim adim {name} {surname} yaşim {age} ve meslegim {job} ") 

# ikinci seçenek...
sonuc = "benim adim " + name + " " + surname + ", yaşim " + str(age) + " ve meslegim " + job +"."
# üçüncü seçenek..
sonuc = "benim adim {0} {1} yaşim {2} ve meslegim {3}".format(name,surname,age,job)

print(sonuc)

