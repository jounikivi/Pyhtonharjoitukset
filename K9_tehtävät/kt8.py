#5.1.14 
# tehtävä
# 11. Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

def is_rightangled():
    while True:
        a = int(input("Syötä a sivun pituus: "))
        b = int(input("Syötä a sivun pituus: "))
        c = int(input("Syötä a sivun pituuse: "))
        if c == (a**2 + b**2)**0.5 or b == (a**2 + c**2)**0.5 or a == (c**2 + b**2)**0.5:
            print("Tämä on suorakulmainen kolmio")
            break
        else:
            print("tämä ei ole suorakulmainen kolmio. Yritä uudelleen")

is_rightangled()