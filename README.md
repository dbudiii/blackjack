# blackjack

Step 1: Set game items and mechanics
 Items:
 - Dealer
 - Player
 - Deck of Cards

 Mechanics:
 - Counting the deck
 - Shuffling the deck
 - Hitting or passing
 - Game flow 
    1. Deck is shuffled
    2. Dealer passes one card to player, then to dealer, 2x. Only first dealer card is revealed.
    3. Dealer asks player if they want to hit or pass
    4. If player hits, player receives an extra card. Check if bust or OK. Repeats if they want to hit again.
    5. After passing, dealer flips second card that was hidden. Deals another card to himself if < 17. Checks if > 21 before and stops if > 17.
    6. Check who has higher card, then declare winner
 
 Bugs to fix:
 - ending the game whenever there is a bust
 - recognizing when there is blackjack