#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: December 2019
# This program finds the smallest number in a list

import random


def find_min(list_of_numbers):
    # this function finds the smallest number
    smallest_num = 100

    # process
    for counter in list_of_numbers:
        if smallest_num > counter:
            smallest_num = counter

    return smallest_num


def main():
    # this function displays the smallest number

    random_numbers = []
    # output
    print("Let's find the smallest number.")

    # process
    for loop_counter in range(0, 10):
        num = random.randint(1, 100)
        random_numbers.append(num)
    print(random_numbers)

    # call function
    smallest = find_min(random_numbers)

    # output
    print("")
    print("The smallest number from this list is: ", smallest)


if __name__ == "__main__":
    main()
