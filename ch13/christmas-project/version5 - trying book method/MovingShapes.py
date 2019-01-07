# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:08:29 2018

@author: ottil
"""

from shape import *
from pylab import random as r
import random

class MovingShape(object):
    def __init__(self,frame,shape,diameter): 
        
        self.diameter = diameter
        self.shape = shape
        self.ﬁgure = Shape(shape,diameter)
        
        self.minx = self.diameter/2
        self.maxx = frame.width - self.minx
        
        self.miny = self.diameter/2
        self.maxy = frame.height - self.miny
        
        self.x = random.randint(self.minx, self.maxx)
        self.y = random.randint(self.miny, self.maxy)
        
#        self.x = self.minx + r() * (self.maxx - self.minx) 
#        self.y = self.miny + r() * (self.maxy - self.miny)
        
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()  

    def goto(self,x,y):
        self.ﬁgure.goto(self.x, self.y)
        
    def moveTick(self):
        if self.x > self.maxx:
            self.dx = -self.dx
        elif self.x < self.minx:
            self.dx = -self.dx
        elif self.y > self.maxy:
            self.dy = -self.dy
        elif self.y < self.miny:
            self.dy = self.dy
            
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        self.ﬁgure.goto(self.x, self.y)
            
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        

class Diamond(MovingShape):
     def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
    
    
    
    
    