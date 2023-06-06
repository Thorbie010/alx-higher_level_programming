#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tmpnum = number

if number < 0:
    number = -(number)

y = number % 10
if tmpnum < 0:
    number = tmpnum
    y = -(y)

if y > 5:
    print("Last digit of", number, "is", y, "and is greater than 5")
elif y == 0:
    print("Last digit of", number, "is", y, "and is 0")
elif y < 6 and y != 0:
    print("Last digit of", number, "is", y, "and is less than 6 and not 0")
