'''
Author: Manvir Kaur
KUID: 3064194
Date: 11/14/2021
Lab: lab09
Last modified: 11/15/2021
Purpose: Pokedex Interaction
'''

import random

pokelist = open("pokelist.txt", "r")


def build_pokedex(pokelist):
    pokelist = open("pokelist.txt", "r")
    poke_dict = {}
    for pokemon in pokelist:
        names = pokemon.strip().split()
        US_name = names[0]
        jpn_name = names[1]
        poke_dict[US_name] = jpn_name
    return poke_dict

def build_team(poke_dict, size = 6, is_unique = False):
    poketeam = []
    if is_unique == False:
        for i in range(size):
            poketeam.append(random.choice(list(poke_dict)))
    else:
        new_dict = {}
        while size > 0:
            pokemon = random.choice(list(poke_dict))
            if new_dict.get(pokemon):
                continue
            else:
                poketeam.append(pokemon)
                new_dict[pokemon] = 1
                size = size - 1
    return poketeam

def battle(poketeam1, poketeam2):
    print("+++Team 1+++")
    for pokemon in poketeam1:
        print(pokemon)
        
    print("\n+++Team 2+++")
    for pokemon in poketeam2:
        print(pokemon)

    round = 1
    print()
    combatant1 = 0
    combatant2 = 0
    while combatant1 < 6 and combatant2 < 6:
        print(f"+++Round {round}+++")
        print(f"{poketeam1[combatant1]} VS {poketeam2[combatant2]}")
        victory = random.randint(0,1)
        if victory == 1:
            combatant2 += 1
            print(f"{poketeam1[combatant1]} wins!")
        else:
            combatant1 += 1
            print(f"{poketeam2[combatant2]} wins!")
        round += 1
        print()
    if combatant2 == 6:
        print("Team 1 won the battle.")
        print("Remaining Pokemon:")
        for i in range(combatant1, 6):
            print(poketeam1[i])
    else:
        print("Team 2 won the battle.")
        print("Remaining Pokemon:")
        for i in range(combatant2, 6):
            print(poketeam2[i])

def main():
    poke_dict = build_pokedex("pokelist.txt")
    x = True
    while x == True:
        print("1) Print Pokedex")
        print("2) Translate")
        print("3) Build a team")
        print("4) Pokemon battle")
        print("5) Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print()
            print("US_Name | JPN_Name")
            for US, jpn in poke_dict.items():
                print(f"{US} | {jpn}")
            print()

        elif choice == 2:
            print()
            US_name = input("Enter the US Name: ")
            if poke_dict.get(US_name) is None:
                print("The given name wasn't found in the pokedex")
            else:
                print("The JPN name is :", poke_dict.get(US_name))
            print()

        elif choice == 3:
            print()
            poketeam = build_team(poke_dict)
            print("+++TEAM+++")
            for pokemon in poketeam:
                print(pokemon)
            print()

        elif choice == 4:
            poketeam1 = build_team(poke_dict, is_unique=True)
            poketeam2 = build_team(poke_dict, is_unique=True)
            battle(poketeam1, poketeam2)
            print()

        elif choice == 5:
            x = False

main()
