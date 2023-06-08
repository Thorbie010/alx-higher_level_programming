#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total_args = len(sys.argv) - 1
    if total_args < 1:
        print("0 arguments.")
    print(total_args, "arguments:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
