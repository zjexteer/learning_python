## this is a simple program to generate password depending on user input ### 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for x in range (0,nr_numbers): # for loop in range of number user entered for example 4 will be from 0 to 4 
  x=random.choice(numbers) # it will loop 4 times inside 0 to 9 
  password+=x # add the number to the list 

for y in range (0,nr_symbols):
  y=random.choice(symbols)
  password+=y

for z in range (0,nr_letters):
  z=random.choice(letters)
  password+=z
## print(password) ##
random.shuffle(password) ## shuffle the password 
## print(password) ## 

generate_password=""  # we creating a new loop to change the list to string 
for a in password:
   generate_password+=a
   
print(generate_password)

