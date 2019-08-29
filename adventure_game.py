import time
import random
import os


# Game Control
def menu():
    while True:
        action = input('Would you like to play again (y/n)').lower()

        if action == 'n':
            print('Thanks for playing!')
            exit()
        elif action == 'y':
            print_pause('Nice! Restarting the game..')
            os.system('cls||clear')
            main()
        else:
            print('Sorry I didn\'t understand that. Please enter (y/n)')
            continue


# Verify user input
def ask(question, options):
    while True:
        option = input(question)
        try:
            option = int(option)
            if option in set(options):
                break
            else:
                print('That option is not available. Try again!')
                continue
        except ValueError:
            print('That doesn\'t seem to be a number')
            continue
    return option


# Print text with delay for better UX
def print_pause(text):
    print(text)
    time.sleep(0.1)


class Weapon:

    """ Provides a way to randomly choose a weapon and description """
    WEAPONS = {
        'sword': 'magical Sword of Ogoroth',
        'axe': 'mighty Golden Axe',
        'flamethrower': 'scorching Flamethrower of Nukem'
    }

    weapon = random.choice(list(WEAPONS))

    def __init__(self, name=weapon, description=WEAPONS[weapon]):
        self.name = name
        self.description = description


def fight_or_flight(cave_visit, weapon, monster):
    print('\n')
    option = ask('Would you like to:\n(1) fight or (2) run away?', [1, 2])
    print('\n')
    if cave_visit and option == 1:
        print_pause(
            f'As the {monster} moves to attack, '
            f'you unsheath your new {weapon.name}.')
        print_pause(
            f'The {weapon.description} shines brightly in your hand as you '
            'brace yourself for the attack.')
        print_pause(
            f'But the {monster} takes one look at your shiny new toy '
            'and runs away!')
        print_pause(
            f'You have rid the town of the {monster}. You are '
            'victorious!')
        menu()
    elif not cave_visit and option == 1:
        print_pause('you do your best...')
        print_pause(f'but your dagger is no match for the {monster}.')
        print_pause('You have been defeated!')
        menu()
    else:
        print_pause(
            'You run back into the field. Luckily, '
            'you don\'t seem to have been followed.')


# Places
def cave(visit):

    my_weapon = Weapon()

    print_pause('You peer cautiously into the cave.')
    if not visit:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause(f'You have found the {my_weapon.description}!')
        print_pause(
            'You discard your silly old dagger and take the '
            f'{my_weapon.name} with you.')
        print_pause('You walk back out to the field.')
        return my_weapon
    else:
        print_pause(
            'You\'ve been here before, and gotten all the good '
            'stuff. It\'s just an empty cave now.')
        print_pause('You walk back out to the field.')


def house(cave_visit, weapon, monster):
    print_pause('You approach the door of the house.')
    print_pause(
        'You are about to knock when the door opens and '
        f'out steps a {monster}.')
    print_pause(f'Eep! This is the {monster}\'s house!')
    print_pause(f'The {monster} attacks you!')
    if not cave_visit:
        print_pause(
            'You feel a bit under-prepared for this, '
            'what with only having a tiny dagger.')
    fight_or_flight(cave_visit, weapon, monster)


def main():
    monsters = ['gorgon', 'pirate', 'dragon', 'troll']

    monster = random.choice(monsters)
    print_pause(
        'You find yourself standing in an open field, filled with '
        'grass and yellow wildflowers.')
    print_pause(
        f'Rumor has it that a {monster} is somewhere around here, '
        'and has been terrifying the nearby village.')
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause(
        'In your hand you hold your trusty (but not very '
        'effective) dagger.')

    # Keep track of visits
    cave_visit = False

    # Track weapon status
    weapon = None
    # Present options and ask user what to do
    print('\n')
    print('============================================')
    print_pause('Enter (1) to knock on the door of the house.')
    print_pause('Enter (2) to peer into the cave.')
    print('============================================')
    print('\n')
    option = ask('What would you like to do?: ', [1, 2])
    print('\n')

    if option == 1:
        house(cave_visit, weapon, monster)
    elif option == 2:
        weapon = cave(cave_visit)
        cave_visit = True


if __name__ == "__main__":
    main()
