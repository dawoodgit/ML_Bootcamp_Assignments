#Write a program using a for loop to accept a string from the user and display it vertically but don’t display the vowels in it.

str = input("Please enter something:")

for i in str:
    if i not in "aeiouAEIOU":
        print(i)