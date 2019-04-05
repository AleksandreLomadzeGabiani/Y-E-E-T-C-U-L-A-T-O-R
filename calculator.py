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

meme_images=("surreal_feel.png","smile_4d_cancer.gif")
win = GraphWin("Y E E T C U L A T O R", WINDOW_WIDTH, WINDOW_HEIGHT)
MEME= Image(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/2),"background_memes/"+choice(meme_images))
MEME.draw(win)
UI= Image(Point(WINDOW_WIDTH/2, 50),"calculatorUI.gif")
UI.draw(win)

def buttons():
    button_list=[]
    button_commands=("1", "2", "3", "4", "5", "6", "7", 
                      "8", "9", "0", ".", "rand", "-",
                      "+", "enter", "/", "<-", "X", "*") #need to be arranged to match correct buttons

    generated_buttons=[]
    for i in range(4):
        for j in range(3):
            generated_buttons.append(Rectangle(Point(75.0+(j*3)+(j-1)*63, 205.0+(i*3)+(i-1)*57), 
                                           Point(75.0+(j*3)+(j)*63, 205.0+(i*3)+(i)*57)))

    cl = Rectangle(Point(17.0, 92.0), Point(71.0, 139.0)) # points are ordered ul, lr
    di = Rectangle(Point(86.0, 92.0), Point(140.0, 139.0))
    mu = Rectangle(Point(154.0, 92.0), Point(208.0, 139.0))
    ba = Rectangle(Point(223.0, 92.0), Point(278.0, 139.0))
    su = Rectangle(Point(223.0, 152.0), Point(278.0, 197.0))
    ad = Rectangle(Point(223.0, 206.0), Point(278.0, 251.0))
    en = Rectangle(Point(223.0, 264.0), Point(278.0, 383.0))
    

    hard_coded_buttons=[su, ad, en, di, ba, cl, mu]
    
    temp=-1
    for button in generated_buttons:
        temp+=1
        button_list.append((button, Text(Point((button.getP1().getX()+button.getP2().getX())/2
                   , (button.getP1().getY()+button.getP2().getY())/2), button_commands[temp])))
    
    for button in hard_coded_buttons:
        temp+=1
        button_list.append((button, Text(Point((button.getP1().getX()+button.getP2().getX())/2
                   , (button.getP1().getY()+button.getP2().getY())/2), button_commands[temp])))
        
    for button in button_list:
        button[0].setFill("white")
        button[0].draw(win)
        button[1].draw(win)
        
    return button_list

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ul (upper left)
    ur = rectangle.getP2()  # assume p2 is lr (lower right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

    
def action(button):
    """ Recieves text and executes command accordingly """
    global first
    global needClear
    global button_list
    
    if needClear==True:
        needClear=False
        action(button_list[17])
        
    if button!=None:
        refference, command =button
        command=command.getText()
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
            chosen=button_list[randrange(0, 18)]
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
            action(button_list[17])
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
        
button_list = buttons()

text = Text(Point(150, 50), "")
text.setSize(28)
text.draw(win)

textOperation= Text(Point(25, 50), "")
textOperation.setSize(28)
textOperation.draw(win)

cont=True

while cont:

    cont=True
    clickPoint = win.getMouse()
    
    if clickPoint is not None:  # so we can substitute checkMouse() for getMouse()
        for button in button_list:
            if inside(clickPoint, button[0]):
                print(button[1].getText())
                cont= action(button)
   

win.close()