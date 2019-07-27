import random
import json
import sys
import os
from operator import add, sub, mul, truediv

# Raise error if colorama isn't installed

try:
    from colorama import Fore, init

    init()
except ImportError:
    print("Can't work without colorama")
    exit()


def command_handler(input_):
    """
    It handels CLI user input.
    """
    # These variables are available across the functions
    global difficulty, score, settings, selected_operator

    # Exits the program
    if input_ in ["exit", "quit", "уволиться"]:
        sys.exit()

    # Saves user settings This includes
    # [score, difficulty level, selected operator]
    elif input_ in ["save", "спасти"]:
        settings = [score, difficulty, selected_operator]
        with open("settings.json", "w") as fd:
            json.dump(settings, fd)
        print(Fore.LIGHTYELLOW_EX + "Save successfull!")

    #   Load user settings from settings.JSON
    elif input_ in ["load", "нагрузка"]:
        try:
            with open("settings.json") as fd:
                settings = json.load(fd)

                score = settings[0]
                difficulty = settings[1]
                selected_operator = settings[2]
            print(Fore.LIGHTYELLOW_EX + "Load successfull!")

        except FileNotFoundError:
            print(Fore.LIGHTYELLOW_EX + "Saved successfully!")

    # Parser for  operator command
    # Usage:
    # <<< operator <operator symbol>
    elif input_.startswith("operator"):
        operator = input_.split(" ")[-1]
        if operator in operators:
            print(Fore.LIGHTYELLOW_EX + "Operator changed to",
                  operator, Fore.WHITE)
            return operator
        print(Fore.LIGHTYELLOW_EX + "Operator doesn't exist" +
              Fore.WHITE)

    # Changes the difficulty of the calculation
    # by changing the upper limit of random number
    # being generated
    elif input_.startswith("limit"):
        try:
            value = int(input_.split(" ")[-1])
            difficulty = value
            print(Fore.LIGHTYELLOW_EX + "Difficulty level changed." +
                  Fore.WHITE)
        except ValueError:
            print(Fore.LIGHTRED_EX + "Incorrect value." + Fore.WHITE)

    # Displays score
    elif input_ in ["score", "Гол"]:
        print('-'*10)
        print(Fore.LIGHTYELLOW_EX + "Score :", score, Fore.WHITE)
        print(Fore.LIGHTYELLOW_EX + "Difficulty :", difficulty, Fore.WHITE)
        print('-'*10)
    return selected_operator


operators = {"+": add, "-": sub, "*": mul, "/": truediv}


selected_operator = "+"
difficulty = 20
attempted = True
score = 0

while True:
    if attempted:
        try:
            a, b = random.randint(0, difficulty), random.randint(0, difficulty)
        except :
            print(Fore.LIGHTRED_EX + "Incorrect limit." + Fore.WHITE)
            difficulty = random.randint(0, 100)
        attempted = False
    print(a, selected_operator, b, " = ____?")
    input_ = input("<<< ").lower()

    try:
        result = int(input_)
        # Result validator
        if operators[selected_operator](a, b) == result:
            print(Fore.LIGHTYELLOW_EX + "[+] Correct." + Fore.WHITE)
            score += 1
        else:
            print(Fore.LIGHTRED_EX + "[-] Incorrect." + Fore.WHITE)
            score -= 1
        attempted = True

    except ValueError:
        selected_operator = command_handler(input_)

    print(Fore.GREEN + "...\n \nPress Return" + Fore.WHITE)
    input()
    if platform.platform() == 'linux':
        os.system('clear')
    else:
        os.system("cls")
