import random
import math
from tkinter import *

def init(data):
    data.Mx = 0
    data.My = 0
    data.board = [[0, 0, 0]
                 ,[0, 0, 0]
                 ,[0, 0, 0]]
    data.turn = 'X'
    data.winner = None
    data.GameOver = False

class draw(object):
    @staticmethod
    def draw(canvas, data):
        draw.checkerboard(canvas, data)
        draw.lines(canvas, data)
        draw.XOdraw(canvas, data)

    @staticmethod
    def lines(canvas, data):
        w = data.width//3
        h = data.height//3
        for i in range(2):
            canvas.create_line(w + w*i, -1, w + w*i, 601, width=5)
            canvas.create_line(-1, h + h*i, 601, h + h*i, width=5)
    
    @staticmethod
    def checkerboard(canvas, data):
        w = (data.width//3)//2
        h = (data.height//3)//2
        o = 0
        for i in range(6):
            o += 1
            for j in range(6):
                if o % 2 == 0:
                    fill = 'chartreuse3'
                else:
                    fill = 'chartreuse4'
                canvas.create_rectangle(w*(j), h*(i), w*(j+1), h*(i+1), fill=fill, outline=fill)
                o += 1
    
    @staticmethod
    def XOdraw(canvas, data):
        for i in range(4):
            for j in range(4):
                x = data.board[i-1][j-1]
                if x != 0:
                    if x == 'X':
                        l = 'red'
                    else:
                        l = 'blue'
                    canvas.create_text(100 + data.width//3*(j-1), 100 + data.height//3*(i-1), text=x, font=("Courier", 75), fill=l)
    
    @staticmethod
    def end(canvas, data):
        draw.checkerboard(canvas, data)
        if data.winner != 'Draw':
            if data.winner == 'X':
                l = 'red'
            else:
                l = 'blue'
            canvas.create_text(300, 200, text=data.winner + ' Wins!', font=("Courier", 70, "bold italic"), fill=l)
        else:
            canvas.create_text(300, 200, text=data.winner , font=("Courier", 70, "bold italic"))
        
        canvas.create_rectangle(100, 300, 500, 500, fill='grey')
        canvas.create_text(300, 400, text='Click to play again!', font=("Courier", 20, "bold italic"))
        if data.Mx < 500 and data.Mx > 100 and data.My < 500 and data.My > 300:
            init(data)
            
class logic(object):
    @staticmethod
    def hub(data):
        x, y = logic.whatCell(data)
        logic.isFree(data, x-1, y-1)
    
    @staticmethod
    def whatCell(data):
        w = data.width//3
        h = data.height//3
        for i in range(4):
            for j in range(4):
                if data.Mx > 0 + w*(i-1) and data.Mx < w*i:
                    if data.My > 0 + h*(j-1) and data.My < h*j:
                        return (i, j)
    
    @staticmethod
    def isFree(data, x, y):
        if data.board[y][x] == 0:
            data.board[y][x] = data.turn
            check.checkall(data)
            if data.turn == 'X':
                data.turn = 'O'
            else:
                data.turn = 'X'
        else:
            return None

class check(object):

    @staticmethod
    def checkall(data):
        check.leftdiag(data)
        check.rightdiag(data)
        check.horizontal1(data)
        check.horizontal2(data)
        check.horizontal3(data)
        check.vertical1(data)
        check.vertical2(data)
        check.vertical3(data)
        check.draw(data)

    @staticmethod
    def leftdiag(data):
        if data.board[0][0] == 'X' and data.board[1][1] == 'X' and data.board[2][2] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[0][0] == 'O' and data.board[1][1] == 'O' and data.board[2][2] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def rightdiag(data):
        if data.board[2][0] == 'X' and data.board[1][1] == 'X' and data.board[0][2] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[2][0] == 'O' and data.board[1][1] == 'O' and data.board[0][2] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def horizontal1(data):
        if data.board[0][0] == 'X' and data.board[0][1] == 'X' and data.board[0][2] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[0][0] == 'O' and data.board[0][1] == 'O' and data.board[0][2] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def horizontal2(data):
        if data.board[1][0] == 'X' and data.board[1][1] == 'X' and data.board[1][2] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[1][0] == 'O' and data.board[1][1] == 'O' and data.board[1][2] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def horizontal3(data):
        if data.board[2][0] == 'X' and data.board[2][1] == 'X' and data.board[2][2] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[2][0] == 'O' and data.board[2][1] == 'O' and data.board[2][2] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def vertical1(data):
        if data.board[0][0] == 'X' and data.board[1][0] == 'X' and data.board[2][0] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[0][0] == 'O' and data.board[1][0] == 'O' and data.board[2][0] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def vertical2(data):
        if data.board[0][1] == 'X' and data.board[1][1] == 'X' and data.board[2][1] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[0][1] == 'O' and data.board[1][1] == 'O' and data.board[2][1] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def vertical3(data):
        if data.board[0][2] == 'X' and data.board[1][2] == 'X' and data.board[2][2] == 'X':
            data.winner = 'X'
            data.GameOver = True
        if data.board[0][2] == 'O' and data.board[1][2] == 'O' and data.board[2][2] == 'O':
            data.winner = 'O'
            data.GameOver = True
    
    @staticmethod
    def draw(data):
        a = 0
        for i in range(4):
            for j in range(4):
                x = data.board[i-1][j-1]
                if x == 0:
                    a += 1
        if a == 0:
            data.GameOver = True
            data.winner = 'Draw'

def mousePressed(event, data):
    data.Mx = event.x
    data.My = event.y
    if data.GameOver == True:
        return
    else:
        logic.hub(data)

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.GameOver == True:
        draw.end(canvas, data)
    else:
        draw.draw(canvas, data)

def run(width, height):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
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

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100
    init(data)
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    root.mainloop()

run(600, 600)