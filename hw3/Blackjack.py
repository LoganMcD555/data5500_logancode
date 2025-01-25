from deck_of_cards import *

# Function to calculate hand score with Ace adjustment
def calculate_score(hand):
    score = sum(card.val for card in hand)
    for card in hand:
        if card.face == "Ace" and score > 21:
            score -= 10
    return score

# Main Blackjack game logic
print("Welcome to Blackjack!")
deck = DeckOfCards()

while True:
    # Shuffle and print the deck
    print("\nDeck before shuffle:")
    deck.print_deck()
    deck.shuffle_deck()
    print("\nDeck after shuffle:")
    deck.print_deck()

    # Deal initial cards
    user_hand = [deck.get_card(), deck.get_card()]
    dealer_hand = [deck.get_card(), deck.get_card()]

    print("\nYour cards:", ", ".join(str(card) for card in user_hand))
    user_score = calculate_score(user_hand)
    print("Your score:", user_score)

    # User's turn
    while user_score < 21 and input("Would you like a hit? (y/n): ").lower() == 'y':
        user_hand.append(deck.get_card())
        user_score = calculate_score(user_hand)
        print("You got:", user_hand[-1], "| New score:", user_score)

    if user_score > 21:
        print("You busted! Dealer wins.")
    else:
        print("\nDealer's cards:", ", ".join(str(card) for card in dealer_hand))
        dealer_score = calculate_score(dealer_hand)
        print("Dealer's score:", dealer_score)

        # Dealer's turn
        while dealer_score < 17:
            dealer_hand.append(deck.get_card())
            dealer_score = calculate_score(dealer_hand)
            print("Dealer hits and gets:", dealer_hand[-1], "| Dealer's score:", dealer_score)

        # Determine the winner
        if dealer_score > 21:
            print("Dealer busted! You win!")
        elif user_score > dealer_score:
            print("You win!")
        elif dealer_score > user_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    # Replay option
    if input("\nPlay again? (y/n): ").lower() != 'y':
        print("Thanks for playing!")
        break



