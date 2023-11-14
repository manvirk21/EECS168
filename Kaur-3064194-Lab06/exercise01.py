'''
Author: Manvir Kaur
KUID: 3064194
Date: 10/18/2021
Lab: lab06
Last modified: 10/24/2021
Purpose: Using Functions 
'''

def last_digit(num):
    num = num % 10
    return num

def remove_last_digit(num):
    num = num // 10
    return num

def add_digit(num, new_digit):
    num = (num * 10) + new_digit
    return num

def reverse(num):
    reverse_dig = 0
    for n in range(count_digits(num)):
        digit = last_digit(num)
        num = remove_last_digit(num)
        reverse_dig = add_digit(reverse_dig, digit)
    return reverse_dig

def count_digits(num):
    count = 0
    while num != 0:
        count = count + 1
        num = remove_last_digit(num)
    return count

def is_palindrome(num):
    return num == reverse(num)

def sum_digits(num):
    added = 0
    for n in range(count_digits(num)):
        digit = last_digit(num)
        num = remove_last_digit(num)
        added = added + digit
    return added

def print_menu():
    return("What would you like to do? (enter the number) \n1) Count digits \n2) Sum digits\n3) Is Palindrome\n4) Reverse\n5) Exit")

def main():
    option = ""
    while option != 5:
        print(print_menu())
        option = int(input("Choice: "))
        if option == 5:
            pass
        else:
            num = int(input("Dear user, please enter a positive integer: "))
            if option == 1:
                print(count_digits(num))
            elif option == 2:
                print(sum_digits(num))
            elif option == 3:
                print(is_palindrome(num))
            elif option == 4:
                print(reverse(num))

main()
