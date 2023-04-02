import random


def roll_dice(num1, num2):
    return random.randrange(num1, num2+1)


def print_menu():
    print("Welcome to Dice Roll Simulator.")
    print("Please select an option from below: ")
    print("\t1. D6 (Six Sides)")
    print("\t2. D8 (Eight Sides)")
    print("\t3. D10 (Ten Sides)")
    print("\t4. D12 (Twelve Sides)")
    print("\t5. D20 (Twenty Sides)")
    print("\t6. Show Menu")
    print("\t0. Quit")


print_menu()
while True:
    try:
        result = int(input())
        if result == 1:
            print("D6 = " + str(roll_dice(1, 6)))
        elif result == 2:
            print("D8 = " + str(roll_dice(1, 8)))
        elif result == 3:
            print("D10 = " + str(roll_dice(1, 10)))
        elif result == 4:
            print("D12 = " + str(roll_dice(1, 12)))
        elif result == 5:
            print("D20 = " + str(roll_dice(1, 20)))
        elif result == 6:
            print_menu()
        elif result == 0:
            quit(0)
        else:
            print("Command not found, press 6. to show menu")
    except ValueError:
        print("Please enter a number")