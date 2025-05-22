# validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")



if len(username) > 12:
    print("Username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif username.isalpha () == False:
# elif not username.isalpha(): ---------------- Does the same thing as line 14
    print("Username cannot contain numbers")
else:
    print(f"Welcome {username}")