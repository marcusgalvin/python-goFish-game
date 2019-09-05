import random

deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6,
        6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "king", "king", "king", "king", "ace", "ace", "ace", "ace"]

# print(len(deck))
computers_cards = []
players_cards = []

computers_matches = []
players_matches = []

computer_matches_dub = []


# def main():


print("Welcome to GO FISH")

# set the computer and players cards to 8 random items from the deck list
computer_cards = random.sample(deck, k=8)
players_cards = random.sample(deck, k=8)

print ("computer chooses these 8 random cards",
       computer_cards)

print ("user chooses these 8 random cards",
       players_cards)

# find matches in the computers cards
computer_matches = set(
    [x for x in computer_cards if computer_cards.count(x) > 1])

print("computers matches: ", computer_matches)

# once the computer finds its matches, we must duplicate the list to show that the computer has two of each card
for item in computer_matches:
    computer_matches_dub.extend([item, item])
    print(computer_matches_dub)


#  for i in range computer_cards:
#    if computer_cards[0] ==


# if __name__ == '__main__':
#         main()
