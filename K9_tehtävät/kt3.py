#5.1.14 
# tehtävä
# 6.Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme:

def grade(mark):
    mark_scheme = [(75, "First"), (70, "Upper Second"), (60, "Second"), (50, "Third"), (45, "F1 Supp"), (40, "FS")]
    for threshold in mark_scheme:
        if mark >= threshold[0]:
            return threshold[1]
    return "F3"
xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for x in xs:
    print(x, grade(x))