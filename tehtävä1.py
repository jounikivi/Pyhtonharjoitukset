P = 10000
n = 12
r = .08

print("kuinka montta vuotta")
t = int(input("\n"))

# Executes the formula shown in the exercise.
temp1 = 1 + r / n
A = P * temp1 ** (n * t)

lopputulos = "{:,} after {} years.".format(
 round(A, 2), t
)

print(lopputulos)