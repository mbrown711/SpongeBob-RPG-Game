import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import *
from time import *
from random import *
import sys

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
