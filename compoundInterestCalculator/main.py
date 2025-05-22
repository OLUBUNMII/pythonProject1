# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Please enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than Zero")
    else:
        break

while True:
    rate = float(input("Please enter the interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than Zero")
    else:
        break

while True:
    time = int(input("Please enter time until maturity date: "))
    if time <= 0:
        print("Time cannot be less than Zero")
    else:
        break

compoundInterest = principle * pow((1 + rate / 100), time)
print(f"Your balance after {time} year/s is: ${compoundInterest:.2f}")