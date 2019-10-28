import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import *
from time import *
from PIL import Image
from random import *
import sys

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
