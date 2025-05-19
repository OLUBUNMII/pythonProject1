import math

firstSide = float(input("Enter the value for the first side of the traingle: "))
secondSide = float(input("Enter the value for the second side of the traingle: "))

hypotenuse = math.sqrt(pow(firstSide, 2) + pow(secondSide, 2))

print(f"The hypotenuse of your right-angled triangle is: {round(hypotenuse, 2)}cm²")