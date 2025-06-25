# Python file detection

import os

# relative file path
file_path = "file_detection/test.txt"

if os.path.exists(file_path): # returns boolean of T/F if file exist
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory (folder)")
else:
    print("That location doesn't exist")

# absolute file path
# get exact location on your computer of file. 
    #  Ex. C:/Users/HP/Desktop/test.txt