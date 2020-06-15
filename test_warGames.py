import unittest
import warGames
from warGames import cardDeck
from warGames import playerHand
from warGames import Warriors

class TestWarGames(unittest.TestCase):

    card_suit = ['H','D','C','S']
    card_weight = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    def test_serveCards_returns_26Cards_for_EachPlayer(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        self.assertEqual(len(share1),len(share2))

    def test_serveCards_unique_Hands(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        self.assertNotEqual(share1, share2)

    def test_shuffleDeck(self):
        deck = cardDeck()
        self.assertNotEqual(deck,deck.shuffleDeck())

    def test_plunder(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        b = playerHand(share2)
        a.plunder(('Z','ZZ'))
        b.plunder(('Z','ZZ'))
        self.assertEqual(len(share1), len(share2))

    def test_plunder_one(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        b = playerHand(share2)
        a.plunder(('Z','ZZ'))
        self.assertNotEqual(len(share1), len(share2))
    
    def test_plunder_count_on_win_firstRound(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        b = playerHand(share2)
        a.plunder(('Z','ZZ'))
        self.assertEqual(len(share1), 27)

    def test_sendForward_entersCard_to_table(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        b = playerHand(share2)
        a.sendForward()
        self.assertNotEqual(len(share1), len(share2))

    def test_sendForward_Handequals25_At_FirstPlay(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        b = playerHand(share2)
        a.sendForward()
        self.assertEqual(len(share1), 25)

    def test_shuffleHand_shuffles_current_hand(self): 
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        hold = share1
        a = playerHand(share1)
        self.assertNotEqual(hold,a.shuffleHand())

    def test_enterNegotiations_firstRound(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        aa = soldier.enterNegotiations()
        self.assertEqual(aa, ('D', 'A'))
    
    def test_enterNegotiations_secondRound(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        aa = soldier.enterNegotiations()
        bb = soldier.enterNegotiations()
        self.assertEqual(bb, ('D', 'K'))

    def test_reinforce_returns_emptyList_when0cardsOnHand_During_War(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        soldier.player.hand = []
        hold = soldier.reinforce()
        self.assertEqual(len(hold), len([]))

    def test_reinforce_return_2_CardsWhenHasMoreThan2Cards_During_War(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        hold = soldier.reinforce()
        self.assertEqual(len(hold), 2)
    
    def test_reinforce_return_emptyListWhen1cardOnHand_During_War(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        soldier.player.hand = []
        soldier.player.hand.append(('H','A'))
        hold = soldier.reinforce()
        self.assertEqual(len(hold), 0)

    def test_reinforce_return_2CardsWhenOnly_2_cardOnHand_During_War(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        soldier.player.hand = []
        soldier.player.hand.append(('H','A'))
        soldier.player.hand.append(('H','K'))
        hold = soldier.reinforce()
        self.assertEqual(len(hold), 2)

    def test_standingArmy(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        self.assertTrue(soldier.standingArmy()>0)

    def test_standingArmy_NotTrue(self):
        deck = cardDeck()
        share1, share2 = deck.serveCards()
        a = playerHand(share1)
        soldier = Warriors('Vikram',a)
        soldier.player.hand = []
        self.assertFalse(soldier.standingArmy()>1)

if __name__ == '__main__':
    unittest.main()