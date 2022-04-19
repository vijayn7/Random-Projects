import random
import math
from tkinter import *
import os

def init(data):
    data.board = [[0, 0, 0, 0, 0, 0, 0, 0]
                 ,[0, 0, 0, 0, 0, 0, 0, 0]
                 ,[0, 0, 0, 0, 0, 0, 0, 0]
                 ,[0, 0, 0, 0, 0, 0, 0, 0]
                 ,[0, 0, 0, 0, 0, 0, 0, 0]
                 ,[0, 0, 0, 0, 0, 0, 0, 0]
                 ,[0, 0, 0, 0, 0, 0, 0, 0]
                 ,[0, 0, 0, 0, 0, 0, 0, 0]]
    
    data.bp = PhotoImage(file='blackp.gif')

class draw(object):
    @staticmethod
    def drawAll(canvas, data):
        draw.board(canvas, data)

    @staticmethod
    def board(canvas, data):
        w = (data.width//8)
        h = (data.height//8)
        o = 0
        for i in range(8):
            o += 1
            for j in range(8):
                if o % 2 == 0:
                    fill = 'white'
                else:
                    fill = 'black'
                canvas.create_rectangle(w*(j), h*(i), w*(j+1), h*(i+1), fill=fill, outline=fill)
                o += 1

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    draw.drawAll(canvas, data)

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

run(800, 800)