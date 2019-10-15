from pygame import *
from time import *
# from PIL import Image


def menu_sleep():
    """Sleep for 3.5 seconds during the menu presentation"""
    sleep(3.5)


def play_again():
    play_again_input = input("Would you like to play again? Press q to quit, or press any key to go on another adventure! ")
    if play_again_input == 'q':
        return False
    else:
        mixer.music.load('Music/Menu_Song.mp3')
        mixer.music.play(-1)
        print("Yay! Let's play again!!")
        return True


def squidward():
    print("this is the squidward function")


mixer.init()
"""
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
"""
mixer.music.load('Music/Menu_Song.mp3')
mixer.music.play(-1)

print(
    "There are so many adventures to go on, but SpongeBob is super busy today and can only choose form 4 of them! "
    "Select a number to choose: ")
menu_sleep()
print("Press 1 to go work at the Krusty Krab")
menu_sleep()
print("Press 2 to go jellyfishing with Patrick")
menu_sleep()
print("Press 3 to play the clarinet with Squidward")
menu_sleep()
print("Press 4 to practice karate with Sandy")
menu_sleep()
print("To quit, just enter the letter q")
menu_sleep()

adventure_choice = ' '

while adventure_choice != 'q':

    adventure_choice = input("What adventure would you like to go on today?! ")

    if adventure_choice == str(1):
        print("krusty_krab function called")
        # def krusty_krab function/method called
        if not play_again():
            break
    elif adventure_choice == str(2):
        print("jellyfishing function called")
        # def jellyfishing function/method called
        if not play_again():
            break
    elif adventure_choice == str(3):
        print("squidward function called")
        squidward()
        mixer.music.stop()
        if not play_again():
            break
    elif adventure_choice == str(4):
        print("karate method called")
        # def karate function/method called
        if not play_again():
            break
    elif adventure_choice == 'q':
        print("Thanks for playing, we hope you had fun!!")
    else:
        print("Invalid input!")

print("You did great!")