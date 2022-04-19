from tkinter import *
import os
import random

def init(data):
    data.timerDelay = 1
    data.stopWatch = 0

    data.question = ''
    data.questionAnswered = True
    data.selected = None
    data.x = None
    data.y = None

    data.level = 1

    data.answerBoxescorners = None
    data.a, data.b, data.c, data.d, data.e, data.f, data.g, data.h = 0, 0, 0, 0, 0, 0, 0, 0
    data.tempANS = None
    data.answerBoxestextCount = 0
    data.correct = None
    data.isStopSign = False
    data.score = 0
    data.rounds = 0
    
    data.car = PhotoImage(file='car.gif')
    data.background = PhotoImage(file='background.gif')
    data.interval = 1000//100

    data.frame1 = PhotoImage(file='1.png')
    data.frame2 = PhotoImage(file='2.png')
    data.frame3 = PhotoImage(file='3.png')
    data.frame4 = PhotoImage(file='4.png')
    data.frame5 = PhotoImage(file='5.png')
    data.frame6 = PhotoImage(file='6.png')
    data.frame7 = PhotoImage(file='7.png')
    data.frame8 = PhotoImage(file='8.png')
    data.frame9 = PhotoImage(file='9.png')
    data.frame10 = PhotoImage(file='10.png')

    data.isStarted = True

def createCar(canvas, data, x, y):
    canvas.create_image(x, y, image=data.car, anchor=NW)

def topGUI(canvas, data):
    canvas.create_rectangle(50, 50, data.width-50, 200, fill='green')

class ans(object):
    
    @staticmethod
    def answerBoxes(canvas, data):
        buttonLength = 312
        corners = [85, 423, 761, 1099]
        data.answerBoxescorners = [corners, buttonLength]
        for i in range(len(corners)):
            canvas.create_rectangle(corners[i], 125, corners[i]+buttonLength, 175, fill='brown')

    @staticmethod
    def Antirepeat(data):
        for a in range(4):
            x = data.tempANS[a][0]*data.tempANS[a][1]
            for b in range(4):
                y = data.tempANS[b][0]*data.tempANS[b][1]
                if x == y:
                    data.tempANS[b][0], data.tempANS[b][1] = random.randrange(1,9), random.randrange(1,9)
                    a= 0
                    b= 0
                if x == data.x*data.y:
                    data.tempANS[a][0], data.tempANS[a][1] = random.randrange(1,9), random.randrange(1,9)
                    a= 0
                    b= 0
                if y == data.x*data.y:
                    data.tempANS[b][0], data.tempANS[b][1] = random.randrange(1,9), random.randrange(1,9)
                    a= 0
                    b= 0
    
    @staticmethod
    def answerBoxestext(canvas, data):
        buttonLength = data.answerBoxescorners[1]
        corners = data.answerBoxescorners[0]
        data.tempANS[data.correct-1][0], data.tempANS[data.correct-1][1] = data.x, data.y

        for i in range(4):
            num = data.tempANS[i][0]*data.tempANS[i][1]
            canvas.create_text(corners[i]+buttonLength//2, 150, font=("Purisa", 24), text=num)

def question(canvas, data):
    data.questionAnswered = False
    x, y = random.randrange(13), random.randrange(13)
    data.x, data.y = x, y
    data.question = str(x)+'X'+str(y)+' = ?'
    data.correct = random.randrange(1, 5)
    data.a, data.b, data.c, data.d, data.e, data.f, data.g, data.h = random.randrange(1,12), random.randrange(1,12), random.randrange(1,12), random.randrange(1,12), random.randrange(1,12), random.randrange(1,12), random.randrange(1,12), random.randrange(1,12)
    data.tempANS = [[data.a, data.b],[data.c, data.d],[data.e, data.f],[data.g, data.h]]
    ans.Antirepeat(data)

def mousePressed(event, data):
    corners = data.answerBoxescorners[0]
    buttonLength = data.answerBoxescorners[1]
    buttonHeight = 50

    for i in range(len(corners)):
        if event.y <= 175 and event.y >= 125:
            if event.x >= corners[i] and event.x <= corners[i]+buttonLength:
                data.selected = i
                if data.selected == data.correct-1:
                    data.questionAnswered = True
                else:
                    print('slow car')

def keyPressed(event, data):
    pass

def animation(canvas, data):
    if data.stopWatch >= 0 and data.stopWatch < data.interval:
        canvas.create_image(0, 0, image=data.frame1, anchor=NW)
    if data.stopWatch >= data.interval and data.stopWatch < data.interval*2:
        canvas.create_image(0, 0, image=data.frame2, anchor=NW)
    if data.stopWatch >= data.interval*2 and data.stopWatch < data.interval*3:
        canvas.create_image(0, 0, image=data.frame3, anchor=NW)
    if data.stopWatch >= data.interval*3 and data.stopWatch < data.interval*4:
        canvas.create_image(0, 0, image=data.frame4, anchor=NW)
    if data.stopWatch >= data.interval*4 and data.stopWatch < data.interval*5:
        canvas.create_image(0, 0, image=data.frame5, anchor=NW)
    if data.stopWatch >= data.interval*5 and data.stopWatch < data.interval*6:
        canvas.create_image(0, 0, image=data.frame6, anchor=NW)
    if data.stopWatch >= data.interval*6 and data.stopWatch < data.interval*7:
        canvas.create_image(0, 0, image=data.frame7, anchor=NW)
    if data.stopWatch >= data.interval*7 and data.stopWatch < data.interval*8:
        canvas.create_image(0, 0, image=data.frame8, anchor=NW)
    if data.stopWatch >= data.interval*8 and data.stopWatch < data.interval*9:
        canvas.create_image(0, 0, image=data.frame9, anchor=NW)

    if data.stopWatch >= data.interval*9 and data.stopWatch < data.interval*10:
        canvas.create_image(0, 0, image=data.frame1, anchor=NW)
    if data.stopWatch >= data.interval*10 and data.stopWatch < data.interval*11:
        canvas.create_image(0, 0, image=data.frame2, anchor=NW)
    if data.stopWatch >= data.interval*11 and data.stopWatch < data.interval*12:
        canvas.create_image(0, 0, image=data.frame3, anchor=NW)
    if data.stopWatch >= data.interval*12 and data.stopWatch < data.interval*13:
        canvas.create_image(0, 0, image=data.frame4, anchor=NW)
    if data.stopWatch >= data.interval*13 and data.stopWatch < data.interval*14:
        canvas.create_image(0, 0, image=data.frame5, anchor=NW)
    if data.stopWatch >= data.interval*14 and data.stopWatch < data.interval*15:
        canvas.create_image(0, 0, image=data.frame6, anchor=NW)
    if data.stopWatch >= data.interval*15 and data.stopWatch < data.interval*16:
        canvas.create_image(0, 0, image=data.frame7, anchor=NW)
    if data.stopWatch >= data.interval*16 and data.stopWatch < data.interval*17:
        canvas.create_image(0, 0, image=data.frame8, anchor=NW)
    if data.stopWatch >= data.interval*17 and data.stopWatch < data.interval*18:
        canvas.create_image(0, 0, image=data.frame9, anchor=NW)
    
    if data.stopWatch >= data.interval*18:
        if data.questionAnswered == True:
            question(canvas, data)
            data.stopWatch = 0
        else:
            canvas.create_image(0, 0, image=data.frame10, anchor=NW)
            topGUI(canvas, data)
            canvas.create_text(data.width//2, 100, font=("Purisa", 24), text=data.question)
            ans.answerBoxes(canvas, data)
            ans.answerBoxestext(canvas, data)

def timerFired(data):
    if data.isStarted == True:
        data.stopWatch += 1
        
    if data.stopWatch == 500:
        data.score += 1

def redrawAll(canvas, data):
    animation(canvas, data)
    createCar(canvas, data, 50, 475)

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
    print("bye!")

run(1500, 800)