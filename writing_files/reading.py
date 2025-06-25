# Pything reading files (.txt, .json, .csv)

'''
# Step I
# .txt
file_path = "writing_files/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

    
# Step II
# .json

import json

file_path = "writing_files/output3.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

'''

# Step III
# .csv

import csv

file_path = "writing_files/output4.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
