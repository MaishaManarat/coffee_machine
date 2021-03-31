from data import menu
from data import resources
from art import logo

import json  # to use zip

from os import system, name
from time import sleep


# define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def play():
    print(logo)
    print("Price Chart:")
    print("Espresso = 15 BDT\nLatte = 25 BDT\nCappuccino = 30 BDT")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    replay(choice)


def bill(price, choice):
    print("please insert coins.")
    five = int(input("How many five taka coins: "))
    two = int(input("How many two taka coins: "))
    one = int(input("How many one taka coins: "))

    total = (one * 1) + (two * 2) + (five * 5)
    if total >= price:
        back = total - price
        print(f"here is your change: {back}")
        print(f"Enjoy your {choice}")
        return True
    else:
        print("Not enough money. Money refunded")
        return False


def check(contents):
    okay = True
    # print(contents)
    # print(resources)
    for (x, y) in zip(contents, resources):
        if contents[x] > resources[y]:
            okay = False
            break

    #print(okay)
    if okay is False:
        return 5
    else:
        for (x, y) in zip(contents, resources):
            resources[y] = resources[y] - contents[x]
        return 10


def replay(choice):
    if choice == 'espresso':
        item = menu['espresso']
        contents = item['ingredients']
        price = item['cost']
        if bill(price, choice) is True:
            go = check(contents)
            if go == 5:
                print("Sorry not enough ingredients")
                print("Money is refunded")
            new = input("Do you want to order? Type 'yes' or 'no': ")
            if new == 'yes':
                clear()
                play()
            else:
                clear()
                play()
        else:
            new = input("Do you want to order? Type 'yes' or 'no': ")
            if new == 'yes':
                clear()
                play()
            else:
                clear()
                play()

    elif choice == 'latte':
        item = menu['latte']
        contents = item['ingredients']
        price = item['cost']
        if bill(price, choice) is True:
            go = check(contents)
            if go == 5:
                print("Sorry not enough ingredients")
                print("Money is refunded")
            new = input("Do you want to order? Type 'yes' or 'no': ")
            if new == 'yes':
                clear()
                play()
            else:
                clear()
                play()
        else:
            new = input("Do you want to order? Type 'yes' or 'no': ")
            if new == 'yes':
                clear()
                play()
            else:
                clear()
                play()

    elif choice == 'cappuccino':
        item = menu['cappuccino']
        contents = item['ingredients']
        price = item['cost']
        if bill(price, choice) is True:
            go = check(contents)
            if go == 5:
                print("Sorry not enough ingredients")
                print("Money is refunded")
            new = input("Do you want to order? Type 'yes' or 'no': ")
            if new == 'yes':
                clear()
                play()
            else:
                clear()
                play()
        else:
            new = input("Do you want to order? Type 'yes' or 'no': ")
            if new == 'yes':
                clear()
                play()
            else:
                clear()
                play()
    elif choice == 'report':
        print(f"{'water'}: {resources['water']}\n{'milk'}: {resources['milk']}\n{'coffee'}: {resources['coffee']}")
        new = input("Do you want to order? Type 'yes' or 'no': ")
        if new == 'yes':
            clear()
            play()
        else:
            clear()
            play()
    else:
        print("incorrect input. please type again: ")
        clear()
        play()


# print(resources)

play()
