website ="http://www.sadikturan.com"
kursAdi ="Python dersleri: Sifirdan ileri seviye Python programlama."

#1 ' Hello word ' karekter dizisinin baş ve sondaki boşluk karekterlerini silin. 
sonuc = ' Hello world '.strip()
print(sonuc)
#2 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki tüm karekterleri silin.
sonuc = website.strip("http://www..com")
print(sonuc)
#3 'kursAdi' karekter dizisinin tüm karekterlerini kücük harf yapın.
sonuc = kursAdi.lower()
print(sonuc)
#4 website içinde kaç tane a karekteri vardır ? count('a'))
sonuc = website.count('a')
print(sonuc)
#5 website 'www' ile başlıyıp 'com' ile bitiyormu ? 
sonuc = website.startswith('www')
sonuc = website.endswith('.com')
print(sonuc)
#6 website içinde '.com' ifadesi varmı 
sonuc = website.find('.com',0,10) # .index() kodu ile de yapabilirz
sonuc = website.find('python')
sonuc = kursAdi.rfind('Python')
sonuc = kursAdi.index('Python')
print(sonuc)
#7 'kursAdi' içindeki karekterlerin hepsi alfabetikmi ? (isalpha,isdigit)
sonuc = kursAdi.isalpha() # (isalpha) kelime alfabetik mı diye sorar 
sonuc = "1234".isdigit() # (isdigit) kelimeler sayımı diye sorar
print(sonuc)
#8 'Contents' ifadesini satırda 50 karekter içine yerleştirip sag ve soluna * ekleyınız.
sonuc ='contents'.center(50,'*')
sonuc ='contents'.ljust(50,'*')
sonuc ='contents'.rjust(50,'*')
print(sonuc)
#9 'kursAdi' karekter dizisindeki tüm boşluk karekterlerini '-' ile degiştirin.
sonuc = kursAdi.replace(' ','-')
print(sonuc)
#10 'Hello world' karekter dizisin 'world' ifadesini 'there' olarak degiştirin.
sonuc = 'Hello World'.replace('World','There')
print(sonuc)
#11 'kursAdi' karekter dizisini boşluk karekterlerinden ayırın.
sonuc = kursAdi.split() 
print(sonuc)


