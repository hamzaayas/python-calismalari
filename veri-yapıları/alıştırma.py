#mesaj = "kadgasljdgajldgadgadgiasdgkjgdkagdaskgdklakajd"
#print(len(mesaj))
###########################################################
#mesaj = 9,123456789
#print(round(9,123456789,))
############################################################
#adim = 'hamza'
#soyAdim = 'ayas'
#yasim = 22
#print("my name is {} {}. I'm {} years old.".format(adim,soyAdim,yasim))
############################################################
#number = 200 / 700
#print(f"benim adim {adim} soyadim {soyAdim} ve yaşim {yasim}")
############################################################
#mesaj = 'asla fenerbahce... şampion '
#sonuc = 'asla'.strip()
#print(sonuc)
########################################################
#alikoc = 'bu sene hakemler cok hata yapiyor'
#dursunÖzbek = 'bu sene hakemler cok hata yapiyor'.replace('yapiyor','yapmiyor')
#alikoc = alikoc.upper()
#print(alikoc)
##############################################################################
'''$
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''
players = {}

id = input('oyuncu id: ')
Name = input('oyuncu ad: ')
yearOfBirth = input('oyuncu dogum yili: ')
nationality = input('ülke: ')
current_Team = input('oyuncu takimi: ')
history = input('oynadigi yerler: ')

players.update({
  id: {   
     "name": Name,
     "yearOfBirth": yearOfBirth,
     "nationality": nationality,
     "current_Team": current_Team,
     "history": history.split(',')
 }
})

id = input('oyuncu id: ')
Name = input('oyuncu ad: ')
yearOfBirth = input('oyuncu dogum yili: ')
nationality = input('ülke: ')
current_Team = input('oyuncu takimi: ')
history = input('oynadigi yerler: ')

players.update({
  id: {   
     "name": Name,
     "yearOfBirth": yearOfBirth,
     "nationality": nationality,
     "current_Team": current_Team,
     "history": history.split(',')
 }
})
#print(players)















