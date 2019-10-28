import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import *
from time import *
from PIL import Image
from random import *
import sys

def menu_sleep():
    # Sleep for 3.5 seconds during the menu presentation
    sleep(3.5)


def play_again():
    play_again_input = input("Would you like to play again? Press q to quit, or press any key to go on another "
                             "adventure! ")
    if play_again_input == 'q':
        return False
    else:
        mixer.music.load('Music/Menu_Song.mp3')
        mixer.music.play(-1)
        print("Yay! Let's play again!!")
        return True

def krusty_krab():
    mixer.init()
    mixer.music.load('krabby_patty.mp3')
    mixer.music.play(1)
    while mixer_music.get_busy():
        sleep(1)

    print("Hey, look! It's Mr. Krabs! ")
    sleep(2)
    print("Spongebob! Enough lolligagin' around me boy! It's time to make some krabby patties!")
    sleep(5)
    print("Mr. Krabs wants you to make a krabby patty for some hungry customers!")
    sleep(4)
    print("To flip the patty, press 'f'. You'll know when it's ready!")
    sleep(4)
    print("Ready.....")
    sleep(2)
    print("Set.....")
    sleep(2)

    number_flips = randint(3, 7)
    while number_flips < 10:
        flip = input("Flip! " + "\n ").lower()
        if flip == 'f':
            number_flips += 1
        elif flip == 'q':
            print("Thanks for playing!")
            sys.exit()
        else:
            flip = input("Wrong input! You need to press f to flip!" + "\n")

    print("The krabby patty is cooked! Now we need to assemble it!")
    sleep(2)

    shown_ingredients = ['cheese', 'patty', 'pickles' 'ketchup', 'bottom bun', 'mustard', 'onions', 'top bun' 'tomato',
                         'lettuce']

    print("Place the below ingredients in the correct order to make a krabby patty! ")
    sleep(2)

    for shown_ingredient in shown_ingredients:
        print(shown_ingredient)
        sleep(2)

    correct_order_ingredients = ('bottom bun', 'patty', 'lettuce', 'cheese', 'onions', 'tomato', 'ketchup', 'mustard',
                                 'pickles', 'top bun')

    user_entered_ingredients = []

    user_input = input("Enter the first ingredient: ").lower()
    counter = 0
    wrong_input = 0

    while counter < 2:
        if user_input == correct_order_ingredients[counter]:
            counter += 1
            user_entered_ingredients.append(user_input)
            print(user_entered_ingredients)
            print(counter)
            user_input = input("Correct! What's the next ingredient?! " + "\n").lower()
        elif user_input == 'q':
            print("Thanks for playing! ")
            sys.exit()
        else:
            wrong_input += 1
            user_input = input("Incorrect! Guess again! ")

    print()
    print("Congratulations! You've made your first Krabby Patty!" + "\n")

    if wrong_input == 0:
        print("Wow - a perfect Krabby Patty on your first try! You deserve a promotion!" + "\n")
    elif wrong_input == 1:
        print("You only missed " + str(wrong_input) + " ingredient! You're a natural!" + "\n")
    elif 3 > wrong_input > 1:
        print("You only missed " + str(wrong_input) + " ingredients! You're a natural!" + "\n")
    elif 3 <= wrong_input < 6:
        print(str(wrong_input) + " missed ingredients - not bad!")
    else:
        print("You missed " + str(wrong_input) + " ingredients!")
        print("Mr. Krabs is not going to be happy - you need to brush up on your Krabby Patty training!")

def jellyfishing_patrick():
    mixer.init()
    mixer.music.load('Jellyfishing_Song.mp3')
    mixer.music.play(-1)

    print("Hey, look! It's Patrick! Hi Patrick! ")
    sleep(3)

    print("Hey Spongebob, are you ready to go jellyfishing?!")
    sleep(3)
    bring_net = str(input("Grab your net and enter 'go' to continue! ").lower())
    while bring_net != 'go':
        if bring_net == 'q':
            print("Thanks for playing!")
            sys.exit()
        else:
            bring_net = str(input("Invalid input! Enter 'go' when you're ready! ").lower())

    mixer.music.stop()

    print("Great! Let's go jellyfishing!")
    sleep(2)
    print("We have to keep running until we're close enough to catch a jellyfish.")
    sleep(4)
    print("Keep entering in 'r' to run until you're close enough to catch it.")
    sleep(4)
    print("When I tell you you're close enough, enter 'catch' to catch the jellyfish!")
    sleep(4)

    # user enters a random number of r's until spongebob is close enough
    # each loop through a random number increases the count by 1
    # once the count reaches a certain number, display the picture of spongebob catching the jellyfish

    run_input = randint(5, 8)
    while run_input < 15:
        run = input("Run, Spongebob, run! ").lower()
        if run == 'r':
            run_input += 1
            if run_input == 14:
                print("You almost got it Spongebob!")
        elif run == 'q':
            print("Thanks for playing!")
            sys.exit()
        else:
            run = input("Invalid input! You need to press r to run!" + "\n").lower()

    catch = str(input("Enter 'catch' to catch the jellyfish! ").lower())

    while catch != 'catch':
        catch = str(input("That won't work! Enter 'catch' to catch the jellyfish! ").lower())

    if catch:
        # When the user catches the jellyfish, show the image of Spongebob and Patrick
        # catching a jellyfish:
        with Image.open('Jellyfishing.jpg') as img:
            img.show()

    print("Great job - you caught the jellyfish!")

def sandy_karate():
    print("It's our old friend, Sandy Cheeks! Hi Sandy! ")
    sleep(3)

    print("Howdy Spongebob! We better high tail it to karate practice!")
    sleep(4)
    print("I hope you've been practicing your karate chopping skills! Let's go! ")
    sleep(4)

    hiya_continue = str(input("Enter 'hi-ya!' to continue! ").lower())
    while hiya_continue != 'hi-ya!':
        if hiya_continue == 'q':
            print("Thanks for playing!")
            sys.exit()
        else:
            hiya_continue = str(input("Invalid input! Enter 'hi-ya!' to continue! ").lower())

    print("Ok Spongebob, let's try to chop this dang-fangled piece of wood in half.")
    sleep(4)
    print("Keep chopping until the piece of wood is chopped in half.")
    sleep(4)
    print("After you see 'HIIII-YAA!', enter 'chop' until you've chopped through the wood.")
    sleep(5)

    chop = " "
    chop_num = randint(5, 7)
    while chop_num < 10:
        chop = input("HIIII-YAA! ").lower()
        if chop == 'chop':
            chop_num += 1
            if chop_num == 14:
                print("By golly Spongebob, one more chop should do it!")
        elif chop == 'q':
            print("Thanks for playing!")
            sys.exit()
        else:
            chop = input("Invalid input! You need to enter 'chop' to to chop the wood in half!" + "\n").lower()

    if chop:
        # When the user catches the jellyfish, show the image of Spongebob and Patrick
        # catching a jellyfish:
        with Image.open('Karate.png') as img:
            img.show()

    print("You did it! HIIII-YAAAA!!!")


mixer.init()

print("Welcome to the SpongeBob SquarePants Adventure Game! Let's get started!")
mixer.music.load('Music/Theme_Song.mp3')
mixer.music.play()
while mixer.music.get_busy():
    sleep(11)
    print("Who lives in a pineapple under the sea?")
    print("Spongebob Squarepants!")
    sleep(3.5)
    print("Absorbant, and yellow, and porous is he")
    print("Spongebob Squarepants!")
    sleep(3.7)
    print("If nautical nonsense be something you wish")
    print("Spongebob Squarepants!")
    sleep(3.8)
    print("Then drop on the deck and flop like a fish")
    print("Spongebob Squarepants!")
    sleep(4)
    print("Spongebob Squarepants!")
    sleep(2.2)
    print("Spongebob Squarepants!")
    sleep(2.2)
    print("Spongebob Squarepants!")
    sleep(2.2)
    print("Spongebob Squarepants!")
    sleep(10)
    mixer.music.stop()

mixer.music.load('Music/Menu_Song.mp3')
mixer.music.play(-1)

print(
    "There are so many adventures to go on, but SpongeBob is super busy today and can only choose from 3 of them! "
    "Select a number to choose: ")
menu_sleep()
print("Press 1 to go work at the Krusty Krab")
menu_sleep()
print("Press 2 to go jellyfishing with Patrick")
menu_sleep()
print("Press 3 to practice karate with Sandy")
menu_sleep()
print("To quit, just enter the letter q")
menu_sleep()

adventure_choice = ' '

while adventure_choice != 'q':

    adventure_choice = input("What adventure would you like to go on today?! ")

    if adventure_choice == str(1):
        krusty_krab()
        mixer.music.stop()
        if not play_again():
            sys.exit()
    elif adventure_choice == str(2):
        jellyfishing_patrick()
        mixer.music.stop()
        if not play_again():
            sys.exit()
    elif adventure_choice == str(3):
        sandy_karate()
        mixer.music.stop()
        if not play_again():
            sys.exit()
    elif adventure_choice == 'q':
        print("Thanks for playing, we hope you had fun!!")
        sys.exit()
    else:
        print("Invalid input!")
