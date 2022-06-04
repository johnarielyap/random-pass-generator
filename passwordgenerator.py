import random
import pyfiglet

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '$', '&', '(', ')', '*', '+', '@', '<', '>', '^', '#', '%']

ascci_banner = pyfiglet.figlet_format("RANDOM PASSWORD GENERATOR")
print(ascci_banner)

s_letters = int(input(f"HOW MANY LETTERS DO YOU WANT?\n"))
s_symbols = int(input(f"HOW MANY SYMBOLS DO YOU WANT?\n"))
s_numbers = int(input(f"HOW MANY NUMBERS DO YOU WANT?\n"))

password = []

for char in range(1, s_letters + 1):
    password += random.choice(letters)
for char in range(1, s_symbols + 1):
    password += random.choice(symbols)
for char in range(1, s_numbers + 1):
    password += random.choice(numbers)

random.shuffle(password)
password_to_show = ""
for char in password:
    password_to_show += char

print(f"GENERATED PASSWORD {password_to_show}")
