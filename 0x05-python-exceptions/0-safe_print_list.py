#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        iterator = iter(my_list)

        while count < x:
            element = next(iterator, None)
            if element is None:
                break
            print(element, end="")
            count += 1

    except TypeError:
        print("Error: Invalid list!")

    print()

    return count
