"""
A difficulty randomizer to select a combination of Adversaries, Scenarios, Boards, etc. for Spirit Island

author: Evan Chiang
"""
import argparse
import random

import setup


def main():
    args = parse_args()

    while not args.number_of_players:
        args.number_of_players = set_number_of_players()
    if not args.difficulty:
        args.difficulty = int(input("Enter number of difficulty: "))
    if not args.single_adversary:
        single_adversary_input = input("Disable double adversaries? (y/n) ")
        args.single_adversary = False
        if single_adversary_input.lower() == 'y':
            args.single_adversary = True
    if not args.no_scenario:
        no_scenario_input = input("Disable scenarios? (y/n) ")
        args.no_scenario = False
        if no_scenario_input.lower() == 'y':
            args.no_scenario = True

    setup_dict = setup.construct_all_board_setups(args.number_of_players, args.single_adversary, args.no_scenario)

    possible_setups = setup_dict[args.difficulty]
    get_random_setup(possible_setups)
    while True:
        retry = input("\n\n\nPick another of the same difficulty? (y/n) \n")
        if retry in ['Y', 'y']:
            get_random_setup(possible_setups)
        else:
            exit(0)


def get_random_setup(possible_setups):
    possible_setups[random.randint(0, len(possible_setups) - 1)].print()


def set_number_of_players():
    number_of_players = int(input("Enter number of players: "))
    if number_of_players < 1 or number_of_players > 6:
        print(f"Number of players must be between 1 and 6 - Entered: {number_of_players}")
        number_of_players = None
    return number_of_players


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--number-of-players', help='The number of Spirits played in the game.',
                        type=int)
    parser.add_argument('-d', '--difficulty', help='The desired difficulty of the setup.', type=int)
    parser.add_argument('-a', '--single-adversary', help='Enable this to only have single adversary setups.',
                        action='store_true')
    parser.add_argument('-s', '--no-scenario', help='Enable this to not include scenarios in setups.',
                        action='store_true')

    return parser.parse_args()


if __name__ == '__main__':
    main()
