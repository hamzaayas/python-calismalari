diller = ['python','C#','java','Javascript','react']

sonuc = diller 
sonuc = type(diller)
sonuc = diller[0]
sonuc = diller[0:3]
sonuc = diller[:4]
sonuc = diller[-1]
sonuc = diller[-4:-1]
# diller[0] = "html" # kodladıgımızda 'python' kelimesi 'html' olarak degişir.
# print(diller)

sonuc = len(diller) # bu şekilde listede kac parça ögrenebiliriz.
print(sonuc)

sonuc = diller + ["merhaba","degmez"] # bu şekilde  listeye ekleme yapabilirsiniz.
print(sonuc)

# if blogu ==) koşul ifadeleri.
if "python" in diller: # bu şekilde yazarsanız,dillerin içinde 'python'varmıdır sorusuna cevap alırsınız.
   print("evet vardir") # evet vardır cevabı yazdırılır.

# döngüler konusu
for x in diller: # bu şekilde sırayla 'diller' listesi aşagıya dogru yazdırılır.
   print(x)

del diller[0] # diller listesindeki [0]'degeri siler.
print(diller)











