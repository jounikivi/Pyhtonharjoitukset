#Kohdan 3.8 tehtävä 5 c
#Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# C.Write a loop that adds all the numbers from the list into a variable called total. You should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed.

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
for x in xs:
  total = total * x
print(total)