#WAP to accept 3 integers from the user and without using any logical operator and cascading of relational operators , find out the greatest number amongst them.

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))
num_3= int(input("Enter third number:"))

greatest_num = max(num_1,num_2,num_3)

print("The greatest number is",greatest_num)