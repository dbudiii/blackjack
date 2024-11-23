# Blackjack Script

import random

# Creating the deck 
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []
player_hand = []
dealer_hand = []

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

# Bust or not
def isBust(hand):
    isBust = False
    if count_hand_value(hand) > 21:
       isBust = True
    
    return isBust

# Dealing cards
def deal_card(hand):
    card = deck.pop(0)
    hand.append(card)

# # Ask player hitting / passing
# def hitting_ask():
#     while True:
#         answer = input("Would you like to hit or pass? H/P\n")
        
#         if answer == "H":
#             deal_card_player()
#             print("Your new deck value is: " + count_hand_value(player_hand))
            
#             if isBust(player_hand):
#                 print("You have busted. The game is over.")
#                 break

#         elif answer == "P":
#             break

#         else:
#             print("Answer is invalid. Please choose hit or pass")



# Check Dealer hands hitting / passing

# Game logic
create_deck()
