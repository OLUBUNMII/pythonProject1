# Set = {} unordered and immutable, but Add/remove OK. No Duplicates.

fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

fruits.add("pineapple")
fruits.remove("apple")

print(fruits)