P = 10000
n = 12
r = .08

print("How many years would you like to let your beautiful $10,000")
t = int(input("investment grow at a rate of 8%, compounded monthly? \n"))

# Executes the formula shown in the exercise.
temp1 = 1 + r / n
A = P * temp1 ** (n * t)

final_statement = "You'll wind up with ${:,} after {} years.".format(
 round(A, 2), t
)

print(final_statement)