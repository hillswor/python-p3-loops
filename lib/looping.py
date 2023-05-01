#!/usr/bin/env python3


def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    squared_integers = [integer * integer for integer in int_list]
    return squared_integers


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


for i in range(10):
    print("Looping!")
    print(f"i is: {i}")
