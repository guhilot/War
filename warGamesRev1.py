#Vikram Guhilot
#Round 2 programming challenge

#Version: Shuffle when cards in hand are over and you have winning card pile
# Winning cards kept seperate till cards in hand finish, then winning cards are taken and shuffled

import random

card_suit = ['H','D','C','S']
card_weight = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

#total number of years the game lasts
year = 0 

#total number of wars
years_of_war = 0 

#stores cards won in rounds
botWins = []
humanWins = []

#stores input from user if they want to continue to next round
cont = '' 

#stores input from user if they want to continue to next round
reshuffle = ''  

#acts like a switch
flag = 0  

class cardDeck():
    # Initilize a new deck of cards
    def __init__(self):
        self.cards = []
        for suit in card_suit:
            for weight in card_weight:
                # assign weights to suit
                self.cards.append((suit,weight))
    
    # Shuffle the new deck to randomize cards
    def shuffleDeck(self):
        print("Shuffeling")
        random.shuffle(self.cards)

    # returns two equally divided hands
    def serveCards(self):
        split1 = self.cards[:26]
        split2 = self.cards[26:]
        return (split1,split2)

#creates a deck of cards
card_deck = cardDeck() 

#call the shuffle fn to shuffle cards
card_deck.shuffleDeck() 

#returns two hands of 26 cards each
hand1, hand2 = card_deck.serveCards() 

class playerHand():
    def __init__(self, hand):
        self.hand = hand

    #shows all cards of the user
    def show(self):
        return self.hand 

    #pops a card out of hand of cards for comparison
    def sendForward(self):
        return self.hand.pop() 

    # insert tuple/card to the start of the list
    def plunder(self,spoils):
        self.hand.insert(0,spoils) 

    #shuffles cards when there is lock (cards aligned in a way to cause extremely long loop)
    def shuffleHand(self):
        print("Shuffling hand")
        random.shuffle(self.hand) 

class Warriors():
    def __init__(self, clan, player):
        self.clan = clan
        self.player = player
    
    #displays both players cards
    def show(self):
        return self.player, self.clan 

    #returns the number of cards in players hand
    def standingArmy(self):
        return len(self.player.hand) 

    #returns a card for comparison
    def enterNegotiations(self):
        fighter = self.player.sendForward()
        print("{} has sent: {} to negotiate".format(self.clan,fighter))
        print('\n')
        return fighter 

    #if player has less than 2 cards return [] list as they cannot fight the war
    #else return two cards for the war comparison
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

# Create Warrior contestants and assigns them a hand
#asks player for their clan name
clan_name = input("Enter your clan name? ") 

#creates your team
human = Warriors(clan_name, player1hand) 

# creates computer team/ second player team needs to be
# modified to accept user input
bot = Warriors("Bot", player2hand)

# asks user if they want to start playing 
# Enter will start the game any other key will exit
cont = input(f'Do you want to enter arena? press enter to accept \n') 

#adds all the popped cards and facedown card to battlefield for winner grabs
def populate_battleGround():
    battle_ground.extend(botReinforcements)
    battle_ground.extend(humanReinforcements)
    battle_ground.append(botPlay)
    battle_ground.append(humanPlay)

def humanBackUpCheck(humanWins):
    human.player.hand.extend(humanWins)
    human.player.shuffleHand()
    humanWins = []
    return humanWins

def botBackUpCheck(botWins):
    bot.player.hand.extend(botWins)
    bot.player.shuffleHand()
    botWins = []
    return botWins

#checks for user input and if player has cards to play turn with
while cont == '' and human.standingArmy() != 0 and bot.standingArmy() != 0: 

#
# Copy paste print statements here if you want to see card movement (print statements at end of page)
#
    print("Bot Winning Pile Count",len(botWins))
    print(f'{human.clan} Winning Pile Count',len(humanWins))

    # year counts the number of rounds the game lasts
    year += 1  

    #option to shuffle at intervals of 50 turns user can shuffle or deny shuffling
    if year in range(50,5000,50):
        human.player.shuffleHand()
        bot.player.shuffleHand()

    print('\n')
    print("Year", year, '\n')

    #gives the stats of each team and the number of cards on hand
    print(f'{human.clan} has a standing army of {len(human.player.hand)} soldiers \n')
    print(f'{bot.clan} has a standing army of {len(bot.player.hand)} soldiers \n')

    #if the user has enough cards
    #battle_ground is the arena where negotiations or wars take place
    #empty arena where cards will be held for comparison and exchange
    battle_ground = [] 

    #clans send warrior into arena
    human_warrior = human.enterNegotiations() #human_warrior is the card for comparison from your team
    bot_warrior = bot.enterNegotiations() #bot_warrior is the card for comparison from computer team

    #warriors meet on battelground to decide their fate 
    #cards added to the holding/exchange list
    battle_ground.append(human_warrior)
    battle_ground.append(bot_warrior)

    #gets the value of the card (2 to A) and stores it in variable
    warriorPower = human_warrior[1]
    botPower = bot_warrior[1]

    #refills user hand with won card pile, if they finish all cards in hand
    if len(human.player.hand) == 0 and len(bot.player.hand) == 0:
        if len(humanWins) != 0 and len(botWins) != 0:
            humanWins = humanBackUpCheck(humanWins)
            botWins = botBackUpCheck(botWins)
        elif len(humanWins) != 0:
            flag = 1
            humanWins = humanBackUpCheck(humanWins)
        elif len(botWins) != 0:
            flag = 1
            botWins = botBackUpCheck(botWins)
    elif len(human.player.hand) == 0: 
        if len(humanWins) != 0:
            humanWins = humanBackUpCheck(humanWins)
    elif len(bot.player.hand) == 0:
        if len(botWins) != 0:
            botWins = botBackUpCheck(botWins)
    #if the cards are of equal weight
    if warriorPower == botPower and flag == 0:
        #this while loop is to encounter another round of equal weight cards where players enter a 2nd,3rd .. round of war
        while warriorPower == botPower : 
            
            years_of_war += 1

            print(f'{human.clan} and the {bot.clan} cannot come to an agreement\n')
            print("Prepare for doom, war is at your doorstep\n")
            print("Send in two of your warriors one hidden and one ready to fight\n")

            #list to hold two cards from each player
            humanReinforcements = []
            botReinforcements = []

            #either gets [] list or two cards depending on number of cards player has
            humanReinforcements = human.reinforce()
            botReinforcements = bot.reinforce()

            #condition to check that each player have enough cards for war
            #if not, checks to see if they have a winning pile of cards, if yes, extend
            #to the current empty hand, if not surrender
            if len(humanReinforcements) <= 1 and len(botReinforcements) <= 1:
                if len(humanWins) != 0 and len(botWins) != 0:
                    humanWins = humanBackUpCheck(humanWins)
                    botWins = botBackUpCheck(botWins)
                    humanReinforcements = human.reinforce()
                    botReinforcements = bot.reinforce()
                    humanPlay = humanReinforcements.pop()
                    botPlay = botReinforcements.pop()
                elif len(humanWins) != 0:
                    humanWins = humanBackUpCheck(humanWins)
                    humanReinforcements = human.reinforce()
                    humanPlay = humanReinforcements.pop()
                    botPlay = botReinforcements.pop()
                    bot.player.hand = []
                    flag = 1
                elif len(botWins) != 0:
                    botWins = botBackUpCheck(botWins)
                    botReinforcements = bot.reinforce()
                    botPlay = botReinforcements.pop()
                    humanPlay = humanReinforcements.pop()
                    human.player.hand = []
                    flag = 1
            elif len(humanReinforcements) <= 1:
                if len(humanWins) != 0:
                    humanWins = humanBackUpCheck(humanWins)
                    humanReinforcements = human.reinforce()
                    humanPlay = humanReinforcements.pop()
                    botPlay = botReinforcements.pop()
                else:
                    flag = 1
                    print("The human race has been taken over by the bots \n")
                    bot.player.hand.extend(human.player.hand)
                    bot.player.hand.extend(battle_ground)
                    human.player.hand = []
            elif len(botReinforcements) <= 1:
                if len(botWins) != 0:
                    botWins = botBackUpCheck(botWins)
                    botReinforcements = bot.reinforce()
                    botPlay = botReinforcements.pop()
                    humanPlay = humanReinforcements.pop()
                else:
                    print("The bots are no match to human intelligence \n")
                    flag = 1
                    human.player.hand.extend(bot.player.hand)
                    human.player.hand.extend(battle_ground)
                    bot.player.hand = []
            else:
                print("Let the reinforcements clash with the enemy \n")
                humanPlay = humanReinforcements.pop()
                botPlay = botReinforcements.pop()

                if len(human.player.hand) == 0 and len(bot.player.hand) == 0:
                    if len(humanWins) != 0 and len(botWins) != 0:
                        humanWins = humanBackUpCheck(humanWins)
                        botWins = botBackUpCheck(botWins)
                    elif len(humanWins) != 0:
                        flag = 1
                        humanWins = humanBackUpCheck(humanWins)
                    elif len(botWins) != 0:
                        flag = 1
                        botWins = botBackUpCheck(botWins)
                elif len(human.player.hand) == 0: #or len(human.player.hand) == 1:
                    if len(humanWins) != 0:
                        humanWins = humanBackUpCheck(humanWins)
                elif len(bot.player.hand) == 0: #or len(bot.player.hand) == 1:
                    if len(botWins) != 0:
                        botWins = botBackUpCheck(botWins)

            #displays the new cards for war comparison to break tie
            print(f'{human.clan} reinforcement is {humanPlay} \n')
            print(f'{bot.clan} reinforcement is {botPlay} \n')
            
            #check and see who has staronger card by getting index in list
            if flag == 0 and card_weight.index(humanPlay[1]) < card_weight.index(botPlay[1]):
                print(f'{bot.clan} wins, they take the reinforcements \n')
                #all popped cards are added back to to holding list which goes to winner
                populate_battleGround() 
                #as no duplicates in war card exist reinitialize to break loop
                warriorPower = -1 
                botWins.extend(battle_ground)
                #checkPlayerHandCount()

            elif flag == 0 and card_weight.index(humanPlay[1]) > card_weight.index(botPlay[1]):
                print(f'{human.clan} wins, we take the reinforcements \n')
                #all popped cards are added back to to holding list which goes to winner
                populate_battleGround()
                warriorPower = -1
                humanWins.extend(battle_ground)
                #checkPlayerHandCount()
            elif flag == 0 and card_weight.index(humanPlay[1]) == card_weight.index(botPlay[1]):
                #if war cards have the same weights add all cards to holding list
                #and update comparison condition with current weights to do another 
                #loop and get more cards for nth round of war
                print("Send in more reinforcements, both armies are equally strong \n")
                populate_battleGround()
                warriorPower = humanPlay[1]
                # updating loop condition parameters
                botPower = botPlay[1] 
            else:
                #if card weights are not equal initialize with false values to break loop
                warriorPower = -1
                botPower = 1 
    # if above conditions fail to trigger flag, extecute 
    elif flag == 0: 
        #compare card weight from list to get winner and then add cards to hand
        if card_weight.index(human_warrior[1]) > card_weight.index(bot_warrior[1]):
            print(f'{human.clan} wins, take soldier as tribute \n')
            humanWins.extend(battle_ground)

            # this condition checks number of cards in players hands, if 0 cards in hand, then it checks if they
            # have a winning pile to use, if so take the winning pile shuffle and play
            if len(human.player.hand) == 0 and len(bot.player.hand) == 0:
                if len(humanWins) != 0 and len(botWins) != 0:
                    human.player.hand.extend(humanWins)
                    human.player.shuffleHand()
                    humanWins = []
                    bot.player.hand.extend(botWins)
                    bot.player.shuffleHand()
                    botWins = []
            elif len(bot.player.hand) == 0:
                if len(botWins) != 0:
                    bot.player.hand.extend(botWins)
                    bot.player.shuffleHand()
                    botWins = []
            elif len(human.player.hand) == 0:
                if len(humanWins) != 0:
                    human.player.hand.extend(humanWins)
                    human.player.shuffleHand()
                    humanWins = []
        elif card_weight.index(human_warrior[1]) < card_weight.index(bot_warrior[1]):
            print(f'{bot.clan} wins, takes soldier as tribute\n')
            botWins.extend(battle_ground)

            # this condition checks number of cards in players hands, if 0 cards in hand, then it checks if they
            # have a winning pile to use, if so take the winning pile shuffle and play
            if len(human.player.hand) == 0 and len(bot.player.hand) == 0:
                if len(humanWins) != 0 and len(botWins) != 0:
                    human.player.hand.extend(humanWins)
                    human.player.shuffleHand()
                    humanWins = []
                    bot.player.hand.extend(botWins)
                    bot.player.shuffleHand()
                    botWins = []
            elif len(bot.player.hand) == 0:
                if len(botWins) != 0:
                    bot.player.hand.extend(botWins)
                    bot.player.shuffleHand()
                    botWins = []
            elif len(human.player.hand) == 0:
                if len(humanWins) != 0:
                    human.player.hand.extend(humanWins)
                    human.player.shuffleHand()
                    humanWins = []
            
    if human.standingArmy() == 0 or bot.standingArmy() == 0:
        cont = 'n'
    else:
        cont = input(f'Do you want to enter arena again? press enter to accept \n')

print(f'{year} years of existance')
print(f'{year - years_of_war} years of peace and compromise')
print(f'{years_of_war} years of plunder, pillage and war in this generation')

#displays the winner of the game based on number of cards on hand
if len(human.player.hand) > len(bot.player.hand):
    print(f'{human.clan} wins')
else:
    print(f'{bot.clan} wins')

######################################END#####################################
    # Put in first while loop to see stats

    # print("BotWins",len(botWins))
    # print("BotInHand", len(bot.player.hand))
    # print("BotInHandDiso", bot.player.show())
    # print("BotWinsDispo", botWins)
    # print('\n')
    # print("HumanWins",len(humanWins))
    # print("HumanInHand", len(human.player.hand))
    # print("HumanInHandDiso", human.player.show())
    # print("HumanWinDiso", humanWins)
    
    # print("Sum", len(botWins) + len(humanWins) + len(human.player.hand) + len(bot.player.hand))