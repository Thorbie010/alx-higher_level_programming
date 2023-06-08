#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div

if __name__ == "__main__":
    a = 10
    b = 5
    result_1 = add(a, b)
    result_2 = sub(a, b)
    result_3 = mul(a, b)
    result_4 = div(a, b)
    print("{} + {} = {}".format(a, b, result_1))
    print("{} - {} = {}".format(a, b, result_2))
    print("{} * {} = {}".format(a, b, result_3))
    print("{} / {} = {}".format(a, b, result_4))
