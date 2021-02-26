import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return (f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.deck = []
        
        for suit in "Diamonds", "Hearts", "Clubs", "Spades":
            for value in "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A":
                self.deck = Card(suit, value)
                print (self.deck)

    def shuffle(self):
        if len(self.deck) > 1:
            random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) > 1:
            delt_cards = self.deck.pop()
            return delt_cards

    def __repr__(self):
        return str(self.deck) 

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)


class Chips:
    def __init__(self):
        # private attribute so people can't see my money (or lack of)
        self.__total = 1000
        self.bet = 0

    def won_bet(self):
        self.total = self.bet + self.total

    def lost_bet(self):
        self.total = self.total - self.bet

    def push_bet(self):
        self.total = self.total

test_card = Card("Diamonds", "7")
test_deck = Deck()
test_shuffle = test_deck.shuffle
test_hand = Hand()
test_chips = Chips()
print("Card:", test_card)
print("")
print("Deck:", test_deck)
print("")
print("")
print("")
print("Shuffled Deck:", test_shuffle)
print("")
print("Hand:", test_hand)
print("")
print("Chips:", test_chips)