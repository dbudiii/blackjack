# Blackjack Script

import random

# Creating the deck 
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []
player_hand = []

def create_deck():
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit])
            random.shuffle(deck)

# Counting value of hand
def count_hand_value(hand):
    total_value = 0
    ace_count = 0

    for card in hand:
        rank, suit = card

        if rank in ['Jack', 'Queen', 'King']:
            total_value += 10
        elif rank == 'Ace':
            total_value += 11
            ace_count += 1
        else:
            total_value += int(rank)
    
    if total_value > 21 and ace_count > 0:
        total_value -= 10
        ace_count -= 1
    
    return total_value

player_hand = [['Ace', 'Clubs'], ['Ace', 'Diamonds']]
print(count_hand_value(player_hand))