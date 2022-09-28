from triangle import *
from block import *
CanvasHeight = 525
BgColor = '#222'
FG_COLOR = '#000000'
CanvasWidth = 1000
CanvasHeight = 800
from tkinter import *

class Movefield:
    def __init__(self, root, FPS, relx, rely, relheight, relwidth):
        print("fieldinit")
        self.Canvasheight = 525
        self.Canvaswidth = 980
        self.root = root
        self.relx = relx
        self.rely = rely
        self.relheight = relheight
        self.relwidth = relwidth
        self.triangles = list()
        self.triangles_IDs = dict()
        self.countdown = 1
        self.FPS = FPS
        self.trianglespeed = 4
        #self.resethelp = 0  #helps to break update() loop
        self.canvas = Canvas(self.root, bg=BgColor, width=CanvasWidth, height=CanvasHeight)
        self.canvas.place(relx=self.relx, rely=self.rely,
                          relwidth=self.relwidth, relheight=self.relheight)
        self.block = Block(self)
        self.nextlevel = 0
        self.reset()
        self.update()

    def reset(self):
        self.canvas.delete('all')
        self.block.resetpos()
        self.triangles.clear()
        self.triangles_IDs.clear()
        self.countdown = 0
        self.trianglespeed = 4
        self.block.movespeed = 10.5
        self.triangles.append(Triangle(self, 0))

    def update(self):
            # create trangles
        self.countdown -= self.trianglespeed
        print(self.countdown)
        if self.countdown <= 0:
            self.triangles.append(Triangle(self, self.nextlevel))
            self.nextlevel = self.Canvasheight * randint(0, 1)
            if self.triangles[-1].level == self.nextlevel:
                self.countdown = self.triangles[-1].width
            if self.triangles[-1].level != self.nextlevel:
                if self.triangles[-1].level == self.triangles[-2].level:
                    self.countdown = self.triangles[-1].width + self.block.width * 2.5 - self.trianglespeed / self.block.movespeed* self.Canvasheight
                else:
                    self.countdown = self.trianglespeed / self.block.movespeed* self.Canvasheight
        for i in self.triangles: 
            #if i.position < -i.width:
            #    self.canvas.delete(self.triangles[-1].polygon)
            #    self.triangles.remove(i)   
            i.move()     
        self.block.move()
        self.canvas.after(1000 // self.FPS, self.update)  # remember to clear in reset

    def stop(self):
        self.trianglespeed = 0
        self.block.movespeed = 0
    






