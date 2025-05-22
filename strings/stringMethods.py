name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

#result = len(name) #length of the string
# result = name.find("n") #first occurence of the letter "n" in the string, it is case sensitive
# result = name.rfind("n") #last occurence of the letter "N" in the string, it is case sensitive
# name = name.capitalize() #capitalizes first character
# name = name.upper() #capitalizes entire string
# name = name.lower() #tranforms string to lowercase
# result = name.isdigit() #boolean that returns true or false if the string contains only digits, a space  isn't a digit
result = name.isalpha() #boolean that returns true or false if the string contains only alphabets, a space isn't an alphabet
# result = phone_number.count("-") #counts the number of specified character in a string, in this case it will count the number of "dashes" in your phone number
# result = phone_number.replace("-", " ") #replaces characters ina  string, in this case it replaces the dashes with spaces

print(result)

#print(help(str)) #PRINTS A COMPREHENSIVE LIST OF ALL THE STRING METHODS AVAILABLE