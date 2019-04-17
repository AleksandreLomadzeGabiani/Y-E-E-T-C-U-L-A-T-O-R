# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 04:35:10 2019

@author: A_Normal_PC
"""

from graphics import *
from random import *
from classes import *
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