# default arguments = A default value for certain parameters. 
# Default is used when that argument is omitted.
# It makes your functions more flexible, reduces number of arguments
# Types of arguments include: Positional, defualt, keyword, arbitary

import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10)