# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 04:35:10 2019

@author: Aleksandre_The_Greatest

credit for the initial structure of code:  
    || https://stackoverflow.com/questions/39867464/adding-button-to-python-graphics-py-window
    || author: cdlane
"""

from graphics import *
from random import *
import time

seed(time.time())

WINDOW_WIDTH, WINDOW_HEIGHT = 300, 400
first=None
needClear=False

win = GraphWin("Y E E T C U L A T O R", WINDOW_WIDTH, WINDOW_HEIGHT)
UI= Image(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/2),"calculatorUI.png")
UI.draw(win)


def buttons():
    
    on = Rectangle(Point(10.0, 167.0), Point(64.0, 212.0))  # points are ordered ul, lr
    tw = Rectangle(Point(79.0, 167.0), Point(133.0, 211.0))
    th = Rectangle(Point(147.0, 167.0), Point(201.0, 212.0))
    fo = Rectangle(Point(10.0, 231.0), Point(64.0, 277.0))
    fi = Rectangle(Point(79.0, 232.0), Point(135.0, 277.0))
    si = Rectangle(Point(147.0, 232.0), Point(201.0, 278.0))
    se = Rectangle(Point(9.0, 290.0), Point(64.0, 337.0))
    ei = Rectangle(Point(79.0, 291.0), Point(133.0, 335.0))
    ni = Rectangle(Point(147.0, 290.0), Point(201.0, 336.0))
    ze = Rectangle(Point(9.0, 350.0), Point(64.0, 394.0))
    cl = Rectangle(Point(17.0, 92.0), Point(71.0, 139.0))
    di = Rectangle(Point(86.0, 94.0), Point(140.0, 137.0))
    mu = Rectangle(Point(154.0, 93.0), Point(208.0, 139.0))
    su = Rectangle(Point(223.0, 152.0), Point(278.0, 197.0))
    ad = Rectangle(Point(223.0, 206.0), Point(278.0, 251.0))
    en = Rectangle(Point(222.0, 264.0), Point(275.0, 383.0))
    do = Rectangle(Point(79.0, 350.0), Point(133.0, 395.0))
    ba = Rectangle(Point(223.0, 94.0), Point(278.0, 138.0))
    rb = Rectangle(Point(148.0, 350.0), Point(202.0, 395.0))
    
    button_tuple=( (on, "1") , (tw, "2") , (th, "3") , (fo, "4"), (fi, "5")
                    , (si, "6"), (se, "7"), (ei, "8"), (ni, "9"), (cl, "X")
                    , (di, "/"), (mu, "*"), (su,"-"), (ad,"+"), (en,"enter")
                    , (do, "."), (ba, "<-"), (ze, "0"), (rb, "rand"))
    
    for button in button_tuple:
        button[0].draw(win)
        
    return button_tuple

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ul (upper left)
    ur = rectangle.getP2()  # assume p2 is lr (lower right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

    
def action(button):
    """ Recieves text and executes command accordingly """
    global first
    global needClear
    global button_tuple
    
    if needClear==True:
        needClear=False
        action(button_tuple[9])
        
    if button!=None:
        refference, command =button
        if command== "1":
            text.setText(text.getText()+"1")
            return True
        
        elif command== "2":
            text.setText(text.getText()+"2")
            return True
        
        elif command== "3":
            text.setText(text.getText()+"3")
            return True
        
        elif command== "4":
            text.setText(text.getText()+"4")
            return True
        
        elif command== "5":
            text.setText(text.getText()+"5")
            return True
        
        elif command== "6":
            text.setText(text.getText()+"6")
            return True
        
        elif command== "7":
            text.setText(text.getText()+"7")
            return True
        
        elif command== "8":
            text.setText(text.getText()+"8")
            return True
        
        elif command== "9":
            text.setText(text.getText()+"9")
            return True

        elif command== "0":
            text.setText(text.getText()+"0")
            return True
        
        elif command==".":
            if text.getText().find(".")==-1:
                text.setText(text.getText()+".")
            return True
        
        elif command=="rand":
            chosen=button_tuple[randrange(0, 18)]
            print("randomly clicked: "+chosen[1])
            action(chosen)
            return True
        
        elif command=="<-":
            text.setText(text.getText()[:-1])
            return True
        
        elif command== "X":
            text.setText("")
            textOperation.setText("")
            first=None
            return True
        
        elif command== "/":
            if text.getText()!="":
                first=float(text.getText())
                text.setText("")
                textOperation.setText("/")
            elif first!=None:
                textOperation.setText("/")
            return True
        
        elif command== "*":
            if text.getText()!="":
                first=float(text.getText())
                text.setText("")
                textOperation.setText("*")
            elif first!=None:
                textOperation.setText("*")
            return True
        
        elif command== "-":
            if text.getText()!="-" and text.getText()!="." and text.getText()!="":
                first=float(text.getText())
                text.setText("")
                textOperation.setText("-")
            elif first!=None:
                textOperation.setText("-")
            elif text.getText()!="-" and text.getText()!=".":
                text.setText("-")
            return True
        
        elif command== "+":
            if text.getText()!="":
                first=float(text.getText())
                text.setText("")
                textOperation.setText("+")
            elif first!=None:
                textOperation.setText("+")
            return True
        
        elif command== "enter":
            second=text.getText()
            first1=first
            operation=textOperation.getText()
            action(button_tuple[9])
            if second!="":
                second=float(second)
                if operation=="/":
                    if second!=0:
                        text.setText(str(round(first1/second,5)))
                        print(first1/second)
                    else:
                        text.setText("Cannot Divide By Zero")
                        print("error")
                        needClear=True
                elif operation=="*":
                    text.setText(str(round(first1*second,3)))
                    print(first1*second)
                elif operation=="+":
                    text.setText(str(round(first1+second,3)))
                    print(first1+second)
                elif operation=="-":
                    text.setText(str(round(first1-second,3)))
                    print(first1-second)
            return True
        else:
            return True
    else:
        return True

def print_pos():
    ll= win.getMouse()
    ur= win.getMouse()
    print ("Rectangle(Point({}, {}), Point({}, {}))".format(ll.getX(),ll.getY(),ur.getX(),ur.getY()))
        
button_tuple = buttons()

text = Text(Point(150, 50), "")
text.setSize(28)
text.draw(win)

textOperation= Text(Point(16, 50), "")
textOperation.setSize(28)
textOperation.draw(win)

cont=True

while cont:
    cont=True
    clickPoint = win.getMouse()
    
    if clickPoint is not None:  # so we can substitute checkMouse() for getMouse()
        for button in button_tuple:
            if inside(clickPoint, button[0]):
                print(button[1])
                cont= action(button)

            

win.close()