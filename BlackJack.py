#!usr/bin/env python

# BlackJack.py
# Author: Phillip Taylor

from random import shuffle

class BlackJack(object):

    def __init__(self):
        self.deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
        self.dealerHand = []
        self.playerHand = []
        self.dealerTotal = 0
        self.playerTotal = 0

   # deal card to hand
    def deal(self):
        hand = []
        total = 0
        for i in range(2):
            shuffle(self.deck)
            card = self.deck.pop(i)
            if card > 10:
                card = self.convertToLetter(card)
            hand.append(card)
            total = self.addToTotal(card, total)
        return hand, total


    def hit(self, hand, total):
        card = self.deck.pop()
        if card > 10:
            card = self.convertToLetter(card)
        hand.append(card)
        total = self.addToTotal(card, total)
        return hand, total


    def addToTotal(self, card, total):
        if not isinstance(card, int):
            if card != 'A':
              total += 10
            else:
                if total > 10:
                    total += 1
                else:
                    total += 11
        else:
            total += card
        return total


     # convert card numbers to face cards
    def convertToLetter(self, card):
         if card == 11:
             card = 'J'
         if card == 12:
             card = 'Q'
         if card == 13:
             card = 'K'
         if card == 14:
             card = 'A'
         return card

    def begin(self):
        self.playerHand, self.playerTotal = self.deal()
        self.dealerHand, self.dealerTotal = self.deal()


    def evaluate(self, option):
        if self.playerTotal == 21:
            print('Blackjack! You win!')

        elif self.playerTotal > 21 :
            print('You busted! Sorry, you lose.')

        elif self.dealerTotal == 21:
            print('Dealer has blackjack... Sorry, you lose.')

        elif self.dealerTotal > 21:
            print('Dealer has busted - you win!')

        elif self.dealerTotal > self.playerTotal and option == 's':
            print('Dealer has a higher hand... Sorry, you lose.')

        elif self.playerTotal > self.dealerTotal and option == 's':
            print('You have the higher hand - you win!')



    def move(self, option):
        option = option.lower()
        if option == 'h':
            self.playerHand, self.playerTotal = self.hit(self.playerHand, self.playerTotal)
            if self.dealerTotal < 17:
                self.dealerHand, self.dealerTotal = self.hit(self.dealerHand, self.dealerTotal)

        elif option == 's':
            while self.dealerTotal < 17:
                self.dealerHand, self.dealerTotal = self.hit(self.dealerHand, self.dealerTotal)

        elif option == 'q':
            print('Thank you for playing!')
            exit(0)

        else:
            print('invalid input.')

    def printHands(self):
        print('The dealer has ' + str(self.dealerHand) + ', totaling ' + str(self.dealerTotal))
        print('You have '+ str(self.playerHand) + ', totaling ' + str(self.playerTotal))

def main():
    option = 0
    game = BlackJack()
    print('Welcome to Blackjack!')
    game.begin()

    while option != 'q':
        game.printHands()
        option = input('press h for hit, s for stay, and q for quit: ')
        game.move(option)
        game.evaluate(option)
        if option == 's' or option == 'q':
            again = input('play again? [y/n] ').lower()
            if again == 'y':
                game = BlackJack()
                game.begin()
            elif again == 'n':
                print('Thank you for playing!')
                exit(0)

if __name__ == '__main__':
    main()
