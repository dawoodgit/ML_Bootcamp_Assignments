#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fName = input("Please enter your first name:")
lName = input("Now enter your last name:")

fName_Rev = fName[::-1]
lName_Rev = lName[::-1]

print("The answer is:",fName_Rev,lName_Rev)