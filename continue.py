#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a while loop program.


def main():
    # This is the function to run while loop.

    loop_counter = 0
    final = 0
    # Input
    user_input_number = input("How many numbers are you going to add:")
    print("")

    # Process & output
    try:
        user_input_number = int(user_input_number)
        if user_input_number > 0:
            while loop_counter < user_input_number:
                inputnumber = input("Enter  integer to add:")
                inputnumber = int(inputnumber)
                if inputnumber < 0:
                    final = final + 0
                    loop_counter = loop_counter + 1
                    continue
                else:
                    while_number = inputnumber
                    final = while_number + final
                    loop_counter = loop_counter + 1
                continue
            print("The total is {}".format(final))
        elif user_input_number < 0:
            print("Sorry, you did not enter a positive integer!")
    except Exception:
        print("You are not type in an integer!")


if __name__ == "__main__":
    main()
