# A function is  a block of reusable code
# Place () after the function name to invoke it.


def happy_birthday(name):
    print(f"Happy birthday to {name}!")


happy_birthday("Nife")
happy_birthday("Toni")
happy_birthday("Pamilerin")


# return statement is used to end a function abd send the result back to the caller.

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

# Positional Argument

full_name = create_name("oluwanifesimi", "olubunmi")

print(full_name)