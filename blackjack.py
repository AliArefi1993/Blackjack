#   blackjack.py
# This program simulate a blackjack game

from deck import Deck

class Blackjack:
    
    def __init__(self, interface):
        self.interface = interface
        self.deck = Deck()
        self.deck.shuffel()
        self.dealer = Player("Dealer", "Dealer")

    def run(self):
        " run the game"
        self.done = False
        self.getNames()
        cash = self.interface.getEachPlayerStartCash()
        for p in self.players:
            p.setCash(cash)
        self.playGame()

    def playGame(self):
        while True:
            if not self.interface.startGame():
                break
            self.interface.resetWindow()
            self.bets = self.interface.getBets()
            self.deck = Deck()
            self.deck.shuffel()
            for i in range(3):
                self.players[i].setBet(self.bets[i])
            for p in self.players:
                self.interface.showGameInf("{}  (bet=${})".format(p.getName(), p.getBet()),p.getPos())
                p.removeCards()
                p.addCards(self.deck.giveCard(2))
                self.interface.showCards(p.getCards(), p.getPos())
            self.dealer.removeCards()
            self.dealer.addCards(self.deck.giveCard(2))
            self.interface.showCards(self.dealer.getCards()[0:1], self.dealer.getPos())
            doublePlays = []
            for p in self.players:
                if p.getCards()[0].getRank() == p.getCards()[1].getRank():
                    double = self.interface.askDouble(p.pos)
                    if double:
                        q = p.clone()
                        p.removeOneCard()
                        p.addCards(self.deck.giveCard(1))
                        self.interface.showCards(p.getCards(), p.getPos())
                        q.addCards(self.deck.giveCard(1))
                        self.interface.showCards(q.getCards(), q.getPos())
                        self.playOneGame(q)
                        doublePlays.append(q)
                self.playOneGame(p)
            self.playOneGame(self.dealer)
            for q in doublePlays:
                result = self.gameResult(q, self.dealer)
                for p in self.players:
                    if p.getPos()[:7] == q.getPos()[:7]:
                        if result == "win":
                            p.updateCash(+p.getBet())
                        elif result == "loss":
                            p.updateCash(-p.getBet())
            for p in self.players:
                self.gameResult(p, self.dealer)

    def playOneGame(self, player):
        if player.getPos() == "Dealer":
            point, status = self.simDealerHand(player)
        else:
            point, status = self.simPlayerHand(player)
        player.setStatus(status)
        player.setPoint(point)
        self.interface.showInf(status, player.getPos())        
            
    def gameResult(self, player, dealer):
        if player.getStatus() == "bust":
            result = "loss"
        elif dealer.getStatus() == "bust":
            result = "win"
        elif player.getPoint() > dealer.getPoint() :
            result = "win"
        elif player.getPoint() == dealer.getPoint() :
            result = "draw"
        else:
            result = "loss"
        if result == "loss":
            player.updateCash(-player.getBet())
        elif result == "win":
            player.updateCash(+player.getBet())
        self.interface.showInf("{}${} - {}:${}".format(result, player.getBet(), player.getPos(), player.getCash()), player.getPos())
        return result

    def simPlayerHand(self, p):
        point = 0
        status = "normal"
        hasAce = False
        cards = p.getCards()
        while status == "normal":
            point = 0
            for c in cards:
                cardPoint = c.value()
                if cardPoint == 1:
                    hasAce = True
                point = point + cardPoint
            if point > 21:
                status = "bust"
                break
            elif point == 11 and hasAce:
                status = "blackJack"
                point = 21
                break
            order = self.interface.askHitStand(p.pos)
            if order == "stand":
                break
            elif order == "hit":
                p.addCards(self.deck.giveCard(1))
                self.interface.showCards(p.getCards(), p.getPos())
            if point < 11 and hasAce:
                point = point + 10
        return point, status

    def simDealerHand(self, p):
        self.interface.showCards(p.getCards(), p.getPos())
        point = 0
        status = "normal"
        hasAce = False
        cards = p.getCards()
        while status == "normal":
            point = 0
            for c in cards:
                cardPoint = c.value()
                if cardPoint == 1:
                    hasAce = True
                point = point + cardPoint
                if hasAce and ( 6 < point < 12 ) :
                    point = point + 10
            if point > 21:
                status = "bust"
                break
            elif point == 21:
                status = "blackJack"
                break
            if point >= 17:
                break
            p.addCards(self.deck.giveCard(1))
            self.interface.showCards(p.getCards(), p.getPos())    
        return point, status

    def cardPoint(self, card):
        Ace = False
        a = card.getRank()
        a = randrange(1,14)
        if a == 1:
            point = 1
            Ace = True
        elif a < 10:
            point = a
        else:
            point = 10
        return point, Ace

    def getNames(self):
        "gives the name of each player and theire places"
        names = self.interface.getPlayersName()    #interface
        p1 = Player(names[0], "Player1")
        p2 = Player(names[1], "Player2")
        p3 = Player(names[2], "Player3")
        self.players = [p1, p2, p3]

    def giveCards(self, players, n):
        "give hands for each player"
        mydeck = Deck()
        mydeckshuffel = mydeck.shuffel()
        hands = []
        for p in players:
            p.setCards(mydeck.giveCard(n))
    
class Player:
    "This class is defined for save specific features of each player "
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.cash = 0
        self.bet = 0
        self.cards = []

    def getPos(self):
        return self.pos
    
    def getName(self):
        return self.name

    def setCash(self, money):
        self.cash = money
        
    def getCash(self):
        return self.cash
        
    def updateCash(self, money):
        self.cash = self.cash + money
        
    def addCards(self, cards):
        for c in cards:
            self.cards.append(c)

    def removeCards(self):
        self.cards = []

    def removeOneCard(self):
        self.cards.remove(self.cards[1])

    def getCards(self):
        return self.cards

    def getBet(self):
        return self.bet
    
    def setBet(self, bet):
        self.bet = bet

    def setStatus(self, status):
        self.status = status
        
    def setPoint(self, point):
        self.point = point

    def getPoint(self):
        return self.point

    def getStatus(self):
        return self.status

    def clone(self):
        q = Player(self.name, self.pos + ".2")
        q.setBet(self.getBet())
        q.addCards(self.cards[1:])
        return q
