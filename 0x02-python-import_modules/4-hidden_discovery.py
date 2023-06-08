#!/usr/bin/python3
import sys
import hidden_4 as hid

if __name__ == "__main__":
    module_names = dir(hid)

    filtered_names = [name for name in hid if not name.startswith('__')]

    sorted_names = sorted(filtered_names)

    for name in sorted_names:
        print(name)
