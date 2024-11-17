# Blackjack Script


# Creating the deck 
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []

def create_deck():
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit])

create_deck()
