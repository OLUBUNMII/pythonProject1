#conditional expression = A one-line shortcut for the if-else statemnet (ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y

# num = -5

# print("Positive" if num > 0 else "Negative")

num = 10
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

result = "Even" if num % 2 == 0 else "Odd"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(max_num)