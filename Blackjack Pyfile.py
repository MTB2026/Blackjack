import random

cardCategories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cardsList = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in cardCategories for card in cardsList]

# card values
def cardValue(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

# player's hand
def handScore(hand):
    score = sum(cardValue(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == 'Ace')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score


def showHands(playerCard, dealerCard):
    print(f"Dealer's hand: {dealerCard}  |  Score: {handScore(dealerCard)}")
    print(f"Player's hand: {playerCard}  |  Score: {handScore(playerCard)}")

random.shuffle(deck)
playerCard = [deck.pop(), deck.pop()]
dealerCard = [deck.pop(), deck.pop()]

while True:
    playerScore = handScore(playerCard)  
    print("Your hand:", playerCard)
    print("Your score:", playerScore)
    print()

    if playerScore > 21:
        showHands(playerCard, dealerCard)
        print("Bust! Dealer wins.")
        break

    choice = input('["Hit" for another card, "Stand" to stand]: ').lower()
    if choice == "hit":
        playerCard.append(deck.pop())
    elif choice == "stand":
        break
    else:
        print("Invalid choice. Please try again.")

else:
    pass  


while handScore(dealerCard) < 17:
    dealerCard.append(deck.pop())

playerScore = handScore(playerCard)
dealerScore = handScore(dealerCard)
showHands(playerCard, dealerCard)

# win logic
if playerScore > 21:
    print("Bust! Dealer wins.")
elif dealerScore > 21:
    print("Dealer busts! You win.")
elif playerScore > dealerScore:
    print("You win! Higher score than dealer.")
elif dealerScore > playerScore:
    print("Dealer wins. Higher score than you.")
else:
    print("It's a tie!")
