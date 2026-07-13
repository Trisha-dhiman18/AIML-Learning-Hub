import os

# Specify the directory path
directory = "."

# Get and print the contents of the directory
contents = os.listdir(directory)

print("Contents of the directory:")
for item in contents:
    print(item)