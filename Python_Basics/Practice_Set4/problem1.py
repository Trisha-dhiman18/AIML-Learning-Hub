# Write a program to store seven fruits in a list entered by the user
n = 6
fruits = []     # Initialize an empty list to store the fruits
for i in range(1, n+1):   
    fruit = input("Enter the name of fruit: ")   # Prompt the user to enter the name of a fruit
    fruits.append(fruit)   # Add the entered fruit to the list
print("The names of the fruits are:", fruits)   # Print the list of fruits entered by the user