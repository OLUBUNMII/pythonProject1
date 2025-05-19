temperature = float(input("Enter temperature: "))
unit = input("Is it Fahrenheite or Celsius, Enter 'F or C': ").strip().lower()

if unit == "f":
    temperature = round((temperature - 32) * 5 / 9, 1)
    unit = "°C"
    print(f"The temperature converted to celsius is: {round(temperature, 1)} {unit}")
elif unit == "c":
    temperature = round((temperature * 9) / 5 + 32, 1)
    unit = "°F"
    print(f"The temperature converted to fahrenheite is {round(temperature, 1)} {unit}")
else: 
    print(f"The unit {unit} is invalid")