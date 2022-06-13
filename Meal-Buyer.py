# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #split returns a list thus names is a Python  list
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)

import random

# this is the wrong usage ->i=names.len()
i=len(names) # successfully stored the number of items in that list
print(f"This is number of items: {i} ")

#now to print out the random items out of list
Buyer=random.randint(0,i-1)
print(f"The index chosen for today is : {Buyer}")
print(f"{names[Buyer]} is going to pay today's bill!")
