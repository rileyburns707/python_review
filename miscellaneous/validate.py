username = input("Enter a user name: ")

if len(username) > 12:
    print("Username must be less than 12 characters.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")
elif username.isalpha() == False:
    print("Username must only contain letters.")
else:
    print(f"Welcome {username}!")