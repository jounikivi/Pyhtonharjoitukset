#5.1.14 
# tehtävä
# 1.Assume the days of the week are numbered 0,1,2,3,4,5,6 
# from Sunday to Saturday. Write a function which is given the day number, and it returns the day name (a string).

def main():
    paina = 'Y'
    while paina == 'y':
      x =int(input('Anna numero joka kuvastaa viikonpäivää'))
      print("That's for ", viikonpäivä(x))
      paina = input('haluatta painaa uudestaa? Y/n \n')

def viikonpäivä(numero):
  if numero == 0:
    return 'Sunnuntain'
  elif numero == 1:
    return 'Maanantai'
  elif numero == 2:
    return 'Tiistai'
  elif numero == 3:
    return 'Keskiviikko'
  elif numero == 4:
    return 'Torstai'
  elif numero == 5:
    return 'Perjantai'
  elif numero == 6:
    return 'Lauantai'
  
  else:
    print('Jotain muuta taitaa olla väärä viikonpäivä function')
    print('kun oikea arvo on', numero)

main()