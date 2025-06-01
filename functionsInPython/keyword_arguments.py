# keyword arguments = an argument preceded by an identifier
# It helps with readability
# The order of arguments doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="Olubunmi", first="Oluwanifesimi")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = f"Your phone number is: {get_phone(country=234, area=123, first=9744, last=272)}"

print(phone_num)