#Write a program to accept an integer from the user and display the sum of all the numbers from 1 to that number.

num = int(input("Please enter the number: "))

sum_num = int(num*(num+1)/2)

print("The sum is:",sum_num)