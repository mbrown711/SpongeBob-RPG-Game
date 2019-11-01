# SpongeBob SquarePants Adventures in Python
Matt Brown<br/>
Pace University - CS 632P<br/>
Project 1<br/>
10/30/19<br/>

*Documentation also in PDF form in folder*

Table of Contents:
==================

[Introduction](#Introduction)

[What's Included](#what's-included)

[Flowchart of Game flow](#flowchart-of-game-flow)

[Getting Started & Preparing your Environment](#getting-started-&-preparing-your-environment)

[Running the Game](#running-the-game)

[Playing the Game](#playing-the-game)

[Game Features & Software Design](#game-features-&-software-design)

[Testing](#testing)

[Known Bugs](#known-bugs)

[Considerations & Enhancements for Version 2.0](#considerations-&-enhancements-for-version-2.0)

[Special Thanks](#special-thanks)

---

## Introduction

Welcome to the SpongeBob SquarePants Adventure video game! In this game, you'll be playing the role of SpongeBob SquarePants - the happiest and most fun invertebrate of Bikini Bottom! You'll get to choose from a few different adventures to go on with familiar friends from Bikini Bottom. Each adventure you choose will bring you on a different path - from jelly fishing with Patrick, to practicing karate with Sandy. As SpongeBob himself would say, "I'm Ready!!” Have fun!

---

## What's Included:

Folders and files included in the package:

***CS 632P Project 1 Flow Chart.pdf*** - A flow chart showing the basic flow of the game. Text that appears in the flow chart is not meant to be an exact match of the text the user will see, but rather a visual representation of how the game flows.

***Spongebob.py*** - The main Python file to run the game (Python source code).

***Requirements.txt*** - Contains a list of package names required to play the game. We will run this file later in a virtual environment so that the game can run properly on any machine.

***Images Folder*** - Folder that contains the necessary images that pop up during the game.

***Songs Folder*** - Contains the song files that are played throughout the game (all in .mp3 format).

***```venv``` Folder*** - Virtual environment folder that contains all of the libraries and dependencies needed to run the game. We will go over how to create a venv on any machine running Python 3.7.4 or greater, so that the game can run properly.

---

## Flowchart of Game flow:

![Flowchart Image.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/Flowchart%20Image.png)

---

## Getting Started & Preparing your Environment:

Typically, Python is already pre-installed on a user's computer. If, for some reason, a user has no version of Python installed on their system, it can be downloaded [here](https://www.python.org/downloads/release/python-374/) and installed.

Save the folder titled SpongebobProject1 onto your computer (I recommend the Desktop). The use of this program involves using the terminal (mac/Linux) or command prompt (windows). Let’s start the virtual environment, which is included in the software package:
  
  1. On macOS, open the terminal applications. To do this, go to Applications --> Utilities folder --> Terminal. You can always search for it using spotlight as well.
  2. On Windows, open the start menu and search for cmd. Open the application titled Command Prompt.
  3. In the terminal/command prompt, make the current directory the Project1Spongebob folder that was saved by typing in ```cd Path/to/file``` on macOS, or ```cd Path\to\file``` on Windows. The below example shows if it was saved on a Desktop (*Tip: to see what's in the folder, you can type and enter ```ls``` for macOS and ```dir``` for Windows*):

*On macOS:*

![cd into spongebob folder.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/cd%20into%20spongebob%20folder.png)

*On Windows:*

![cd windows.JPG](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/cd%20windows.JPG)

  4. Now, we need to activate our virtual environment, or venv for short. This step will allow us to run the game, whether it's macOS, Windows, or Linux. It will also allow us to run the game in case there are different versions of Python or packages from machine to machine. While still in the project folder, enter the following command to activate the virtual environment:
  
*On macOS:*

```sh
source ./venv/bin/activate
```

*On Windows:*

```sh
venv\Scripts\activate
```

  * You should see something similar to the screenshot below:
  
![activate venv.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/activate%20venv.png)

  5. Now that we have activated our virtual environment, we need to install the proper packages. To do this, enter the command below while in the virtual environment:

```sh
pip3 install -r Requirements.txt
```

  * This will install the necessary packages automatically. You are now ready to play! 
  * The steps above only need to be run the first time you set up the virtual environment. After the first time, you can skip right to playing the game. 

---

## Running the game

* It's best to start and run the game in the terminal (macOS)/cmd prompt (Windows). To start playing:
  1. Open a new terminal window.
  2. Find the location where you saved ```Spongebob.py``` (from a previous step in this document, it should be on your Desktop).
  3. In the terminal/command prompt, make the location of the ```Spongebob.py``` the current directory:

  - For macOS & Linux, enter in: ```cd path/to/Project1Spongebob```(Example below):
  
![cd into spongebob folder.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/cd%20into%20spongebob%20folder.png)

  - For Windows, enter in: ```cd path\to\Project1Spongebob```(Example below):

![cd windows.JPG](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/cd%20windows.JPG)
  
  4. Activate your virtual environment by typing in ```source ./venv/bin/activate``` on macOS or ```venv\Scripts\activate``` on Windows:

![activate venv.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/activate%20venv.png)
  
  5. To start the game, type in ```python3 Spongebob.py``` and press enter:

![run the name.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/run%20the%20name.png)

---

## Playing the game:

* Once the game is started, the SpongeBob theme song will start to play. While the song is playing, the lyrics to the theme song are displayed:
  
![lyrics.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/lyrics.png)
  
* You will then be presented with a greeting, and a menu:

```sh
There are so many adventures to go on, but SpongeBob is super busy today and can only choose from 3 of them! Select a number to choose:
Press 1 to go work at the Krusty Krab
Press 2 to go jellyfishing with Patrick
Press 3 to practice karate with Sandy
To quit, just enter the letter q
What adventure would you like to go on today?!
```

* If you enter 1 and choose to work at the Krusty Krab, you'll get to cook and assemble the legendary Krabby Patty! You'll meet Mr. Krabs, who will then ask you to make a Krabby Patty. First, you'll have to cook the patty. You'll be asked to flip the patty over a few times until it's done. Then, you'll need to assemble the Krabby Patty. The game will show you the ingredients needed to make a Krabby Patty. Enter in each ingredient, one-by-one, until you've correctly assembled the Krabby Patty. Don't worry about forgetting what you've entered for ingredients - the game will keep track of your list, and show your progress. Once you've successfully made a Krabby Patty, an image will appear. Close the image to return to the game.

* If you enter 2 and choose to go jellyfishing, you'll hang out with Patrick and get the chance to catch your very own jellyfish in jellyfish fields! Jellyfish don't get caught by just sitting around and waiting for them to fall into your net, so you'll have to run to catch them. When Patrick tells you to, run as fast as you can towards the jellyfish. Patrick, being the best buddy that he is, will let you know once you're close enough to try to catch the jellyfish. Once you catch it, an image will appear. Close the image to return to the game.

* If you enter 3 and choose to go practice karate, you and Sandy will brush up on your karate chopping skills! You and Sandy need to chop through the piece of wood, no matter how many chops it takes! Sandy will let you know when to start chopping, and when you're close to chopping the wood in half. Once you've chopped through the wood, an image will display. Close the image to return to the game. Are you up for the challenge? Hi-ya!

---

## Game Features & Software Design:

### Functions:

Below are the custom functions & algorithms that were made for the game:

```python
def menu_sleep()
```

This is a simple function that's called during the menu presentation. After each choice presentation, wait for 3.5 seconds, then show the next choice.

```python
def show_krabby_patty()
```

This function utilizes the Pillow package to show an image of a Krabby Patty once the user in successful in assembling it during the game.

```python
def show_jellyfishing()
```

This function utilizes the Pillow package to show an image of SpongeBob and Patrick in jellyfish fields once the user "catches" the jellyfish in the game it during the game.

```python
def show_karate()
```

This function utilizes the Pillow package to show an image of SpongeBob in action in his karate gear once the user completes "chopping" the wood in half during the game.

```python
def play_again()
```

This function runs at the end of each adventure choice, and asks the user if they'd like to play again. An input prompt asks the user if they want to play again, and the user does, they press any key to continue. The game asks the user what adventure they'd like to go on, and they can either enter in another adventure choice (1, 2, 3) or 'q' to quit. If the user doesn't enter either of these, the game tells the user that the input is invalid.

```python
def krusty_krab()
```

Adventure choice 1 is to go work at the Krusty Krab to cook and assemble a Krabby Patty. Once the user enters 1 as their adventure choice, this function is run. It starts by utilizing the Pygame package to play a sound bite, which is the from the classic episode where SpongeBob goes through training at the Krusty Krab. The song is loaded, and the ```mixer.music.play(1)``` plays the sound bite, but only once, as we passed ```1``` as a parameter. The code

```python
while mixer_music.get_busy():
  sleep(1)
```

is needed to check if the music stream is playing, and returns ```True``` if the music stream is actively playing. Pygame is used again to load the Krusty Krab theme song, and this is played throughout the user's time in the Krusty Krab.

Mr. Krabs then tells SpongeBob that there are customers waiting for their Krabby Patties, and it's his job to cook and assemble a Krabby Patty. The code below creates a variable called ```number_flips``` which will be used as a counter for the number of times the user enters `f`. It's assigned a random number between 3 and 7, and while its value is < 10, the game will prompt an input from the user to "flip" the patty:

```python
number_flips = randint(3, 7)
    while number_flips < 10:
        flip = input("Flip! ").lower()
        if flip == 'f':
            number_flips += 1
        elif flip == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            print("Wrong input! You need to press f to flip!")
```

For example, if the random number ends up being 5, the game will prompt the user to flip the patty 5 more times to fully cook it.

Once the patty is done cooking, the user needs to assemble the patty. Here, we are going to utilize lists and tuples for data structures. The list `shown_ingredients` is a list of Krabby Patty ingredients that are show to the user, 1 by 1 with the `for` loop below:

```python
for shown_ingredient in shown_ingredients:
  print(shown_ingredient)
  sleep(1.5)
```

The user needs to assemble the patty using the above ingredients in the correct order. The tuple `correct_order_ingredients` is the correct order in which a Krabby Patty is made. We went with a tuple here, since they are immutable, and the order of a Krabby Patty cannot be changed. Now, we know what you're thinking - "why is the cheese on top of the lettuce and not on top of the patty?". We agree that's it's maddening that this is the order in which a Krabby Patty is made (we had to confirm it with sources close to Mr. Krabs), but this is indeed the way it's made...

An empty list is created called `user_entered_ingredients`. This list will be appended with input from the user as they are assembling the Krabby Patty. We then have the `user_input` which will take the ingredient input from the user, a variable called `counter` to keep track of the index in the list, and a variable called `wrong_input`, which tracks how many times the user messed up their Krabby Patty and entered the wrong sequential ingredient. We then go into the algorithm that determines whether or not the user entered the correct ingredient:

```python
    while counter < 9:
        if user_input == correct_order_ingredients[counter]:
            counter += 1
            user_entered_ingredients.append(user_input)
            print(user_entered_ingredients)
            user_input = input("Correct! What's the next ingredient?! " + "\n").lower()
        elif user_input == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            wrong_input += 1
            user_input = input("Incorrect! Guess again! ")
```

The `while` loop conditional is that while `counter` is < 9, keep looping through. We set this to 9 because there are 9 ingredients in a Krabby Patty. If the `user_input` is the same as the counter's index spot in the `correct_order_ingredients` tuple, the `counter` is increased by 1, and the `user_entered_ingredients` list is appended with the input from `user_input`. The game will then print the list that the user is working on, so that they don't forget what they've entered so far, informs the user that they're correct, and asks for the next ingredient. If the user is incorrect, the `wrong_input` value increases by 1, and the program asks the user to guess again.

If, at any time, input is available to the user, and the user enters 'q', the program will end,and thank the user for playing.

Once the user has successfully "made" a Krabby Patty, the `show_krabby_patty()` function is called, and an image of a Krabby Patty appears on screen. 

The game then takes the value of `wrong_input`, and displays a message depending on how many times the user incorrectly guessed the wrong ingredient.

```python
def jellyfishing_patrick()
```

Adventure choice 2 is to go jellyfishing with Patrick in jellyfish fields. After the user enters 2, this function is run. A new song is started, which is the song you would hear all the time whenever SpongeBob and Patrick would hang out. The program has Patrick ask if the user is ready to go jellyfishing, and to enter 'go' to continue. If the user enters q, the program will end, and if the user enters anything other than 'go' Patrick will tell the user that it's an invalid input, and prompt the user again, asking if they are ready. Whenever there is an input, we are utilizing the `.lower()` function in order to avoid any potential case-sensitive input errors:

```python
print("Hey Spongebob, are you ready to go jellyfishing?!")
sleep(1)
bring_net = input("Grab your net and enter 'go' to continue! ").lower()
while bring_net != 'go':
  if bring_net == 'q':
    print("Thanks for playing! We hope you had fun!")
    sys.exit()
  else:
    bring_net = input("Invalid input! Enter 'go' when you're ready! ").lower()
```

If the user enters 'go', the program continues, and Patrick explains how to catch a jellyfish to the user. The user will have to input 'r' to simulate running towards a jellyfish. Patrick will then let the user know that they are close to the jellyfish, and then tell the user to enter 'catch' to actually catch the jellyfish. `run_input` is a random `int` between 5 and 8, and represents the number of times the user needs to enter in 'r' to run. If the user enters 'r', `run_input` increases by 1, up until the conditional for the `while` loop it's in, which is 15. If the user enters 'q' at any time, the program exits. If the user enters anything other than 'r' or 'q', a message is displayed, letting the user know that the input is invalid and to try again. Once `run_input` hits 14, the game lets the user know that they're close by displaying "You almost got it SpongeBob". After the user enters in the next 'r', Patrick tells the user to enter "catch" to catch the jelly fish. If the user enters "catch", the `show_jellyfishing()` function is called, and the picture of SpongeBob and Patrick in jellyfish fields is displayed.

```python
def sandy_karate()
```

Adventure choice 3 is to go practice karate with Sandy, and it works similarly to the `def jellyfishing_patrick()` function. The Pygame package is utilized to start a new song that plays throughout the adventure. The user is prompted with Sandy greeting them with print statements, and is then asked to enter 'hi-ya!' to continue. If the user enters anything other than 'hi-ya!' or 'q', it lets the user know that it's an invalid input, and to try again. If the user enters 'q' the program ends:

```python
hiya_continue = input("Enter 'hi-ya!' to continue! ").lower()
    while hiya_continue != 'hi-ya!':
        if hiya_continue == 'q':
            print("Thanks for playing! We hope you had fun!")
            sys.exit()
        else:
            hiya_continue = input("Invalid input! Enter 'hi-ya!' to continue! ").lower()
```

The program continues to them create a random `int` called `chop_num` and a variable called `chop` that will be used to check if the user actually entered the word 'chop' when prompted. If the user correctly enters in 'chop', the variable `chop_num` is increased by 1. Once `chop_num` is equal to 14, Sandy lets the user know that they're almost done "chopping", and that 1 more input will be needed. After the final time the user enters 'chop', the `show_karate()` function is called, and a picture is displayed on the screen:

```python
chop = " "
chop_num = randint(5, 7)
while chop_num < 15:
  chop = input("HIIII-YAA! ").lower()
  if chop == 'chop':
    chop_num += 1
    if chop_num == 14:
      print("By golly Spongebob, one more chop should do it!")
    elif chop == 'q':
      print("Thanks for playing! We hope you had fun!")
      sys.exit()
      else:
        print("Invalid input! You need to enter 'chop' to to chop the wood in half!")

if chop:
  show_karate()
```

### Libraries Used

***Pygame:***
 
The Pygame library is being used to play the music throughout the game. Pygame's ```pygame.mixer.music``` needs to first be initialized with ```mixer.init()```. The music is then loaded, with ```mixer.music.load('Path/to/song.mp3')```, with the path to the song file being passed through as a string. .mp3 files work best for this, and other sound files didn't have as much consistency as .mp3 files. The music will start to play with the ```mixer.music.play()``` method. A parameter can be passed depending on how many times you want to play the song, but since we're only playing the theme song once, no parameter is needed. In order to check and make sure the music stream is playing, we run ```mixer.music.get busy()```, and loop through the theme song/lyrics once to display them. We add ```mixer.music.stop()``` to stop the music where we want it to. When it's all put together, the code is as follows:

```python
from pygame import *

mixer.init()

print("Welcome to the SpongeBob SquarePants Adventure Game! Let's get started!")
mixer.music.load('Songs/Theme_Song.mp3')
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
```

***Pillow:***

The Pillow package's main feature is to display images when the user has completed one of their adventures. The following code is placed in a function, depending on the situation:

```python
import PIL form Image

with Image.open('Path/to/image.png') as img:
  img.show()
```

### Main Body:

The main body of the program runs right after the theme song is played once the program is started. We create a variable called `adventure_choice`. While the user doesn't enter 'q' when prompted, the program will continue to run. Depending on what the user enters as a choice, a certain function will run, and the game will continue. If, at any point during the game, the user enters 'q' when prompted, the program will end with `sys.exit()`:

```python
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
```

## Testing:

Various test we ran are shown below with screen shots, showing each adventure, and the possible input a user could enter while playing. All tests were done while using the virtual environment provided with the package:

### New Game Testing

***Testing Main Body:***

  * Theme song starts and plays successfully each time.
  * Song starts and menu displays successfully on new run.
  * Entering the following invalid options had no effect on the game on a new or existing run from a previous adventure:
    - Number that is not an option
    - Words
    - Random letters
    - Negative numbers
    - Pressing enter only
    - Entering spaces
    - Entering 0
    - Input accepted lower case and capital letters

![random inputs new game.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/random%20inputs%20new%20game.png)

  * The song will continue to play until the player enters a valid input.
  
***Testing Adventure 1 - Krusty Krab:***

  * Krabby Patty anthem plays successfully.
  * Krusty Krab theme song plays successfully.
  * Instructions appear successfully.
  * Entering the following invalid options had no effect on the game on a new or existing run during the patty cooking section nor the Krabby Patty assemble section:
    - Words
    - Random letters
    - Negative numbers
    - Pressing enter only
    - Entering spaces
    - Entering 0

  * Song continues to play throughout.
  * Once user completes the adventure, picture displays successfully.
  * Music stops successfully.
  * User is prompted if they want to play again.
  
Screen shots show testing below:

![flip input.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/flip%20input.png)

![random inputs new game.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/random%20inputs%20new%20game.png)

***Testing Adventure 2 - Jellyfishing with Patrick:***

  * Jellyfishing song plays successfully.
  * Instructions appear successfully.
  * Entering the following invalid options had no effect on the game on a new run or when starting from a previous adventure:
    - Words
    - Random letters
    - Negative numbers
    - Pressing enter only
    - Entering spaces
    - Entering 0

  * Song continues to play throughout.
  * Once user completes the adventure, picture of SpongeBob and Patrick displays successfully.
  * Music stops successfully.
  * User is prompted if they want to play again.
  
Screen shots show testing below:

![jellyfishing test.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/jellyfishing%20test.png)

***Testing Adventure 3 - Practicing Karate with Sandy:***

  * Kung-fu song plays successfully.
  * Instructions appear successfully.
  * Entering the following invalid options had no effect on the game on a new run or when starting from a previous adventure:
    - Words
    - Random letters
    - Negative numbers
    - Pressing enter only
    - Entering spaces
    - Entering 0

  * Song continues to play throughout.
  * Once user completes the adventure, picture of SpongeBob in his karate gear displays successfully.
  * Music stops successfully.
  * User is prompted if they want to play again.
  
Screen shots show testing below:

![Sandy tests.png](https://github.com/mbrown711/Screenshots-for-CS632P-Project1/blob/master/Sandy%20tests.png)

***Testing cases where the user enters 'q' at any time:***

  * At the main menu (new game or coming form an existing adventure) - pass.
  * Krusty Krab function during a new game or coming from an existing adventure - pass.
  * Jellyfishing with Patrick function during a new game or coming from an existing adventure - pass.
  * Practicing Karate with Sandy function during a new game or coming from an existing adventure - pass.

## Known Bugs:

* Program is not compatible with Python 3.8. Third party packages return errors when running on Python 3.8.
* We have noticed 2 times out of several tests that the music played was very slowed down.
* Sometimes right when a song will begin to play, there is sound distortion, but it is very brief. 

## Considerations & Enhancements for Version 2.0:

* Add a 4th adventure that involves Squidward or Gary (SpongeBob's snail).
* Make a GUI for the characters to interact with each other.
* Allow the user to play as themselves instead of SpongeBob (i.e. ask the user for their name, and have the characters interact with the user).

## Special Thanks:

Special thanks to the Pygame and Pillow developers for making the libraries that made this game possible. 

Thanks to all my friends and family (Kelly, Alex, Mom, Dad) that helped test this game by playing it. 

A very special thanks to my wife, Dalila. Thank you for testing this game several times, and suffering through hearing the SpongeBob theme song hundreds of times.
