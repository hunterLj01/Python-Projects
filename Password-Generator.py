#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for letter in range(1, nr_letters+1):
  password += random.choice(letters)
#print(password)
#same for all symbols and numbers
#output would be easy form of passwords

for number in range(1, nr_numbers+1):
  password += random.choice(numbers)
#print(password)

for symbol in range(1, nr_symbols+1):
  password += random.choice(symbols)
print(f"Easy password is :'{password}'")
  
hard_pass=''.join(random.sample(password,len(password)))
# Getting the hard form of password

print(f"Hard Password : '{hard_pass}'")

'''
to get a list back into string use for loop
for char in password_list:
  password +=char
print(f"your password is : {password}")
'''
