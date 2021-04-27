#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This is the "calculate area and perimeter of a 15mm radius circle" program

import math


def main():
    print("What is the area and perimeter of a 15mm radius circle?")
    print()
    print("Area: {}mm²".format(math.pi * 15 ** 2))
    print("Perimeter: {}mm".format(math.pi * 2 * 15))


if __name__ == "__main__":
    main()
