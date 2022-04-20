# oopyDotsDemo.py
# starts with betterDotsDemo and adds:
#   * a dotCounter that counts all the instances of Dot or its subclasses
#   * a MovingDot subclass of Dot that scrolls horizontally
#   * a FlashingMovingDot subclass of MovingDot that flashes and moves

'''
Create a Dots class where you can draw normal dots that have a random radius, random color, and click count
'''


import random
import math
from tkinter import *

class Dot(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(20, 50)
        self.color = random.choice(["pink", "yellow", "blue", "purple", "green", "red"])
        self.clickCount = 0

    def draw(self, canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=self.color)
        canvas.create_text(self.x, self.y, text=str(self.clickCount))

    def containsPoint(self, x, y):
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        return distance <= self.radius

    def move(self, data):
        pass

class MovingDot(Dot):

    def move(self, data):
        self.x += 5
        if self.x > data.width:
            self.x = 0 

class BouncingDot(Dot):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 5

    def move(self, data):
        self.x += self.speed
        if self.x > data.width:
            self.speed *= -1
        if self.x < 0:
            self.speed *= -1

def init(data):
    data.dots = []

def mousePressed(event, data):
    # increment click counts
    for dot in reversed(data.dots):
        if dot.containsPoint(event.x, event.y):
            dot.clickCount += 1
            return

    dotType = random.randint(1, 3)
    if dotType == 1:
        data.dots.append(MovingDot(event.x, event.y))
    elif dotType == 2:
        data.dots.append(Dot(event.x, event.y))
    else:
        data.dots.append(BouncingDot(event.x, event.y))

def redrawAll(canvas, data):
    for dot in data.dots:
        dot.draw(canvas)

def keyPressed(event, data):
    pass

def timerFired(data):
    for dot in data.dots:
        dot.move(data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)