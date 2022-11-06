# This Python project gives a random password for users
# This project contains string and random module
# This project is created using function and extend() and some more variables.......

import string
import random

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = int(input("Enter the password length:- "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)

gen()
