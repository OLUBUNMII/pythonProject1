menu = {"pizza": 3.00,
        "soda": 3.00,
        "hotdog": 4.99,
        "water": 2.99,
        "chocolate": 4.00,
        "fries": 3.59,
        "chips": 2.00}

cart = []
Total = 0

print("---------- MENU ----------")
# print(menu)
for item , price in menu.items():
        print(f"{item:10}: ${price:.2f}")
print()

while True:
        food = input("Select an item (q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)

for food in cart:
        Total += menu.get(food)
        print(food, end=" ")

print()
print(f"Your total is ${Total:.2f}")
    # if item in menu.:
    #     input = "What would you like to buy, (Press q to quit): ".lower
    #     menu.append[cart]
    # elif item not in menu.items:
    #      print("Item is not on the menu")