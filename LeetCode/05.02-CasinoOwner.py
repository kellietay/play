"""
Using a deck of cards, the player draws exactly N cards. 
Player wins if the sum of the values of all cards drawn is equal to W. 
For a given deck, compute N and W that minimize the probability of winning, 
such that the probability of winning is still > 0

Example:
Cards = {"1","1","2"}
N=1, W=1 gives 2/3 chance
N=1, W=2 gives 1/3 chance
N=2, W=2 gives 1/3 chance
N=2, W=3 gives 2/3 chance
In this case either N=1, W=2 or N=2, W=2 minimize the chances of winning

1. function to calculate probability of a given N and W
2. fuction to pass in valid N and W and store them, then return smallest probability that is not 0
- what is a valid N? 1 < N < len(cards). If N = len(cards), the prob will either be 0 or 100% so that is not a 'sane' value.
- what is a valid W? value of the smallest card < W < sum of all cards. If W = sum of all cards, prob will either be 0 or 100% so thats not a sane value. 
"""
from math import factorial

class Casino(object):
    def __init__(self,cards):
        self.smallest_card = 13
        self.sum_cards = 0

        for i,card in enumerate(cards):
            if card == "J":
                cards[i] = 11
            elif card == "D":
                cards[i] = 12
            elif card == "K":
                cards[i] = 13
            else:
                cards[i] = int(card)

            if cards[i] < self.smallest_card:
                self.smallest_card = cards[i]
            
            self.sum_cards += cards[i]

        self.cards = cards
        self.len_cards = len(cards)

    
    def minimizeWin(self):
        prob_dict = {}
        for N in range(1 , self.len_cards):
            for W in range(self.smallest_card, self.sum_cards):
                prob_value = self.calcProbability(N, W)
                if prob_value > 0:
                    if prob_dict.get((prob_value)):
                        prob_dict[(prob_value)].append((N,W))
                    else:
                        prob_dict[(prob_value)] = [(N,W)]
        print(prob_dict)
        return prob_dict[sorted(prob_dict)[0]]


    def calcProbability(self, N:int, W:int):
        combinations = factorial(self.len_cards)/(factorial(N) * factorial(self.len_cards-N))

        def helper(N, W, cards):
            wins = 0
            if W < 0: return 0
            if N == 0:
                if W == 0:
                    return 1
                else: 
                    return 0
            
            for i,card in enumerate(cards):
                wins += helper(N-1, W - card, cards[i+1:])
                
            return wins

        return helper(N,W,self.cards) / combinations


game1 = Casino(["1","1","2"])
print(game1.minimizeWin())

game2 = Casino(["1","2","3","4","5","J"])
print(game2.minimizeWin())
