from graphics import *
from button import Button
from deck import Card

class GraphicInterface:
    def __init__(self):
        self.win = GraphWin("Bridge Game", 1200, 600)
        self.win.setCoords(0,0,400,200)
        self.win.setBackground("white")
        
    def resetWindow(self):
        self.win.close()
        self.win = GraphWin("Bridge Game", 1200, 600)
        self.win.setCoords(0,0,400,200)
        self.win.setBackground("white")
        self.infs = []
        d = Point(50, 5)
        t = Text(d, "")
        self.infs.append(t)
        d = Point(50, 100)
        t = Text(d, "")
        self.infs.append(t)
        d = Point(145, 5)
        t = Text(d, "")
        self.infs.append(t)
        d = Point(225, 5)
        t = Text(d, "")
        self.infs.append(t)
        d = Point(330, 5)
        t = Text(d, "")
        self.infs.append(t)
        d = Point(330, 100)
        t = Text(d, "")
        self.infs.append(t)
        d = Point(200, 100)
        t = Text(d, "")
        self.infs.append(t)
        for t in self.infs:
            t.draw(self.win)

        self.gameInfs = []
        d = Point(50, 88)
        t1 = Text(d, "")
        self.gameInfs.append(t1)
        d = Point(175, 88)
        t1 = Text(d, "")
        self.gameInfs.append(t1)
        d = Point(325, 88)
        t1 = Text(d, "")
        self.gameInfs.append(t1)
        for t1 in self.gameInfs:
            t1.draw(self.win)
        
##    def showSetWinner(self, inf):
##        print("\n The winner is:" + inf)
##        
##    def showIntro(self):
##        print("Skunk is amazing isn't it?")
##
##    def setDices(self, point1, point2, name, p):
##        print("\n{}:(point = {})\nDice1 is: {} , Dice2 is {}.".format(name, p, point1, point2))
##
##    def save(self):
##        ans = input("Do you want to save? ")
##        return ans[0] in "Yy"
    
    def startGame(self):
        t = Text(Point(160,125), "Do you want to Start a new game? ")
        t.draw(self.win)
        d = Point(150, 115)
        yesBut = Button(self.win, d, 17, 8, "yes")
        yesBut.activate()
        d.move(25,0)
        noBut = Button(self.win, d, 17, 8, "no")
        noBut.activate()
        while True:
            p = self.win.getMouse()
            if yesBut.clicked(p):
                yesBut.undraw()
                noBut.undraw()
                return True
            if noBut.clicked(p):
                noBut.undraw()
                yesBut.undraw()
                return False

    def getPlayersName(self):
        texts = []
        entries = []
        t = Text(Point(160,110), "Player1 name is: ")
        texts.append(t)
        t = Text(Point(160,100), "Player2 name is: ")
        texts.append(t)
        t = Text(Point(160,90), "Player3 name is: ")
        texts.append(t)
        e = Entry(Point(210,110),19)
        entries.append(e)
        e = Entry(Point(210,100),19)
        entries.append(e)
        e = Entry(Point(210,90),19)
        entries.append(e)
        for t in texts:
            t.draw(self.win)
        for e in entries:
            e.draw(self.win)
        okBut = Button(self.win, Point(200, 80), 17, 8, "OK")
        okBut.activate()
        while True:
            p = self.win.getMouse()
            if okBut.clicked(p):
                break
        names = []
        for e in entries:
            names.append(e.getText())
            e.undraw()
        for t in texts:
            t.undraw()
        okBut.undraw()

        return names[0], names[1], names[2]
    
    def getEachPlayerStartCash(self):
        t = Text(Point(160,100), "Each Player Cash Is:$ ")
        t.draw(self.win)
        e = Entry(Point(210,100),15)
        e.draw(self.win)
        okBut = Button(self.win, Point(200, 80), 17, 8, "OK")
        okBut.activate()
        while True:
            p = self.win.getMouse()
            if okBut.clicked(p):
                break
        cash = int(e.getText())
        e.undraw()
        t.undraw()
        okBut.undraw()
        return cash

    def getBets(self):
        texts = []
        entries = []
        t = Text(Point(160,110), "Player1 bet is: ")
        texts.append(t)
        t = Text(Point(160,100), "Player2 bet is: ")
        texts.append(t)
        t = Text(Point(160,90), "Player3 bet is: ")
        texts.append(t)
        e = Entry(Point(210,110),19)
        entries.append(e)
        e = Entry(Point(210,100),19)
        entries.append(e)
        e = Entry(Point(210,90),19)
        entries.append(e)
        for t in texts:
            t.draw(self.win)
        for e in entries:
            e.draw(self.win)
        okBut = Button(self.win, Point(200, 80), 17, 8, "OK")
        okBut.activate()
        while True:
            p = self.win.getMouse()
            if okBut.clicked(p):
                break
        bet = []
        for e in entries:
            bet.append(int(e.getText()))
            e.undraw()
        for t in texts:
            t.undraw()
        okBut.undraw()

        return bet[0], bet[1], bet[2]


    def showGameInf(self, inf, pos):
        if pos == "Player1":
            self.gameInfs[0].setText(inf)
        elif pos == "Player2":
            self.gameInfs[1].setText(inf)
        elif pos == "Player3":
            self.gameInfs[2].setText(inf)

            
    def showInf(self, inf, pos):
        if pos == "Player1":
            self.infs[0].setText(inf)
        elif pos == "Player1.2":
            self.infs[1].setText(inf)
        elif pos == "Player2":
            self.infs[2].setText(inf)
        elif pos == "Player2.2":
            self.infs[3].setText(inf)
        elif pos == "Player3":
            self.infs[4].setText(inf)
        elif pos == "Player3.2":
            self.infs[5].setText(inf)
        elif pos == "Dealer":
            self.infs[6].setText(inf)
        

    def showCards(self, card, pos):        
        if pos == "Dealer":
            p = Point(175,155)
        elif pos == "Player3":
            p = Point(325,35)
        elif pos == "Player2":
            p = Point(145,35)
        elif pos == "Player1":
            p = Point(25,35)
        elif pos == "Player1.2":
            p = Point(25,135)
        elif pos == "Player2.2":
            p = Point(225,35)
        elif pos == "Player3.2":
            p = Point(325,135)
        for c in card:
                c.cardDraw(self.win, p)
                p.move(10,0)

    def askHitStand(self, pos):
        if pos == "Player1":
            d = Point(15, 70)
        elif pos == "Player1.2":
            d = Point(15, 170)
        
        elif pos == "Player2":
            d = Point(175, 70)
        elif pos == "Player2.2":
            d = Point(225, 70)
        
        elif pos == "Player3":
            d = Point(325, 70)
        elif pos == "Player3.2":
            d = Point(325, 170)
        
        hitBut = Button(self.win, d, 17, 8, "hit")
        hitBut.activate()
        d.move(25,0)
        standBut = Button(self.win, d, 17, 8, "stand")
        standBut.activate()
        while True:
            p = self.win.getMouse()
            if hitBut.clicked(p):
                hitBut.undraw()
                standBut.undraw()
                return hitBut.getLabel()
            if standBut.clicked(p):
                hitBut.undraw()
                standBut.undraw()
                return standBut.getLabel()

    def askDouble(self, pos):
        if pos == "Player1":
            d = Point(15, 70)
        elif pos == "Player2":
            d = Point(175, 70)
        elif pos == "Player3":
            d = Point(325, 70)
        
        yesBut = Button(self.win, d, 17, 8, "Yes")
        yesBut.activate()
        d.move(25,0)
        noBut = Button(self.win, d, 17, 8, "No")
        noBut.activate()
        d.move(-11, 10)
        t = Text(d, "Dou you want to double? ")
        t.draw(self.win)
        while True:
            p = self.win.getMouse()
            if yesBut.clicked(p):
                yesBut.undraw()
                noBut.undraw()
                t.undraw()
                return True
            if noBut.clicked(p):
                yesBut.undraw()
                noBut.undraw()
                t.undraw()
                return False
