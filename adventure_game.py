import time
import random
import sys
import os


# Game Control
def menu():
    while True:
        action = input('Would you like to play again (y/n)')
        if len(action) > 1:
            print('Enter (y/n)')
            continue
        elif len(action) == 1 and action.lower() == 'n':
            print('Thanks for playing!')
            sys.exit()
        elif len(action) == 1 and action.lower() == 'y':
            print_pause('Nice! Restarting the game..')
            os.system('cls||clear')
            main()


# Ask question and verify input
def ask(question, options):
    while True:
        option = (input(question))
        print(option)
        try:
            option = int(option)
            # Check if option is available
            if option in set(options):
                break
            else:
                print('That option is not available')
                continue
        except ValueError:
            print('That doesn\'t seem to be a number')
            continue
    return option


# Print pause text
def print_pause(text):
    print(text)
    time.sleep(2)


# Fight or Flight
def fight_or_flight(sword, monster):
    print('\n')
    option = ask('Would you like to (1) fight or (2) run away?', [1, 2])
    print('\n')
    if sword and option == 1:
        print_pause(
            'As the {} moves to attack, you unsheath your new sword.'
            .format(monster))
        print_pause(
            'The Sword of Ogoroth shines brightly in your hand as you '
            'brace yourself for the attack.')
        print_pause(
            'But the {} takes one look at your shiny new toy '
            'and runs away!'.format(monster))
        print_pause(
            'You have rid the town of the {}. You are '
            'victorious!'.format(monster))
        menu()
    elif not sword and option == 1:
        print_pause('you do your best...')
        print_pause('but your dagger is no match for the {}.'.format(monster))
        print_pause('You have been defeated!')
        menu()
    else:
        print_pause(
            'You run back into the field. Luckily, '
            'you don\'t seem to have been followed.')


# Places
def cave(visit):
    print_pause('You peer cautiously into the cave.')
    if not visit:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause('You have found the magical Sword of Ogoroth!')
        print_pause(
            'You discard your silly old dagger and take the '
            'sword with you.')
        print_pause('You walk back out to the field.')
    else:
        print_pause(
            'You\'ve been here before, and gotten all the good '
            'stuff. It\'s just an empty cave now.')
        print_pause('You walk back out to the field.')


def house(visit, sword, monster):
    print_pause('You approach the door of the house.')
    print_pause(
        'You are about to knock when the door opens and '
        'out steps a {}.'.format(monster))
    print_pause('Eep! This is the {}\'s house!'.format(monster))
    print_pause('The {} attacks you!'.format(monster))
    if not sword:
        print_pause(
            'You feel a bit under-prepared for this, '
            'what with only having a tiny dagger.')
    fight_or_flight(sword, monster)


# Main program
def main():
    monsters = ['gorgon', 'pirate', 'dragon', 'troll']
    monster = random.choice(monsters)
    print_pause(
        'You find yourself standing in an open field, filled with '
        'grass and yellow wildflowers.')
    print_pause(
        'Rumor has it that a {} is somewhere around here, '
        'and has been terrifying the nearby village.'.format(monster))
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause(
        'In your hand you hold your trusty (but not very '
        'effective) dagger.')

    # Keep track of visits
    house_visit = False
    cave_visit = False
    while True:
        # Present options and ask user what to do
        print('\n')
        print_pause('Enter (1) to knock on the door of the house.')
        print_pause('Enter (2) to peer into the cave.')
        option = ask('What would you like to do?: ', [1, 2])
        print('\n')

        if option == 1:
            house(house_visit, cave_visit, monster)
            house_visit = True
        elif option == 2:
            cave(cave_visit)
            cave_visit = True
        else:
            print('that doesn\'t seem like a valid option')


main()
