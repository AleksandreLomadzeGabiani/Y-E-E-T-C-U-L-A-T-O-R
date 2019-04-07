# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 04:35:10 2019

@author: Aleksandre_The_Greatest

credit for the basic button collisions):  
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
YEET=False

meme_images=("surreal_feel.png","smile_4d_cancer.gif","Brainlet_3.gif"
             ,"brainlet_2.gif","feel_conceal.gif")
MEME=None
win = GraphWin("Y E E T C U L A T O R", WINDOW_WIDTH, WINDOW_HEIGHT)
UI= Image(Point(WINDOW_WIDTH/2, 50),"calculatorUI.gif")
UI.draw(win)

def buttons():
    button_list=[]
    button_commands=("1", "2", "3", "4", "5", "6", "7", 
                      "8", "9", "0", ".", "YEET", "-",
                      "+", "*", "/", "<-", "X", "enter") #need to be arranged to match correct buttons

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
    
    hard_coded_buttons=[su, ad, mu, di, ba, cl, en]
    
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
    
    #all global variables I need for functionality of certain buttons
    global first
    global needClear
    global button_list
    global YEET
    global MEME
#    global UI
#    global text
#    global textOperation
    
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
        
        elif command=="YEET":
            YEET=True
            for button in button_list:
                b, t=button
                if t.getText()=="YEET":
                    t.setText("PLZ STAPH")
                    break
            yeetening=Text(Point(150,390),"click to continue")
            MEME=Image(Point(WINDOW_WIDTH/2, WINDOW_HEIGHT/2),"background_memes/"+choice(meme_images))
            MEME.draw(win)
            yeetening.setTextColor("red")
            yeetening.draw(win)
            clickPoint = win.getMouse()
            yeetening.undraw()
            swap(20)
            button_list[18][0].undraw()
            button_list[18][1].undraw()
            UI.undraw()
            text.undraw()
            textOperation.undraw()
            UI.draw(win)
            text.draw(win)
            textOperation.draw(win)
            button_list[18][0].draw(win)
            button_list[18][1].draw(win)
            return True
        
        elif command=="PLZ STAPH":
            YEET=False
            MEME.undraw()
            for button in button_list:
                b, t=button
                b.undraw()
                t.undraw()
            button_list=buttons()
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
    """ cool way to create rectangles easily (just click)"""
    ll= win.getMouse()
    ur= win.getMouse()
    print ("Rectangle(Point({}, {}), Point({}, {}))".format(ll.getX(),ll.getY(),ur.getX(),ur.getY()))

def swapText(text1, text2):
    """ swaps 2 text object locations """
    anchor1=text1.getAnchor()
    anchor2=text2.getAnchor()
    text1.undraw()
    text2.undraw()
    text2.move(anchor1.getX()-anchor2.getX(),anchor1.getY()-anchor2.getY())
    text1.move(anchor2.getX()-anchor1.getX(),anchor2.getY()-anchor1.getY())
    text1.draw(win)
    text2.draw(win)

def swapButtons(button1, button2):
    """ swaps 2 rectangle object locations """
    anchor1=button1.getCenter()
    anchor2=button2.getCenter()
    button1.undraw()
    button2.undraw()
    button2.move(anchor1.getX()-anchor2.getX(),anchor1.getY()-anchor2.getY())
    button1.move(anchor2.getX()-anchor1.getX(),anchor2.getY()-anchor1.getY())
    button1.draw(win)
    button2.draw(win)


def swap(amount_swaps):
    """ swaps 2 button locations amount_swaps times"""
    global button_list
    
    for i in range(amount_swaps):
        choice1 , choice2= button_list[randrange(0, 18)], button_list[randrange(0, 18)]
        if choice1 != choice2:
            button1, text1 = choice1
            button2, text2= choice2
            print("SWAPPING: '{}' '{}'".format(text1.getText(),text2.getText()))
            swapButtons(button1, button2)
            swapText(text1,text2)
        
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
    
    if YEET:
        swap(randrange(0,5))
        
    if clickPoint is not None:  # so we can substitute checkMouse() for getMouse()
        for button in button_list:
            if inside(clickPoint, button[0]):
                print(button[1].getText())
                cont= action(button)
   

win.close()