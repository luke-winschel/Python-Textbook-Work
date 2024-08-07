#Exercise 5.24 - 5.26
#5.24(Card Shuffling and dealing) Create an initialize_deck function to initialize a deck of cards.  Before returning the list, use the random module's shuffle function to randomly order the elements and display them in a four column format
#5.25 (Card playing: Evaluating poker hands) Create a function to deal 5 random cards as a tuple.  Then create functions that determine whether the hand received contains a winable hand
#5.26 (Determine the winning hand) Write a script that deals two poker hands and evaluates each hand and determines which wins.  As each card is dealt it should be removed from the deck tuple

#Section 5.24
#Import random function
import random

def initialize_deck():
    #Create empty list
    deck = []
    #Create two lists that contain the values and suites
    suits = ['Heart', 'Spades', 'Clubs', 'Diamonds']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    #For loops that match one of every value to one of every suit and appends it to the deck list.
    for suit in suits:
        for value in values:
            deck.append((value, suit))
    
    #Randomly shuffle the deck list.
    random.shuffle(deck)
   
    #Return deck to allow future programs to use and manipulate the list
    return deck

shuffled_deck = initialize_deck()

for i in range (len(shuffled_deck)):
    face, suit = shuffled_deck[i]
    print('{:28s}'.format(face + ' of ' + suit), end='')
    if (i + 1) % 4 == 0:
        print()
#Section 5.25



initialize_deck()
        