ad = 'Dzeko'
soyad = 'Edin'
yas = ' 38 '

msj = ' benim adim ' + ad + ' ve soyadim ' + soyad + ' yaşim ise ' + yas 

print(len(msj)) # len karekteri cümlediki harflerı saymaya yardımcı olur.

print(msj [4]) # i
print(msj[-8]) # m
print(msj[15]) # k

print(msj[0:5])  # beni sonucu alırız.
print(msj[7:20]) # adım dzeko ve sonucu alırız.
print(msj[1:29]) # benim adım dzeko ve soyadim cevabını alırız.
print(msj[:17])  # en başından alır ve 17 e kadar ilerler.
print(msj[1:])   # 1.harfden alır ve kelimenın sonuna kadar ilerler..
print(msj[-12:-1]) # sag taraftan başlar. ve sonuc: yaşim ise 38
print(msj[0:40:2]) # bu şekilde yaparsanız adım mesafesı koymus olursunuz.
print(msj[::1])    # baştan başlar ve sona kadar gider adım sayısı 1,1 olur.

