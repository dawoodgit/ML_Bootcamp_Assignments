#WAP to accept a character from the user and check whether it is a capital letter or small letter or a digit or some special symbol.

my_char = input("Please enter any single character:")

if "a" <= my_char <= "z":
    print(my_char,"is a small letter.")
elif "A" <= my_char <= "Z":
    print(my_char,"is a capital letter.")
elif my_char in "0123456789":
    print(my_char,"is a digit.")
else:
    print(my_char,"is a special character.")