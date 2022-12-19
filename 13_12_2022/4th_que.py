#Write a program that asks the user to enter his/her name and age. Print out a message , displaying the user’s name along with the year in which they will turn 100 years old.

your_name = input("Please enter your name:")
your_age = input("Now, your age plaese:")

your_year = 2022 + 100 - int(your_age)

print("Dear {name}, your age will 100 in the year of {year}".format(name = your_name , year = your_year))