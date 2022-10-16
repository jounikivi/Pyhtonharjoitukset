#5.1.14 
# tehtävä
# 10. Write a function find_hypot which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)


def find_hypot():
    a = int(input("Syötä a sivun pituus: "))
    b = int(input("Syötä b sivun pituus: "))
    c = (a**2 + b**2)**0.5

    print("Tämän kolmion hypotenuse pituus on:", c)

find_hypot()
