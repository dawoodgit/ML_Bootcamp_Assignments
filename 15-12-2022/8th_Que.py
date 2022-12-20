#Write a program to continuously accept integers from the user until the user types 0 and as soon as 0 is entered display sum of all the nos entered before 0.
print("Please enter the numbers below:")

sum = 0

while True:
    a = int(input())
    if a == 0:
        break

    elif a < 0:
        continue

    else:
        sum = sum + a

print("The sum of all the numbers is",sum)
    