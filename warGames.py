#Vikram Guhilot
#Round 2 programming challenge

import random

card_suit = ['♠︎','♣︎','♥︎','♦︎']
card_weight = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#print(card_suit)
#print(card_weight)

class cardDeck:
    # Initilize a new deck of cards
    def __init__(self):
        self.cards = []
        for suit in card_suit:
            for weight in card_weight:
                self.cards.append((suit,weight))
        #print(self.cards)
    
    # Shuffle the new deck to randomize cards
    def shuffleDeck(self):
        print("Shuffeling")
        random.shuffle(self.cards)
        #print(self.cards)

    # returns two equally divided hands
    def serveCards(self):
        split1 = self.cards[:26]
        split2 = self.cards[26:]
        #print(self.cards)
        return (split1,split2)

card_deck = cardDeck()
card_deck.shuffleDeck()
hand1, hand2 = card_deck.serveCards()
#print(hand1)
