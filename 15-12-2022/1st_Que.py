#WAP to accept an integer from the user and check whether it is an even or odd.

num = int(input("Enter the number:"))

if num % 2 == 0 :
    print(num,'is an even number.')
else:
    print(num,'is an odd number.')