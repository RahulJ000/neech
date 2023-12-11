import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'jack', 'queen', 'king', 'ace']
suits = ['hearts', 'diamond', 'clubs', 'spades']
deck = [{'rank':rank, 'suit':suit} for rank in ranks for suit in suits]

def shuffle_deck(deck):
    random.shuffle(deck)

def display_deck(deck):
    for card in deck:
        print(f"{card['rank']} of {card['suit']}")

shuffle_deck(deck)
print("shuffle deck:")
display_deck(deck)
