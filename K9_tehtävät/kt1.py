#5.1.14 
# tehtävä
# 1.Assume the days of the week are numeroed 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given the day numero, and it returns the day name (a string).

def main():
    pelaa_uudestaan = "Y"
    while pelaa_uudestaan == "Y":
        x = int(input("Anna numero joka kuvastaa viikonpäivää.\n"))
        print("se on:", viikonpäivä(x))
        pelaa_uudestaan = input("Haluattko pelata uudestaan Y/n \n")

def viikonpäivä(numero):
    if numero == 0:
        return "Sunnuntai"
    elif numero == 1:
        return "Maanantai"
    elif numero == 2:
        return "Tiistai"
    elif numero == 3:
        return "Keskiviikko"
    elif numero == 4:
        return "Torstai"
    elif numero == 5:
        return "Perjantai"
    elif numero == 6:
        return "Lauantain"
    else:
        print("Jotain meni pieleen viikonpäivä function")
        print("kun annettiin oikea arvo ", numero)
    
main()