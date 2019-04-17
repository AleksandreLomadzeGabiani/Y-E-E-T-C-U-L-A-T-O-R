# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 05:34:56 2019

@author: A_Normal_PC
"""

from graphics import *
from random import *

import time
seed(time.time())

def swapText(text1, text2):
    """ swaps 2 text object locations """
    anchor1=text1.getAnchor()
    anchor2=text2.getAnchor()
    text1.undraw()
    text2.undraw()
    text2.move(anchor1.getX()-anchor2.getX(),anchor1.getY()-anchor2.getY())
    text1.move(anchor2.getX()-anchor1.getX(),anchor2.getY()-anchor1.getY())
    return (text1, text2)

def swapButtons(button1, button2):
    """ swaps 2 rectangle object locations """
    anchor1=button1.getCenter()
    anchor2=button2.getCenter()
    button1.undraw()
    button2.undraw()
    button2.move(anchor1.getX()-anchor2.getX(),anchor1.getY()-anchor2.getY())
    button1.move(anchor2.getX()-anchor1.getX(),anchor2.getY()-anchor1.getY())
    return (button1, button2)

def print_pos():
    """ cool way to create rectangles easily (just click)"""
    ll= win.getMouse()
    ur= win.getMouse()
    print ("Rectangle(Point({}, {}), Point({}, {}))".format(ll.getX(),ll.getY(),ur.getX(),ur.getY()))
    
def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ul (upper left)
    ur = rectangle.getP2()  # assume p2 is lr (lower right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def buttons():
    """ Generates buttons for the default UI """
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
        
    return button_list