#Import statements
from Classes import *
from Functions import *
from WordGen import *
#import random  --- it isn't clear to me whether there is any difference
#between this and importing from numpy



def main():
    #Main function, entrypoint:

    #Code below gives locations.
    placeholder_start_location = Location("Start Area", "You are at the start location.")

    #The code below should run at the beginning, including any introduction, welcoming messages etc.

    r1 = word_length()
    r2 = word_length()

    word = word_gen(r1).capitalize() +" "+ word_gen(r2).capitalize()
    print("Hello. Welcome to the"+" "+ word +" "+ "galaxy")

    #Ask player for their Name.
    #The player also needs to start at some location.
    print("\nWhat is your name?")
    player = Player(input("My name is "), placeholder_start_location)

    



    #Main game loop:
    play_game = True

    while(play_game):
        #Main game code goes here. The player has just arrived at a location.
        
        #Output the name of the place they are in.
        print("\nYou are in %s." %(player.location.get_name()))

        #Output description of location that they are in.
        print(player.location.get_description())

        #Ask the player what they want to dir
        print("\nWhat do you want to do?")
        
        player_choice = input("> ")

        




        



        pass #placeholder.

    


if __name__ == "__main__":
    main()

