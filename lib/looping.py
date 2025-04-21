#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    # pass
    counter = 10
    while counter > 0:
        print(f"{counter}")
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    # pass
    int_list = [num*num for num in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    # pass
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)