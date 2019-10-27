#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This is program adds all the whole numbers up to that number


def main():
    # This is program adds all the whole numbers up to that number

    print("This programs adds your number into itslef ex. (5=5+4+3+2+1=15)")

    number = int(input("Please put in number: "))

    number1 = number

    counter = 0

    total = 0

    while counter != number1:

        number = number + counter

        counter = counter + 1

        total = number

        print("{0}".format(total))

        if counter == number1:

            print("The numbers have been crunched and your final number is {0}"
                  .format(total))


if __name__ == "__main__":
    main()
