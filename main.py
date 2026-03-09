import random
import string

print("==== PASSWORD GENERATOR ====")

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Please enter a valid number")
    exit()

if length < 4:
    print("Password length should be at least 4")
    exit()

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)