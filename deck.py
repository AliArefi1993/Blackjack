# deck.py
from random import randrange
##from tkinter.filedialog import askopenfilename, asksaveasfilename
from graphics import *
##from button import Button

##def readFile(filename):
##    infile = open(filename , 'r')
##    data = infile.readlines()
##    infile.close()
##    return data

def getchRank(rank):
        if rank == 1:
            ch1 = "Ace"
        elif 2 <= rank <= 10:
            ch1 = str(rank)
        elif rank == 11:
            ch1 = "Jack"
        elif rank == 12:
            ch1 = "Queen"
        elif rank == 13:
            ch1 = "King"
        return ch1

class Card:

    """ Represent a playing card."""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.rank <= 10:
            val = self.rank
        else:
            val = 10
        return val
    
    def cardDraw(self, win, center):
        filename = "PNG2\\" + str(self.rank) + str(self.suit) + ".png"
        pic = Image(center, filename)
        pic.draw(win)
        
    def __str__(self):
        rank = self.rank
        suit = self.suit
        if suit == "D":
            ch2 = "diamonds"
        elif suit == "C":
            ch2 = "clubs"
        elif suit == "H":
            ch2 = "hearts"
        elif suit == "S":
            ch2 = "spades"

        if rank == 1:
            ch1 = "Ace"
        elif 2 <= rank <= 10:
            ch1 = str(rank)
        elif rank == 11:
            ch1 = "Jack"
        elif rank == 12:
            ch1 = "Queen"
        elif rank == 13:
            ch1 = "King"

        return "{} of {}".format(ch1, ch2)

def num2suit(n):
    if n == 1:
        suit = "D"
    elif n == 2:
        suit = "C"
    elif n == 3:
        suit = "H"
    elif n == 4:
        suit = "S"
    return suit


class Deck:
    def __init__(self):
        suit = ['C', 'S', 'H', 'D']
        rank = list(range(1,14))
        cards = []
        for s in suit:
            for r in rank:
                cards.append(Card(r,s))
        self.cards = cards

    def shuffel(self):
        myList = self.cards
        n = len(myList)
        shuffList = []
        newList = []
        for i in range(n):
            newList.append(myList[i])
        for i in range(n):
            rnd = randrange(n)
            shuffList.append(newList[rnd])
            newList.remove(newList[rnd])
            n = n - 1
        self.cards = shuffList
        
    def giveCard(self ,n):
        hand = self.cards[:n]
        for c in hand:
            self.cards.remove(c)
        return hand
        
    def leftCard(self):
        return len(self.cards)
        
                
def main():
    mydeck = Deck()
    mydeckshuffel = mydeck.shuffel()
    a = mydeck.giveCard(13)
    b = mydeck.giveCard(13)
    e = mydeck.giveCard(13)
    d = mydeck.giveCard(13)
    
    for c in a:
        print(c)

    print("\n\n")
    for c in b:
        print(c)

    print("\n\n")
    for c in e:
        print(c)

    print("\n\n")
    for c in d:
        print(c)

    print("\n\n")
##    win = GraphWin("Game Card",1000,500)
##    win.setCoords(0,0,100,50)
##
##    mydeck = Deck()
##    mydeckshuffel = mydeck.shuffel()
##    center = Point(10,25)
##    n = int(input("Enter number of cards: "))
##    for i in range(n):
##        mydeck.dealCard().cardDraw(win, center)
##        center.move(2,0)
##    print("number of cards that left is:", mydeck.leftCard())
##    exitMsg = Text(Point(50, 40), "Click to Exit").draw(win)
##    exitMsg.setTextColor("red")
##    exitMsg.setStyle("bold")
##    win.getMouse()
##    win.close()
##

