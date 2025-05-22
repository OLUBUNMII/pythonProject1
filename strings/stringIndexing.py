# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0]) #prints the value with the index of 0 which is 1
# print(credit_number[:4]) #prints the values from indexes 0 - 4, the value at index 4 is exclusive.
# print(credit_number[5:9]) #index 5 - 9
# print(credit_number[5:]) #index 5 till the end
# print(credit_number[-1]) #prints first index from the back (last digit)
#print(credit_number[::3]) #prints every 3rd index from 0 till the end starting from 0 (the first index).

last_digits = credit_number[15:]
# last_digits = credit_number[-4:] # it does the same thing as line 13
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] #reverses the string, prints it backwards
print(credit_number)