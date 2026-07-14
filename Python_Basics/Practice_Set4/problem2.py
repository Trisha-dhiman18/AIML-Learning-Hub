# Write a program to accept marks of 6 students and display them in a sorted manner.
n = 6
marks = []  # Initialize an empty list to store the marks
for i in range(1, n+1):
    mark = int(input("Enter the marks of student {}: ".format(i)))
    marks.append(mark)   # append the marks entered by the user
marks.sort()    # Sort the list of marks in ascending order
print("The marks of the students in sorted manner are:", marks)