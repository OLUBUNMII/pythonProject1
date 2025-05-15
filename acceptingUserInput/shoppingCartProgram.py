item = str(input("What item would you like to buy: "))
price = float(input("How much is it: "))
quantity = int(input ("How many would you like to buy: "))
total = (price * quantity)

print(f"You ordered {quantity} {item} at ${price} a piece.")
print(f"Your total fee is ${total}")