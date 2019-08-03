# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 04:35:10 2019

@author: A_Normal_PC
"""

#Calculator DOES NOT IMPORT FROM classes.py! This error was not present before so I just copied this to keep the code working.
#Still works as usual just import is messed up,so I will leave this until I decide to fix it.
class Calculator(object):

    def __init__(self):
        """ initialize a new instance of a calculator """
        
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 300, 400
        self.first=None
        self.needClear=False
        self.YEET=False
        
        self.meme_images=("surreal_feel.png","smile_4d_cancer.gif","Brainlet_3.gif"
            ,"brainlet_2.gif","feel_conceal.gif","dr_emoji.gif")
        self.MEME=None
        self.win = GraphWin("Y E E T C U L A T O R", self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.UI= Image(Point(self.WINDOW_WIDTH/2, 50),"assets/UI/calculatorUI.gif")
        self.UI.draw(self.win)
        
        self.button_list = buttons()
        self.draw_button_list()

        self.text = Text(Point(150, 50), "")
        self.text.setSize(28)
        self.text.draw(self.win)


        self.textOperation= Text(Point(25, 50), "")
        self.textOperation.setSize(28)
        self.textOperation.draw(self.win)
        
    def swap(self, amount_swaps):
        """ swaps 2 button locations amount_swaps times"""
        
        for i in range(amount_swaps):
            choice1 , choice2= self.button_list[randrange(0, 18)], self.button_list[randrange(0, 18)]
            if choice1 != choice2:
                button1, text1 = choice1
                button2, text2= choice2
                print("SWAPPING: '{}' '{}'".format(text1.getText(),text2.getText()))
                button1, button2 =swapButtons(button1, button2)
                text1, text2 =swapText(text1,text2)
                button1.draw(self.win)
                button2.draw(self.win)                
                text1.draw(self.win)
                text2.draw(self.win)
                
    def draw_button_list(self):
        """ draws every button from button_list to win """
        for button in self.button_list:
            button[0].setFill("white")
            button[0].draw(self.win)
            button[1].draw(self.win)
            
    def action(self,button):
        """ Recieves text and executes command accordingly """
       
        if self.needClear==True:
            self.needClear=False
            action(self.button_list[17])
            
        if button!=None:
            refference, command =button
            command=command.getText()
            
            for i in range(10):
                if command==str(i):
                    self.text.setText(self.text.getText()+str(i))
                    return True
            
            if command==".":
                if self.text.getText().find(".")==-1:
                    self.text.setText(self.text.getText()+".")
                return True
            
            elif command=="YEET":
                self.YEET=True
                for button in self.button_list:
                    b, t=button
                    if t.getText()=="YEET":
                        t.setText("PLZ STAPH")
                        break
                #yeetening=Text(Point(150,390),"click to continue")
                self.MEME=Image(Point(self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2),"assets/background_memes/"+choice(self.meme_images))
                self.MEME.draw(self.win)
                #yeetening.setTextColor("red")
                #yeetening.draw(self.win)
                #clickPoint = self.win.getMouse()
                #yeetening.undraw()
                time.sleep(1/10)
                self.swap(20)
                self.button_list[18][0].undraw()
                self.button_list[18][1].undraw()
                self.UI.undraw()
                self.text.undraw()
                self.textOperation.undraw()
                self.UI.draw(self.win)
                self.text.draw(self.win)
                self.textOperation.draw(self.win)
                self.button_list[18][0].draw(self.win)
                self.button_list[18][1].draw(self.win)
                return True
            
            elif command=="PLZ STAPH":
                self.YEET=False
                self.MEME.undraw()
                for button in self.button_list:
                    b, t=button
                    b.undraw()
                    t.undraw()
                self.button_list=buttons()
                self.draw_button_list()
                return True
            
            elif command=="<-":
                self.text.setText(self.text.getText()[:-1])
                return True
            
            elif command== "X":
                self.text.setText("")
                self.textOperation.setText("")
                self.first=None
                return True
            
            elif command== "/":
                if self.text.getText()!="":
                    self.first=float(self.text.getText())
                    self.text.setText("")
                    self.textOperation.setText("/")
                elif self.first!=None:
                    self.textOperation.setText("/")
                return True
            
            elif command== "*":
                if self.text.getText()!="":
                    self.first=float(self.text.getText())
                    self.text.setText("")
                    self.textOperation.setText("*")
                elif self.first!=None:
                    self.textOperation.setText("*")
                return True
            
            elif command== "-":
                if self.text.getText()!="-" and self.text.getText()!="." and self.text.getText()!="":
                    self.first=float(self.text.getText())
                    self.text.setText("")
                    self.textOperation.setText("-")
                elif self.first!=None:
                    self.textOperation.setText("-")
                elif self.text.getText()!="-" and self.text.getText()!=".":
                    self.text.setText("-")
                return True
            
            elif command== "+":
                if self.text.getText()!="":
                    self.first=float(self.text.getText())
                    self.text.setText("")
                    self.textOperation.setText("+")
                elif self.first!=None:
                    self.textOperation.setText("+")
                return True
            
            elif command== "enter":
                second=self.text.getText()
                first1=self.first
                operation=self.textOperation.getText()
                self.action(self.button_list[17])
                if second!="":
                    second=float(second)
                    if operation=="/":
                        if second!=0:
                            self.text.setText(str(round(first1/second,5)))
                            print(first1/second)
                        else:
                            self.text.setText("Cannot Divide By Zero")
                            print("error")
                            needClear=True
                    elif operation=="*":
                        self.text.setText(str(round(first1*second,3)))
                        print(first1*second)
                    elif operation=="+":
                        self.text.setText(str(round(first1+second,3)))
                        print(first1+second)
                    elif operation=="-":
                        self.text.setText(str(round(first1-second,3)))
                        print(first1-second)
                return True
            else:
                return True
        else:
            return True
        
from graphics import *
from random import *
#from classes import *
from functions import *

import time
seed(time.time())

calculator=Calculator()
cont=True

while cont:
    cont=True
    clickPoint = calculator.win.getMouse()
    
    if calculator.YEET:
        calculator.swap(randrange(0,5))
        
    if clickPoint is not None:  # so we can substitute checkMouse() for getMouse()
        for button in calculator.button_list:
            if inside(clickPoint, button[0]):
                print(button[1].getText())
                cont= calculator.action(button)
   

win.close()