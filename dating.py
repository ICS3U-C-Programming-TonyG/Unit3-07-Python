#!/usr/bin/env python3

# Created By: Tony G

# Date: 2025-03-31

# Dating program (COMPOUND BOOL EXPRESSIONS)


def main():
    # Greeting message and user input
    print("Hello, This program will tell you if you are worthy of my grandchildren.")

    # Try catch
    try:
        # determines whether the person is rich or not
        user_input = input("Are you rich (y/n): ")
        if user_input == "y" or user_input == "Y":
            rich = True
        elif user_input == "n" or user_input == "N":
            rich = False
        else:
            print("please input y or n")

        # Determines whether the person is handsome or not
        user_input2 = input("Are you handsome (y/n): ")
        if user_input2 == "y" or user_input2 == "Y":
            handsome = True
        elif user_input2 == "n" or user_input2 == "N":
            handsome = False
        else:
            print("please input y or n")

        # Determines whether the person can date my grandchild
        if rich or handsome:
            print("You can date my grandchild")
        else:
            print("You cannot date my grandchild")

    except ValueError:
        print("Invalid input. Please enter 'y' or 'n' only.")


if __name__ == "__main__":
    main()
