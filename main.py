#           Our Blackjack House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The  Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.



import random
import os
import art


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    """Returns a random card from the card list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(data):
    """Takes the list of card and returns the calculated score """
    if len(data) == 2 and sum(data) == 21:
        return 0
    if 11 in data and sum(data) > 21:
        data.remove(11)
        data.append(1)
    return sum(data)


def compare(user_score, computer_score):
    """Reveals the winner """
    if user_score == computer_score:
        return "It's Draw 😁"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😔"
    elif user_score == 0:
        return "Win with Blackjack 🥳"
    elif user_score > 21:
        return "Lost, you went over 😔"
    elif computer_score > 21:
        return "Win, opponent went over 🥳"
    elif user_score > computer_score:
        return "You Win with highest score 🤑"
    else:
        return "You lost opponent scored more than you 😔"


def play_game():
    """This function is made if user doesn't want to play the game again"""
    print(art.logo)

    user_card = []
    computer_card = []
    is_game_over = False
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        """Calculates the scores of user and computer and shows the result"""
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"user_score cards : {user_card}  current score {user_score}")
        print(f"computer_score first card : {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("do you want to add another card : ").lower() == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        """Add cards to computer's deck until not more than 17"""
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand {user_card} and final score of {user_score}")
    print(f"Computer's final hand {computer_card} and final score of {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of Blackjack  , enter 'y' for yes and 'n' for no : ").lower() == "y":
    clear_screen()
    play_game()
