import random

# Display welcome message
print("Welcome to the Py Password Generator!")

# Characters used to generate the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', 'A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [ '!', '#', '$', '%', '&', '(', ')', '*', '+']

# Ask the user how many characters of each type they want
nr_letters = int(input("How many letters would you like in your password? \n "))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))




# Create an empty list to store password characters
password_list = []
password = ""

# Add random letters to the password
for letter in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password
for symbol in range(nr_symbols):
     password_list.append(random.choice(symbols))

# Add random numbers to the password
for number in range(nr_numbers):
     password_list.append(random.choice(numbers))

# Shuffle the characters so their order is random
random.shuffle(password_list)

# Convert the list of characters into a single string
for char in password_list:
    password += char

# Display the generated password
print(f"Your password is: {password}")

input("\nPress the enter key to exit.")