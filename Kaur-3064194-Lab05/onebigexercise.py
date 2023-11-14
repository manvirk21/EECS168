"""
Author: Manvir Kaur
KUID: 3064194
Date: 10/04/2021
Lab: lab05
Last modified: 10/18/2021
Purpose: Web History
"""

arrow = ' <=='
history = []
command = ""
num = -1

while command != ["EXIT"]:
    command = input("Enter a command: ")
    command = command.split()
    if command[0] == "NAVIGATE":
        num += 1
        while num < len(history):
            history.remove(history[(len(history) - 1)])
        history.append(command[1])
    elif command[0] == "BACK":
        if  num > 0:
            num -= 1
        else:
            num = 0
    elif command[0] == "FORWARD":
        if num < len(history) - 1:
            num += 1
        else:
            num = len(history) - 1
    elif command[0] == "HISTORY":
        print_hist = list(history)
        print_hist[num] = print_hist[num] + arrow
        print("Oldest \n=========== \n" + "\n".join(print_hist) + "\n=========== \nNewest")
