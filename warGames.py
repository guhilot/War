#Vikram Guhilot
#Round 2 programming challenge

import random

card_suit = ['H','D','C','S']
card_weight = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
year = 0 #total number of years the game lasts
years_of_war = 0 #total number of wars
botWins = []
humanWins = []
cont = '' #stores input from user if they want to continue to next round
reshuffle = ''  #stores input from user if they want to continue to next round
flag = 0  #acts like a switch

class cardDeck:
    # Initilize a new deck of cards
    def __init__(self):
        self.cards = []
        for suit in card_suit:
            for weight in card_weight:
                self.cards.append((suit,weight))# assign weights to suit
    
    # Shuffle the new deck to randomize cards
    def shuffleDeck(self):
        print("Shuffeling")
        random.shuffle(self.cards)

    # returns two equally divided hands
    def serveCards(self):
        split1 = self.cards[:26]
        split2 = self.cards[26:]
        return (split1,split2)

card_deck = cardDeck() #creates a deck of cards
card_deck.shuffleDeck() #call the shuffle fn to shuffle cards
hand1, hand2 = card_deck.serveCards() #returns two hands of 26 cards each

class playerHand():
    def __init__(self, hand):
        self.hand = hand

    def show(self):
        return self.hand #shows all cards of the user

    def sendForward(self):
        return self.hand.pop() #pops a card out of hand of cards for comparison

    def plunder(self,spoils):
        self.hand.insert(0,spoils) # insert tuple/card to the start of the list

    def shuffleHand(self):
        print("Shuffling hand")
        random.shuffle(self.hand) #shuffles cards when there is lock (cards aligned in a way to cause extremely long loop)

class Warriors():
    def __init__(self, clan, player):
        self.clan = clan
        self.player = player
    
    def show(self):
        return self.player, self.clan #displays both players cards

    def standingArmy(self):
        return len(self.player.hand) #returns the number of cards in players hand

    def enterNegotiations(self):
        fighter = self.player.sendForward()
        print("{} has sent: {} to negotiate".format(self.clan,fighter))
        print('\n')
        return fighter #returns a card for comparison

    def reinforce(self):
        warTeam = []
        if len(self.player.hand) < 2:
            return warTeam # if player has less than 2 cards return [] list as they cannot fight the war
        else:
            for x in range(2):
                warTeam.append(self.player.hand.pop())
            return warTeam # return two cards for the war comparison

player1hand = playerHand(hand1)
player2hand = playerHand(hand2)

# Create Warrior contestants and assigns them a hand
clan_name = input("Enter your clan name? ") # asks player for their clan name
human = Warriors(clan_name, player1hand) #creates your team
bot = Warriors("Bot", player2hand) # creates computer team/ second player team needs to be
                                   # modified to accept user input

cont = input(f'Do you want to enter arena? press enter to accept \n') # asks user if they want to start playing 
                                                                      # Enter will start the game any other key will exit

#adds all the popped cards and facedown card to battlefield for winner grabs
def populate_battleGround():
    battle_ground.extend(botReinforcements)
    battle_ground.extend(humanReinforcements)
    battle_ground.append(botPlay)
    battle_ground.append(humanPlay)

while cont == '' and human.standingArmy() != 0 and bot.standingArmy() != 0: #checks for user input and if player has cards to play turn with
    print("BotWins", botWins)
    print("HumanWins",humanWins)
    year += 1  # year counts the number of rounds the game lasts

    #cont = input(f'Do you want to enter arena again? press enter to accept ')

    #option to shuffle at intervals of 50 turns user can shuffle or deny shuffling
    if year in range(50,5000,50):
        reshuffle = input("Lets re-arrange our forces ('y' to reshuffle existing hand) \n")

    #if user agrees to shuffle both player cards get shuffled
    if reshuffle == 'y':
        human.player.shuffleHand()
        bot.player.shuffleHand()

    reshuffle = '' #reinitialize to avoid shuffling at every turn

    print('\n')
    print("Year", year, '\n')

    #gives the stats of each team and the number of cards on hand
    print(f'{human.clan} has a standing army of {len(human.player.hand)} soldiers \n')
    print(f'{bot.clan} has a standing army of {len(bot.player.hand)} soldiers \n')

    #if user has 0 or 1 card the game is declared as 
    #there is a potential for war without reinforcements
    #to back up during war
    if len(human.player.hand) == 0 or len(human.player.hand) == 1:

        if len(humanWins) != 0:
            human.player.hand.extend(humanWins)
            human.player.shuffleHand()
            humanWins = []
        else:
            flag = 1 # condition breaker
            bot.player.hand.extend(human.player.hand) # takes all remaining warriors
            human.player.hand = []
            print(f'{human.clan} surrenders to the mighty {bot.clan}')
    elif len(bot.player.hand) == 0 or len(bot.player.hand) == 1:
        if len(botWins) != 0:
            bot.player.hand.extend(botWins)
            bot.player.shuffleHand()
            botWins = []
        else:
            flag = 1
            human.player.hand.extend(bot.player.hand)
            bot.player.hand = []
            print(f'{bot.clan} surrenders to the mighty {human.clan}\n')
    else:
        #if the user has enough cards
        #battle_ground is the arena where negotiations or wars take place
        battle_ground = [] #empty arena where cards will be held for comparison and exchange

        #clans send warrior into arena
        human_warrior = human.enterNegotiations() #human_warrior is the card for comparison from your team
        bot_warrior = bot.enterNegotiations() #bot_warrior is the card for comparison from computer team

        #warriors meet on battelground to decide their fate 
        # cards added to the holding/exchange list
        battle_ground.append(human_warrior)
        battle_ground.append(bot_warrior)

        #gets the value of the card (2 to A) and stores it in variable
        warriorPower = human_warrior[1]
        botPower = bot_warrior[1]
    
    #if the cards are of equal weight
    if warriorPower == botPower:
        while warriorPower == botPower : #this while loop is to encounter another round of equal weight cards where players enter a 2nd,3rd .. round of war
            
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
            
            #checks to see if any player is out of cards or has only one card, if so
            #the player cannot win the war and has to surrender by giving up card
            #if they have enough cards to fight the war one card from each is taken out for
            #comparison
            if len(humanReinforcements) == 0 or len(humanReinforcements) == 1:
                if len(humanWins) != 0:
                    human.player.hand.extend(humanWins)
                    human.player.shuffleHand()
                    humanWins = []
                else: 
                    print("The human race has been taken over by the bots \n")
                    flag = 1
                    bot.player.hand.extend(human.player.hand)
                    bot.player.hand.extend(battle_ground)
                    human.player.hand = []
            elif len(botReinforcements) == 0 or len(botReinforcements) == 1:
                if len(botWins) != 0:
                    bot.player.hand.extend(botWins)
                    bot.player.shuffleHand()
                    botWins = []
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

            #displays the new cards for war comparison to break tie
            print(f'{human.clan} reinforcement is {humanPlay} \n')
            print(f'{bot.clan} reinforcement is {botPlay} \n')
            
            #check and see who has staronger card by getting index in list
            if flag == 0 and card_weight.index(humanPlay[1]) < card_weight.index(botPlay[1]):
                print(f'{bot.clan} wins, they take the reinforcements \n')
                populate_battleGround() #all popped cards are added back to to holding list which goes to winner
                warriorPower = -1 #as no duplicates in war card exist reinitialize to break loop
                # for soldier in battle_ground:
                #     bot.player.plunder(soldier) # insert to the start of the list (hand) to avoid immidiate reuse as cards are being popped from end of list
                botWins.extend(battle_ground)
            elif flag == 0 and card_weight.index(humanPlay[1]) > card_weight.index(botPlay[1]):
                print(f'{human.clan} wins, we take the reinforcements \n')
                populate_battleGround()#all popped cards are added back to to holding list which goes to winner
                warriorPower = -1
                # for soldier in battle_ground:
                #     human.player.plunder(soldier) # insert to the start of the list (hand) to avoid immidiate reuse as cards are being popped from end of list
                humanWins.extend(battle_ground)
            elif flag == 0 and card_weight.index(humanPlay[1]) == card_weight.index(botPlay[1]):
                #if war cards have the same weights add all cards to holding list
                #and update comparison condition with current weights to do another 
                #loop and get more cards for nth round of war
                print("Send in more reinforcements, both armies are equally strong \n")
                populate_battleGround()
                warriorPower = humanPlay[1]
                botPower = botPlay[1] # updating loop condition parameters
            else:
                warriorPower = -1
                botPower = 1 #if card weights are not equal initialize with false values to break loop
    elif flag == 0: # if above conditions fail to trigger flag
        #compare card weight from list to get winner and then add cards to hand
        if card_weight.index(human_warrior[1]) > card_weight.index(bot_warrior[1]):
            print(f'{human.clan} wins, take soldier as tribute \n')
            # for j in battle_ground:
            #     human.player.plunder(j)
            humanWins.extend(battle_ground)
        elif card_weight.index(human_warrior[1]) < card_weight.index(bot_warrior[1]):
            print(f'{bot.clan} wins, takes soldier as tribute\n')
            # for j in battle_ground:
            #     bot.player.plunder(j)
            botWins.extend(battle_ground)

    if human.standingArmy() == 0 or bot.standingArmy() == 0:
        cont = 'n'
    else:
        cont = input(f'Do you want to enter arena again? press enter to accept ')

print(f'{year} years of existance')
print(f'{year - years_of_war} years of peace and compromise')
print(f'{years_of_war} years of plunder, pillage and war in this generation')

#displays the winner of the game based on number of cards on hand
if len(human.player.hand) > len(bot.player.hand):
    print(f'{human.clan} wins')
else:
    print(f'{bot.clan} wins')
