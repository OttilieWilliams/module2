# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:17:53 2019

@author: ottil 
"""
from shape import Frame
#import time
from MovingShapes import *

#print(r()<0.5)

frame = Frame()
numshapes = 3
shapes = []
for i in range(numshapes):
    shapes.append(Square(frame,100))
    shapes.append(Diamond(frame,100))
    shapes.append(Circle(frame,100))
for i in range(100):
    for shape in shapes:
        shape.moveTick()
#        time.sleep(0.03)
        
