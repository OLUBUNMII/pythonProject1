# while loop = execute some code WHILE some condition remains true

# name = input ("Enter your name: ")

# while name == "":
#     print("Name cannot be blank")
#     name = input ("Enter your name: ")
# else:
#     print(f"Welcome {name}")


# food = input("Enter a food you like (Press q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food that you like (press q to quit): ")

# print("BYE")


num = int(input("Enter number between 1 -10: "))

while num < 1 or num > 10 :
    print(f"{num} is not a valid number")
    num = int(input("Please enter number between 1 -10: "))
else: 
    print(f"Your number is {num}")