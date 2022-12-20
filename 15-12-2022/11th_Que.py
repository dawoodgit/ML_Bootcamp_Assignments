#Write a program to accept an integer from the user and calculate its factorial.

num = int(input("Please enter the number: "))

fact = 1

for i in range(1,num+1):
    fact = fact*i

print("The factorial is:",fact)