"""
daire alani = nr2
daire alani = 2nr
  ** yari çapi verilen bir dairenin alan ve çevresini hesaplayiniz..( n:3.14 )

"""
pi = 3.14

r = float(input("yari çapi: "))
alan = pi * (r ** 2)
çevre = 2 * pi * r

print(alan, çevre)

"""
bir aracin km cinsinden gittigi yol bilgisini mil olarak yazdirniz.
mil = km / 1609344
"""
print("kaç km yol gittiniz")
mesafekm = input()
mesafemil = float (mesafekm) / 1609344
mesafemil = round(mesafemil, 2 )

print(str(mesafekm) + "km = " + str(mesafemil) + " mil, ")








