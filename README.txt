*************READ ME*************

This project has two versions

Version 1.0 : warGames.py
Version 1.1 : warGamesRev1.py

1) After running and starting the game

2) Press enter for a new round or any key to exit the game

3) If you exit the game before it ends the winner will be decided bases on number of cards in hand

4) If the users both throw a card with same weight a war is declared at this time each user removes
   two more cards from hand, from theses two cards only one will be used to break the tie, the winning
   card takes all, however, if there is another tie the war continues and the players draw two more cards
   and only use one to compare and break tie, this process goes on till a winner is decided and hence the
   winner take all cards on table

   For Version 1.0 : winning cards are inserted to the start of the current hand being played
   For Version 1.1 : winning cards are stored into a seperate list and not inserted into the playing hand
   on finishing cards in hand the player then takes the pile of won cards shuffles and starts playing again

5) In the event if a user throws one card which results in war and only has one card in hand the game is 
   declared in favor of team who can provide all cards for war to take place ie. two cards

6) The system prompts the user if they want to shuffle cards at 50 turn intervals in case there is a need 
   to shuffle to spice up a long boring game


Experiment:
Had two volunteers play the game and the results were as I expected with a wide average game length of 
600 to 1500 rounds, volunteers reported scenarios with player not having enough cards during war, scenario 
where wars took place back to back as the most complex cases, or coming to a deadlock where its a back and 
forth match(case for shuffling), these scenarios have been coded to function properly. At the end the 
volunteers decided to never play this game again --lol

Time and Ideas:
If I were given more time and had the bandwith after work, I would definetely research into how I could 
use React to give this game a UI on the web where two people sitting anywhere in the world could play it
I would also add few more unit tests to make sure it is robust and that I am doing my part, as it is essential for
a good programmer to write his/her own unit tests before walking away, this coding challenge made me brush up
on my python skills and I enjoyed every minute coding with it, I shall do a deep dive into python too and 
redo this assignment to see where I could do better and cut down on some of the complexity, I am currently also 
working on the feature in which the user puts his winning cards at the bottom of his/her stack, when the face card 
becomes visible, the user shuffles his cards and continues, 

Assumptions:
1)If a user does not have enough cards for a war round, the game is declared in favour of the team with most 
cards as they can fulfill the war rules

2)Cards are inserted to start of the list as we pop from the back of the list to play the game

3)Uesr would like to decide when to shuffle instead of hand being automatically shuffled at 50 rounds intervals
User will be promped 

Coner cases:
1)User does not have enough cards for war: When this scenario occurs, I had the option of having the user throw 
the only card in hand for war, however on one hand that is not fair and on the other hand what if there is another 
tie, hence the player is in a bad situation, the strategy I used was for the user in this case to surrender to the 
other player

2)War happens contiguously(back to back): In this scenario when there is a tie in the second.. round, ie both players 
throw cards with same weight, I needed to create a seperate loop inside the main loop to handle this as there 
could be 'n' number of continuous wars, hence I created a while loop whose conditional parameters were updated with the 
current war card values, if they were equal weights loop again and have a war, if they were different condition fails 
and exits out of the loop and proceed to play in the normal flow

3)Cards align such that there is an endless back and forth: In a case as such, the game can go on for a really really long
time, where players cards are alligned in such a way where each player wins in every alternate round causing their armies
to have the same number of fighters, I included a count and at every 50 turns the user gets a prompt to shuffle if they feel
there is a need, it definetely helps

4)Player has 3 cards in hand and 0 winnings in pile, throws one card causing a war, player has to now put down both cards 
in hand, when player uses one of his cards from the 2 card entry and this causes another war, at this point, the game is 
surrendered to the other player
