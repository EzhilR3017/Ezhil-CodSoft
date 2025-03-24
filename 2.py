import random
import string

print("Welcome to the password generator!")

random_letters = []
random_symbols = []
random_digits = []

letter_no = int(input("How many letters would you like in your password? "))
for _ in range(letter_no):
    random_letters.append(random.choice(string.ascii_letters))

symbol_no = int(input("How many symbols would you like? "))
for _ in range(symbol_no): 
    random_symbols.append(random.choice(string.punctuation))

digit_no = int(input("How many digits would you like? "))
for _ in range(digit_no): 
    random_digits.append(str(random.randint(0, 9)))

password_list = random_letters + random_symbols + random_digits
random.shuffle(password_list)
password = "".join(password_list)

print("Your password is:", password)
