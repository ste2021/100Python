# Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

def input_function():

    input1 = input("What is your Name?")
    print_len = len(input1)
    if len(input1) > 0:
        print(str(print_len))
    else:
        print("Enter a valid Name")
        input_function()

input_function()