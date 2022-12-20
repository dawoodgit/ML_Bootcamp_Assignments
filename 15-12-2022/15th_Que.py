#Write a program to accept an integer from the user and display all the numbers from 1 to that number. Repeat the process until the user enters 0.


while True:
    num = int(input("Enter a number:"))
    if num == 0:
        print("Thanks!")
        break
    for i in range(1, num+1):
        print(i)