"""
Generate random password
Password's length will be of 12
Password might contain :- A-Z, a-z, 0-9, punctuators (/,\, %, -, ?, ! etc )
Password should contain at least one lowercase alphabet, upper alphabet, digit, and punctuation
"""

import random
import string

while True:
    # create a string containing A-Z, a-z, 0-9, punctuators
    pwdStr = string.ascii_letters + string.digits + string.punctuation

    # Initialize the length of password
    pwdLen = 12

    # Initialize the password string
    pwd = ""
    for i in range(pwdLen):
        pwd += random.choice(pwdStr)

    # Generate password using list comprehension
    # pwd = "".join([random.choice(pwdStr) for i in range(pwdLen)])

    # If password contains at least one lowercase alphabet, upper alphabet, digit, and punctuation
    if (any(char in string.ascii_lowercase for char in pwd) and any(char in string.ascii_uppercase for char in pwd)
            and any(char in string.digits for char in pwd) and any(char in string.punctuation for char in pwd)):
        break

print("The password generated is:", pwd)
