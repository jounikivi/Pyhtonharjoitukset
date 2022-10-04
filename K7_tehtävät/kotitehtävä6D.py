#Kohdan 3.8 tehtävä 5 d
#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# D. Print the product of all the numbers in the list. (product means all multiplied together)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 1
for x in xs:
    total = total * x
print(total)