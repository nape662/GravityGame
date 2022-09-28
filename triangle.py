from random import randint, choice
from tkinter import *

#triangle moves, appears randomly on top or bottom, and only 1 tringangle in one appearance

Rightedge = 980
TopLineY = 0  # upper line y coord
BottomLineY = 525  # bottom line y coord
TriangleColor = 'blue'
class Triangle:
    def __init__(self, movefield, level):
        self.level = level
        self.movefield = movefield
        self.movefield.countdown=100
        self.height = randint(100, 200)
        self.width = self.height*1
        self.position = 980

        # this one can be replaced, here is how to draw the triangles
        if self.level == BottomLineY:
            self.polygon = self.movefield.canvas.create_polygon(Rightedge, self.level, Rightedge + self.width, self.level, Rightedge + self.width/2, self.level - self.height, fill = 'Blue', tag = 'triangle')
        else:
            self.polygon = self.movefield.canvas.create_polygon(Rightedge, self.level, Rightedge + self.width, self.level, Rightedge + self.width / 2, self.level + self.height, fill = 'Blue', tag = 'triangle')
       
    
    def move(self): #triangle moves
        self.movefield.canvas.move(self.polygon,-self.movefield.trianglespeed, 0)
        self.position -= self.movefield.trianglespeed

