from time import *
from PIL import Image
from random import *
import sys

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
