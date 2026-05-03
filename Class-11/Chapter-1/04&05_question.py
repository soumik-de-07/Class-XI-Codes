import os

# Select the directory whose content you want to list 
directory_path = 'C:'

# Use os module to list the contents  
content = os.listdir(directory_path)

# list the contents in order 
for items in content:
    print(items)
