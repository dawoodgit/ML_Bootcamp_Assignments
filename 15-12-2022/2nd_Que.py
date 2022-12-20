#WAP to accept a character from the user and check whether it is a capital letter or small letter. Assume user will input only alphabets.

my_char = input("Please enter any single alphabet:")

if my_char == my_char.lower() :
    print(my_char,"is a small letter.")
else:
    print(my_char,"is a capital letter.")

#Assuming that the user would input a single alphabet only, otherwise would have used code like "a">my_char>"z"