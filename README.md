# Phase 10 Scorekeeper
Scorekeeper for the card game "Phase 10". Score is kept at the command line (cards are played in-person).

## Rules
From [Wikipedia](https://en.wikipedia.org/wiki/Phase_10):
> The game can be played by two to six people. The object of the game is to be the first person to complete all ten phases. 

> In the case of two players completing the last phase in the same hand, the player who completed the last phase with the lowest overall score is the winner. If those scores also happen to be tied, a tiebreaker round is played where the tying players attempt to complete phase ten (or in variants, the last phase each player had tried to complete in the previous round).


## Initialization 
Specify the number of players, and enter names based on the selection:

![Game Setup](/images/setup.jpg)

## Gameplay 
When one of the players has A) made their phase, and B) laid down all cards, the program checks the following for every *other* player (the winner moves to the next phase, with no points added to their score):
1. Did the player make their phase?
2. With how many points were they caught?
The information is then displayed below with the current standings:

![Gameplay](/images/gameplay.jpg)

This program becomes quite useful for tallying large scores, particularly with higher player counts:

![Gameplay - High Scores](/images/gameplay-1.jpg)

## Game Over
As soon as a player completes phase 10, the program checks to see if they are the only player having done so.
* If so, that player is declared the winner
* If not, all players that have completed Phase 10 have their scores checked; the lowest wins!

![Game Over](/images/gameover.jpg)


