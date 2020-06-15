#Vikram Guhilot
#Round 2 programming challenge

import random

card_suit = ['♠︎','♣︎','♥︎','♦︎']
card_weight = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
year = 0
years_of_war = 0
botWins = 0
humanWins = 0
cont = ''
reshuffle = ''
flag = 0

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

class playerHand():
    def __init__(self, hand):
        self.hand = hand

    def show(self):
        return self.hand

    def sendForward(self):
        return self.hand.pop()

    def plunder(self,spoils):
        self.hand.insert(0,spoils) # insert to the start of the list

    def shuffleHand(self):
        print("Shuffling hand")
        random.shuffle(self.hand)

class Warriors():
    def __init__(self, clan, player):
        self.clan = clan
        self.player = player
    
    def show(self):
        return self.player, self.clan

    def standingArmy(self):
        return len(self.player.hand)

    def enterNegotiations(self):
        fighter = self.player.sendForward()
        print("{} has sent: {} to negotiate".format(self.clan,fighter))
        print('\n')
        return fighter

    def reinforce(self):
        warTeam = []
        if len(self.player.hand) < 2:
            return warTeam
        else:
            for x in range(2):
                warTeam.append(self.player.hand.pop())
            return warTeam

player1hand = playerHand(hand1)
player2hand = playerHand(hand2)

#print(player1hand.show())
#print(player2hand.show())

# Create Warrior contestants and assigns them a hand
clan_name = input("Enter your clan name? ")
human = Warriors(clan_name, player1hand)
bot = Warriors("Bot", player2hand)

#a, b = human.show()
#print(b, a.show())
#print(human.standingArmy())
cont = input(f'Do you want to enter arena? press enter to accept \n')
while cont == '' and human.standingArmy() != 0 and bot.standingArmy() != 0:
    # year counts the number of rounds the game lasts
    year += 1

    #cont = input(f'Do you want to enter arena again? press enter to accept ')

    if year in range(50,5000,300):
        reshuffle = input("Lets re-arrange our forces ('y' to reshuffle existing hand) \n")

    if reshuffle == 'y':
        human.player.shuffleHand()
        bot.player.shuffleHand()
    reshuffle = ''
    print('\n')
    print("Year", year, '\n')
    print(f'{human.clan} has a standing army of {len(human.player.hand)} soldiers \n')
    print(f'{bot.clan} has a standing army of {len(bot.player.hand)} soldiers \n')

    #if user has 0 or 1 card the game is declared as 
    #there is a potential for war without reinforcements
    #to back up during war

    if len(human.player.hand) == 0 or len(human.player.hand) == 1:
        #print(human.player.show()) # View remaining cards
        flag = 1 # condition breaker
        bot.player.hand.extend(human.player.hand) # takes all remaining warriors
        human.player.hand = []
        print(f'{human.clan} surrenders to the mighty {bot.clan}')
    elif len(bot.player.hand) == 0 or len(bot.player.hand) == 1:
        #print(bot.player.show()) # View remaining cards
        flag = 1
        human.player.hand.extend(bot.player.hand)
        bot.player.hand = []
        print(f'{bot.clan} surrenders to the mighty {human.clan}')
    else:
        #battle_ground is the arena where negotiations or wars take place
        battle_ground = []

        #clans send warrior into arena
        human_warrior = human.enterNegotiations()
        bot_warrior = bot.enterNegotiations()

        #warriors meet on battelground to decide their fate 
        battle_ground.append(human_warrior)
        battle_ground.append(bot_warrior)
        #print(human_warrior[1], bot_warrior[1])
        warriorPower = human_warrior[1]
        botPower = bot_warrior[1]
    #counter = 0
    if warriorPower == botPower:
        while warriorPower == botPower :
            years_of_war += 1
            print(f'{human.clan} and the {bot.clan} cannot come to an agreement\n')
            print("Prepare for doom, war in on you doorstep\n")
            print("Send in two of your warriors one hidden and one ready to fight\n")

            humanReinforcements = []
            botReinforcements = []

            humanReinforcements = human.reinforce()
            botReinforcements = bot.reinforce()
            

            if len(humanReinforcements) == 0 or len(humanReinforcements) == 1:
                print("The human race has been taken over by the bots \n")
                flag = 1
                bot.player.hand.extend(human.player.hand)
                bot.player.hand.extend(battle_ground)
                human.player.hand = []
            elif len(botReinforcements) == 0 or len(botReinforcements) == 1:
                print("The bots are no match to human intelligence \n")
                flag = 1
                human.player.hand.extend(bot.player.hand)
                human.player.hand.extend(battle_ground)
                bot.player.hand = []
            else:
                print("Let the reinforcements clash with the enemy \n")
                humanPlay = humanReinforcements.pop()
                botPlay = botReinforcements.pop()

            print(f'{human.clan} reinforcement is {humanPlay} \n')
            print(f'{bot.clan} reinforcement is {botPlay} \n')
            
            #check and see who has stronger reinforcement

            if flag == 0 and card_weight.index(humanPlay[1]) < card_weight.index(botPlay[1]):
                print('Bots Win, they take the reinforcements \n')
                battle_ground.extend(botReinforcements) # list
                battle_ground.extend(humanReinforcements) # list
                battle_ground.append(botPlay) # tuple
                battle_ground.append(humanPlay) # tuple
                warriorPower = -1
                for soldier in battle_ground:
                    bot.player.plunder(soldier) # insert to the start of the list (hand)
            elif flag == 0 and card_weight.index(humanPlay[1]) > card_weight.index(botPlay[1]):
                print('We Win, we take the reinforcements \n')
                battle_ground.extend(botReinforcements)
                battle_ground.extend(humanReinforcements)
                battle_ground.append(botPlay)
                battle_ground.append(humanPlay)
                warriorPower = -1
                for soldier in battle_ground:
                    human.player.plunder(soldier) # insert to the start of the list (hand)
            elif flag == 0 and card_weight.index(humanPlay[1]) == card_weight.index(botPlay[1]):
                print("Send in more reinforcements, both armies are equally strong \n")
                battle_ground.extend(botReinforcements)
                battle_ground.extend(humanReinforcements)
                battle_ground.append(botPlay)
                battle_ground.append(humanPlay)
                warriorPower = humanPlay[1]
                botPower = botPlay[1]
            else:
                warriorPower = -1
                botPower = 1
    elif flag == 0:
        if card_weight.index(human_warrior[1]) > card_weight.index(bot_warrior[1]):
            print(f'{human.clan} wins, take soldier as tribute \n')
            for j in battle_ground:
                human.player.plunder(j)
            #a, b = human.show()
        elif card_weight.index(human_warrior[1]) < card_weight.index(bot_warrior[1]):
            print(f'{bot.clan} wins, takes soldier as tribute\n')
            for j in battle_ground:
                bot.player.plunder(j)
            #c, d = bot.show()
    if human.standingArmy() == 0 or bot.standingArmy() == 0:
        cont = 'n'
    else:
        cont = input(f'Do you want to enter arena again? press enter to accept ')

print(f'{year} years of existance')
print(f'{year - years_of_war} years of peace and compromise')
print(f'{years_of_war} years of plunder, pillage and war in this generation')

if len(human.player.hand) > len(bot.player.hand):
    print(f'{human.clan} wins')
else:
    print(f'{bot.clan} wins')

