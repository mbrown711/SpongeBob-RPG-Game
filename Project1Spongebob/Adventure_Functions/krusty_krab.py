from pygame import *
from time import *

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
print("Are you ready?!")
sleep(5)

try:
    flip = input("Flip! " + "\n")
    number_flips = 0
    while number_flips < 4:
        if flip.lower() == 'f':
            flip = input("Flip again! " + "\n")
            number_flips += 1
        elif flip.lower() == 'q':
            break
        else:
            flip = input("Wrong input! You need to press f to flip!" + "\n")
except(ValueError, TypeError):
    print("Wrong input! You need to press f to flip!" + "\n")

print("The krabby patty is cooked! Now we need to assemble it!")
sleep(2)

ingredients = ['cheese', 'patty', 'ketchup', 'buns', 'mustard', 'onions', 'tomato', 'lettuce']

print("Place the below ingredients in the correct order to make a krabby patty! ")
sleep(2)

for ingredient in ingredients:
    print(ingredient)
    sleep(2)


