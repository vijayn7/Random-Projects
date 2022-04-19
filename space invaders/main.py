from tkinter import *
import random
import math
import os
import copy

def init(data):
    data.timerDelay = 1
    data.time = 0
    data.gameOver = False

    data.shipX, data.shipY = 420, 900

    data.a1Alive = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    data.a2Alive = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    data.a3Alive = [[0, 0, 0, 0, 0]]
    data.mothershipAlive = [[0, 0, 0]]

    data.a1Data = []
    data.a2Data = []
    data.a3Data = []
    data.msData = []

    data.lasers = []
    data.l = None

    data.aSpeed = 0
    data.count = 0

    data.ship = PhotoImage(file='ship.gif')
    data.alien1 = PhotoImage(file='alien1.gif')
    data.alien2 = PhotoImage(file='alien2.gif')
    data.alien3 = PhotoImage(file='alien3.gif')
    data.mothership = PhotoImage(file='mothership.gif')
    data.b = PhotoImage(file='back.gif')

class draw(object):
    @staticmethod
    def background(canvas, data):
        canvas.create_image(0, 0, image=data.b, anchor=NW)
        canvas.create_image(540, 0, image=data.b, anchor=NW)
        canvas.create_image(0, 357, image=data.b, anchor=NW)
        canvas.create_image(540, 357, image=data.b, anchor=NW)
        canvas.create_image(0, 714, image=data.b, anchor=NW)
        canvas.create_image(540, 714, image=data.b, anchor=NW)

    @staticmethod
    def alienGrid(canvas, data, rows, columns, startingX, startingY, margin, alienWidth, alienHeight, alienIMG):
        for i in range(rows):
            for j in range(columns):

                if alienIMG == data.alien1:
                    if data.a1Alive[i][j] == 1:
                        continue
                if alienIMG == data.alien2:
                    if data.a2Alive[i][j] == 1:
                        continue
                if alienIMG == data.alien3:
                    if data.a3Alive[i][j] == 1:
                        continue
                if alienIMG == data.mothership:
                    if data.mothershipAlive[i][j] == 1:
                        continue

                x1 = startingX + margin*j + alienWidth*j
                y1 = startingY + margin*i + alienHeight*i + data.aSpeed
                canvas.create_image(x1, y1, image=alienIMG, anchor=NW)

    @staticmethod
    def army(canvas, data):
        draw.alienGrid(canvas, data, 3, 15, 20, 240, 10, 55, 40, data.alien1)
        draw.alienGrid(canvas, data, 2, 16, 32, 120, 20, 40, 40, data.alien2)
        draw.alienGrid(canvas, data, 1, 5, 150, 60, 100, 60, 40, data.alien3)
        draw.alienGrid(canvas, data, 1, 3, 200, 10, 180, 80, 35, data.mothership)
    
    @staticmethod
    def ship(canvas, data):
        canvas.create_image(data.shipX+40, data.shipY, image=data.ship, anchor=NW)
    
    @staticmethod
    def laser(canvas, data):
        for i in range(len(data.lasers)):
            canvas.create_rectangle(data.lasers[i][0], data.lasers[i][1], data.lasers[i][0]+ 5, data.lasers[i][1]+20, fill='blue')

class laser(object):
    def __init__(self, data):
        self.x = data.shipX+75
        self.y = data.shipY-15
    
    def aslist(self):
        return self.x, self.y

class collisons(object):
    @staticmethod
    def a1(data, startingX, startingY, margin, alienWidth, alienHeight):
        for i in range(3):
            for j in range(15):
                x1 = startingX + margin*j + alienWidth*j
                y1 = startingY + margin*i + alienHeight*i + data.aSpeed
                x2 = startingX + margin*j + alienWidth*j + alienWidth
                y2 = startingY + margin*i + alienHeight*i + data.aSpeed + alienHeight
                data.a1Data.append([x1, y1, x2, y2])

    @staticmethod
    def a2(data, startingX, startingY, margin, alienWidth, alienHeight):
        for i in range(2):
            for j in range(16):
                x1 = startingX + margin*j + alienWidth*j
                y1 = startingY + margin*i + alienHeight*i + data.aSpeed
                x2 = startingX + margin*j + alienWidth*j + alienWidth
                y2 = startingY + margin*i + alienHeight*i + data.aSpeed + alienHeight
                data.a2Data.append([x1, y1, x2, y2])
    
    @staticmethod
    def a3(data, startingX, startingY, margin, alienWidth, alienHeight):
        for i in range(1):
            for j in range(5):
                x1 = startingX + margin*j + alienWidth*j
                y1 = startingY + margin*i + alienHeight*i + data.aSpeed
                x2 = startingX + margin*j + alienWidth*j + alienWidth
                y2 = startingY + margin*i + alienHeight*i + data.aSpeed + alienHeight
                data.a3Data.append([x1, y1, x2, y2])
    
    @staticmethod
    def ms(data, startingX, startingY, margin, alienWidth, alienHeight):
        for i in range(1):
            for j in range(3):
                x1 = startingX + margin*j + alienWidth*j
                y1 = startingY + margin*i + alienHeight*i + data.aSpeed
                x2 = startingX + margin*j + alienWidth*j + alienWidth
                y2 = startingY + margin*i + alienHeight*i + data.aSpeed + alienHeight
                data.msData.append([x1, y1, x2, y2])
    
    @staticmethod
    def laser(data):
        for i in range(len(data.a1Data)):
            for j in range(len(data.lasers)):
                if data.lasers[j][1] > 0:
                    if data.lasers[j][1] >= data.a1Data[i][1] and data.lasers[j][1] <= data.a1Data[i][3]:
                        if data.lasers[j][0] >= data.a1Data[i][0] and data.lasers[j][0] <= data.a1Data[i][2]:
                            a = i // 15
                            b = i % 15
                            if data.a1Alive[a][b] == 0:
                                data.a1Alive[a][b] = 1
                                data.lasers.pop(j)
                                break
        for i in range(len(data.a2Data)):
            for j in range(len(data.lasers)):
                if data.lasers[j][1] > 0:
                    if data.lasers[j][1] >= data.a2Data[i][1] and data.lasers[j][1] <= data.a2Data[i][3]:
                        if data.lasers[j][0] >= data.a2Data[i][0] and data.lasers[j][0] <= data.a2Data[i][2]:
                            a = i // 16
                            b = i % 16
                            if data.a2Alive[a][b] == 0:
                                data.a2Alive[a][b] = 1
                                data.lasers.pop(j)
                                break
        for i in range(len(data.a3Data)):
            for j in range(len(data.lasers)):
                if data.lasers[j][1] > 0:
                    if data.lasers[j][1] >= data.a3Data[i][1] and data.lasers[j][1] <= data.a3Data[i][3]:
                        if data.lasers[j][0] >= data.a3Data[i][0] and data.lasers[j][0] <= data.a3Data[i][2]:
                            if data.a3Alive[0][i] == 0:
                                data.a3Alive[0][i] = 1
                                data.lasers.pop(j)
                                break
        for i in range(len(data.msData)):
            for j in range(len(data.lasers)):
                if data.lasers[j][1] > 0:
                    if data.lasers[j][1] >= data.msData[i][1] and data.lasers[j][1] <= data.msData[i][3]:
                        if data.lasers[j][0] >= data.msData[i][0] and data.lasers[j][0] <= data.msData[i][2]:
                            if data.mothershipAlive[0][i] == 0:
                                data.mothershipAlive[0][i] = 1
                                data.lasers.pop(j)
                                break

class logic(object):

    @staticmethod
    def playerWin(data):
        c = 0
        for j in range(3):
            if data.mothershipAlive[0][j] == 1:
                c += 1
                if c == 3:
                    for y in range(5):
                        if data.a3Alive[0][y] == 1:
                            c += 1
                            if c == 8:
                                for i in range(2):
                                    for x in range(16):
                                        if data.a2Alive[i][x] == 1:
                                            c += 1
                                            if c==40:
                                                for a in range(3):
                                                    for b in range(15):
                                                        if data.a1Alive[a][b] == 1:
                                                            c += 1
                                                            if c == 85:
                                                                return True
    
    @staticmethod
    def alienWin(data):
        for i in range(45):
            if data.a1Data[i][3] >= data.height:
                a = i // 15
                b = i % 15
                if data.a1Alive[a][b] == 0:
                    data.gameOver = True
        for i in range(32):
            if data.a2Data[i][3] >= data.height:
                a = i // 16
                b = i % 16
                if data.a2Alive[a][b] == 0:
                    data.gameOver = True
        for i in range(5):
            if data.a3Data[i][3] >= data.height:
                if data.a3Alive[0][i] == 0:
                    data.gameOver = True
        for i in range(3):
            if data.msData[i][3] >= data.height:
                if data.mothershipAlive[0][i] == 0:
                    data.gameOver = True


def mousePressed(event, data):
    data.l = laser(data).aslist()
    data.lasers.append(data.l)
    

def keyPressed(event, data):
    if event.char == 'a' or event.keysym == 'Left':
        if data.shipX + 30 >= 0:
            data.shipX -= 10
    if event.char == 'd' or event.keysym == 'Right':
        if data.shipX + 120 + 10 <= data.width:
            data.shipX += 10


def timerFired(data):
    data.time += 1

    if len(data.a1Data) > 0:
        logic.alienWin(data)

    if len(data.lasers) > 0:
        for i in range(len(data.lasers)):
            data.lasers[i] = list(data.lasers[i])
            data.lasers[i][1] -= 10
            data.lasers[i] = tuple(data.lasers[i])
    
    if data.time % 20 == 0:
        data.aSpeed += 3
    
        if data.count == 0:
            collisons.a1(data, 20, 240, 10, 55, 40)
            collisons.a2(data, 32, 120, 20, 40, 40)
            collisons.a3(data, 150, 60, 100, 60, 40)
            collisons.ms(data, 200, 10, 180, 80, 35)
            data.count += 1
        else:
            for i in range(len(data.a1Data)):
                data.a1Data[i][1] += 3
                data.a1Data[i][3] += 3
            for i in range(len(data.a2Data)):
                data.a2Data[i][1] += 3
                data.a2Data[i][3] += 3
            for i in range(len(data.a3Data)):
                data.a3Data[i][1] += 3
                data.a3Data[i][3] += 3
            for i in range(len(data.msData)):
                data.msData[i][1] += 3
                data.msData[i][3] += 3

def redrawAll(canvas, data):
    if data.gameOver == True:
        draw.background(canvas, data)
        canvas.create_text(data.width//2, data.height//2, fill='green', text='GAME OVER', font=("Purisa", 24))
    else:
        draw.background(canvas, data)
        draw.army(canvas, data)
        draw.ship(canvas, data)

        collisons.laser(data)

        if len(data.lasers) > 0:
            draw.laser(canvas, data)
    
        if logic.playerWin(data) == True:
            init(data)

def run(width, height):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='black', width=0)
        redrawAll(canvas, data)
        canvas.update()
    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False)
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
              mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
              keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    root.mainloop()

run(1000, 1000)