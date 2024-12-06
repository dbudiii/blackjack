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

# Ask player hitting / passing
def hitting_ask():
    while True:
        answer = input("Would you like to hit or pass? H/P\n")
        
        if answer == "H":
            deal_card(player_hand)
            print("Your new deck value is: " + str(count_hand_value(player_hand)))
            
            if isBust(player_hand):
                print("You have busted. The game is over.") 
                break
            
            elif count_hand_value(player_hand) == 21:
                break

        elif answer == "P":
            break

        else:
            print("Answer is invalid. Please choose hit or pass")


# Game logic
create_deck()

player_hand_value = 0
dealer_hand_value = 0

while True:
    # deal cards to player and dealer
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)

    # show first card of dealer
    print(dealer_hand[0])
    
    # showing player hand and value
    print(player_hand)
    player_hand_value = count_hand_value(player_hand)
    print("Your hand value is: " + str(player_hand_value))

    # hitting ask
    hitting_ask()

    # dealer shows full hand
    print("The dealer will now reveal his full hand.")
    print(dealer_hand)
    dealer_hand_value = count_hand_value(dealer_hand)
    print("The dealer's value is: " + str(dealer_hand_value))

    # logic to determine if dealer will hit or stay
    if dealer_hand_value < 17:
        print("The dealer will now hit.")

        while dealer_hand_value < 17:
            deal_card(dealer_hand)
            dealer_hand_value = count_hand_value(dealer_hand)
            print("The dealer's new hand value is: " + str(dealer_hand_value))

            if dealer_hand_value > 21:
                print("Dealer busts. You win.")
                break
    else:
        print("The dealer stays.")

    # logic to compare player vs. dealer hands
    if dealer_hand_value > player_hand_value:
        print("The dealer wins.")
        break
    
    elif dealer_hand_value < player_hand_value:
        print("You win.")
        break

    else: 
        print("You tie.")
        break