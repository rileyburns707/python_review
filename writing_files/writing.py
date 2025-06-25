# Pything writing files (.txt, .json, .csv)
    
'''
# Step I.
# txt = plain text

txt_data = "I like pizza!"

file_path = "writing_files/output.txt"    # relative file path

# "with" statement automatically closes files
# "open" function returns the file object. 
    #  first param = file path. 
    # second param = mode.  
        # "w" write
        # "x" also writes if file doesn't exist. If it does it will be an error
        # "a" appends a file
        # "r" reads a file


with open(file=file_path, mode="w") as file:  # creates file. 
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

try: 
    with open(file=file_path, mode="x") as file: 
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")


try: 
    with open(file=file_path, mode="a") as file: 
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

# Step II.

# with a collection
employees = ["Plato", "Socrates", "Mill"]

file_path = "writing_files/output2.txt"

try: 
    with open(file_path, "w") as file: 
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")


# Step III.
# outputting json file
    # json files are made of key:value pairs
import json

employee = {
    "name": "Socrates",
    "age": 70,
    "job": "teacher"
}

file_path = "writing_files/output3.json"

try: 
    with open(file_path, "w") as file: 
        json.dump(employee, file, indent=4) # dump will convert dictionary to json string. indent is just formatting
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")
'''

# Step IV
# going to use .csv files
# csv = comma separated values. Common with spreadsheet of data
import csv
employees = [["Name", "Age", "Job"], 
              ["Socrates", 70, "Teacher"], 
              ["Plato", 80, "Student"],
              ["Mills", 67, "Economist"]]

file_path = "writing_files/output4.csv"

try: 
    with open(file_path, "w") as file: 
        writer = csv.writer(file)   # writer is an object, it provides methods for writing data to a csv file
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")