#Nicklas' password generator
import random

#Variables
letters = "abcdefghijklmnopqrstuvwxyz!@%&?#1234567890"
pass_length = random.randrange(15, 20)

#The generator itself
def generator():
    password = ""
    for i in range(0, pass_length):
        ran_index = random.randint(0, len(letters) - 1)
        password += letters[ran_index]
    return password

generator()
print("length of password:", pass_length, "letters")
print(generator()) #