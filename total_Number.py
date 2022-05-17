#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on may 2022
# This program format the mailing adress

import random


def main():
    # this function uses a list

    list_of_numbers = []
    total = 0

    # input
    for counter in range(0, 10):
        random_number = random.randint(1, 100)  # a number between 1-100
        total = total + random_number
        list_of_numbers.append(random_number)
        print("The random number is : {0}".format(random_number))
        counter += 1

    average = total / (len(list_of_numbers))
    rounded_average = round(average, 2)
    print("\nThe average is {0}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
