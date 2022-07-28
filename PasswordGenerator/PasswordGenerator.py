import random
import os
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

lenght = int(input("insert lenght: "))
password = ""


for a in range(lenght):
    password+= random.choice(chars)

print("Here is your password: " + password)
print("enjoy.")