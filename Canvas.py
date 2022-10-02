from triangle import *
from block import *
from tkinter import *


BgColor = '#222'

blockspeed = 10.5
trianglespeed = 4


class Movefield:
    def __init__(self, root, FPS, relx, rely, relheight, relwidth):
        self.Canvasheight = 420
        self.Canvaswidth = 980
        self.FPS = FPS
        self.root = root
        self.relx = relx
        self.rely = rely
        self.relheight = relheight
        self.relwidth = relwidth
        self.triangles = list()
        self.UntilNextTriangle = 1 
        self.speedcountdown = 200 #speedup
        self.stopvar = 0  # 0 stopped, 1 running

        self.canvas = Canvas(self.root, bg=BgColor, width=1, height=1)
        self.canvas.place(relx=self.relx, rely=self.rely,
                          relwidth=self.relwidth, relheight=self.relheight)
        self.block = Block(self)

        # CreateTriangle helpers
        self.leniencydist = self.block.width * 2.2
        self.fullgravchangeX = trianglespeed / blockspeed * self.Canvasheight
        self.NextTriangleLevel = 0
        
        self.score = 0
        self.label = None  # have to declare for ScoreUpdate because this thing exists in Form and Form is created after update() uses this
        
        self.reset()
        self.update()

    def reset(self):
        self.canvas.delete('all')
        self.block.resetpos()
        self.triangles.clear()

        self.score = 0

        self.speedcountdown = 200
        self.UntilNextTriangle = 0
        self.trianglespeed = trianglespeed
        self.block.movespeed = blockspeed
        self.stopvar = 1

    def createtriangle(self):
        self.triangles.append(Triangle(self, self.NextTriangleLevel))
        self.NextTriangleLevel = self.Canvasheight * randint(0, 1)
        if self.triangles[-1].level == self.NextTriangleLevel:
            self.UntilNextTriangle = self.triangles[-1].width
        else:
            k3 = 0
            k1 = self.triangles[-1].width + self.leniencydist - self.fullgravchangeX
            if len(self.triangles) >= 2 and self.triangles[-1].level == self.triangles[-2].level:
                k2 = k1
                k3 = -self.triangles[-2].width + self.fullgravchangeX
                if len(self.triangles) >= 3:
                    k2 = self.triangles[-3].width - self.triangles[-2].width - self.fullgravchangeX + self.leniencydist
            else:
                k2 = self.fullgravchangeX
            self.UntilNextTriangle = max(k1, k2, k3)

    def speedup(self):
        self.speedcountdown -= 1
        if self.speedcountdown == 0 and self.trianglespeed <= 10:
            self.trianglespeed += 0.4
            self.block.movespeed += 1.05
            self.speedcountdown = 100
        
    def UpdateScore(self):
        if self.stopvar == 1:
            self.score += 1
        if self.label != None:
           self.label.config(text = "Score:" + str(self.score//10))

    def MoveTriangles(self):
        for i in self.triangles: 
            if i.position < -i.width * 2:
                self.canvas.delete(i.polygon)
                self.triangles.remove(i)   
            i.move()     


    def update(self):
        self.speedup()
        self.UpdateScore()
    
        self.UntilNextTriangle -= self.trianglespeed * self.stopvar
        if self.UntilNextTriangle <= 0:
            self.createtriangle()

        self.block.move()
        self.MoveTriangles()

        self.canvas.after(1000 // (self.FPS), self.update)

    def stop(self):
        self.trianglespeed = 0
        self.block.movespeed = 0
        self.speedcountdown = -1
        self.stopvar = 0
    






