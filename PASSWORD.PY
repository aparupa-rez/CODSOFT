#Importing random and strng library
import random
import string

#Taking user Input to Specify the Length of The Characters
len=int(input("Enter the Length of the Password:"))

#assigning the digits,letters, and symbols
chars=string.ascii_letters
chars+=string.digits
chars+=string.punctuation

#Intialising the password
password=""

#Initialising for loop for adding characters
for i in range(len):
    nxt_char=random.choice(chars)
    password+=nxt_char

    #Display the password
    print("Your New password is:", password)