weight = float(input("Enter your weight: "))
unit = input("Enter the unit of your weight (Kg or Lbs): ")

if unit == "Kg":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight converted to Pounds is {round(weight, 1)} {unit}")
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kg"
    print(f"Your weight converted to Kilograms is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not a valid unit.")