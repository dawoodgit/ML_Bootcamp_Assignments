#WAP to accept a year from the user and check whether it is a leap year or not.

user_yr = int(input("Enter the year:"))

if user_yr % 400 == 0:
    print(user_yr,"is a leap year.")
elif user_yr % 4 == 0 and user_yr % 100 != 0:
    print(user_yr,"is a leap year.")
else:
    print(user_yr,"is not a leap year.")