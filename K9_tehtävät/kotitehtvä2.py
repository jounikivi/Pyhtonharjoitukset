#5.1.14 
# tehtävä
#You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a Wednesday). 
# You return home after 137 sleeps. Write a general version of the program which asks for the starting day number, and the 
# length of your stay, and it will tell you the name of day of the week you will return on.

viikonpäivät = {0: 'Sunnuntai', 1: 'Maanantai', 2: 'Tiistai', 3: 'Keskiviikko', 4: 'Torstain', 5: 'Perjantain', 6: 'Lauantain'}

print("anna minulle numero 0-6, joka edustaa päivää, jona menit ", \
       "määränpääsi, jossa 0 edustaa sunnuntaita, 1 edustaa Maantaita \n")

x = int(input('Mikä on numero? \n'))
print("Se on {}.".format(viikonpäivät[x]))

y = int(input('Kuinka monta yötä nukut määränpäässäsi \n'))

z = (x + y) % 7

print("Lähdet Kohteesta {}.".format(viikonpäivät[z]))