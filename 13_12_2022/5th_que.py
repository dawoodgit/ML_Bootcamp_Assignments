#Write a program that asks the user to input 2 integers and adds them . Accept both the numbers in a single line only.

opening = "Hi. please enter two numbers below that should be seperated by a comma e.g. '12,45' or 98,34 etc.\n"

a = input(opening)
lst = a.split(",")
first_num = int(lst[0])
second_num = int(lst[1])
num_sum = first_num + second_num
print("The sum of these number is:",num_sum)
