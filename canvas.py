from triangle import *
from block import *
from tkinter import *


BgColor = '#222'

block_speed = 10.5
triangle_speed = 4


class Movefield:
    def __init__(self, root, FPS, relx, rely, relheight, relwidth):
        self.canvas_height = 420
        self.canvas_width = 980
        self.FPS = FPS
        self.root = root
        self.relx = relx
        self.rely = rely
        self.relheight = relheight
        self.relwidth = relwidth
        self.triangles = list()
        self.triangle_speed = 0
        self.UntilNextTriangle = 1 
        self.speedcountdown = 200  # speedup
        self.stopvar = 0  # 0 stopped, 1 running

        self.canvas = Canvas(self.root, bg=BgColor, width=1, height=1)
        self.canvas.place(relx=self.relx, rely=self.rely,
                          relwidth=self.relwidth, relheight=self.relheight)
        self.block = Block(self)

        # CreateTriangle helpers
        self.leniencydistance = self.block.width * 2.2
        self.fullGravityChangeCoordinate = triangle_speed / block_speed * self.canvas_height
        self.NextTriangleLevel = 0
        
        self.score = 0
        self.form = None
        self.label = None  # have to declare for ScoreUpdate because this thing exists in Form
        # and Form is created after update() uses this
        
        self.reset()
        self.update()

    def reset(self):
        self.canvas.delete('all')
        self.block.resetpos()
        self.triangles.clear()

        if self.form is not None:
            self.form.root.bind("<space>", self.block.gravityswitch)

        self.score = 0

        self.speedcountdown = 200
        self.UntilNextTriangle = 0
        self.triangle_speed = triangle_speed
        self.block.movespeed = block_speed
        self.stopvar = 1

    def createtriangle(self):
        self.triangles.append(Triangle(self, self.NextTriangleLevel))
        self.NextTriangleLevel = self.canvas_height * randint(0, 1)
        if self.triangles[-1].level == self.NextTriangleLevel:
            self.UntilNextTriangle = self.triangles[-1].width
        else:
            k3 = 0
            k1 = self.triangles[-1].width + self.leniencydistance - self.fullGravityChangeCoordinate
            if len(self.triangles) >= 2 and self.triangles[-1].level == self.triangles[-2].level:
                k2 = k1
                k3 = -self.triangles[-2].width + self.fullGravityChangeCoordinate
                if len(self.triangles) >= 3:
                    k2 = self.triangles[-3].width - self.triangles[-2].width - \
                         self.fullGravityChangeCoordinate + self.leniencydistance
            else:
                k2 = self.fullGravityChangeCoordinate
            self.UntilNextTriangle = max(k1, k2, k3)

    def speedup(self):
        self.speedcountdown -= 1
        if self.speedcountdown == 0 and self.triangle_speed <= 10:
            self.triangle_speed += 0.4
            self.block.movespeed += 1.05
            self.speedcountdown = 100
        
    def update_score(self):
        if self.stopvar == 1:
            self.score += 1
        if self.label is not None:
            self.label.config(text="Score:" + str(self.score//10))

    def move_triangles(self):
        for i in self.triangles: 
            if i.position < -i.width * 2:
                self.canvas.delete(i.polygon)
                self.triangles.remove(i)   
            i.move()     

    def update(self):
        self.speedup()
        self.update_score()
    
        self.UntilNextTriangle -= self.triangle_speed * self.stopvar
        if self.UntilNextTriangle <= 0:
            self.createtriangle()

        self.block.move()
        self.move_triangles()

        self.canvas.after(1000 // self.FPS, self.update)

    def stop(self):
        self.triangle_speed = 0
        self.block.movespeed = 0
        self.speedcountdown = -1
        self.stopvar = 0
        if self.form is not None:
            self.form.root.bind("<space>", self.form.fieldreset)
    
