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
        self.resethelp = 1  #helps to break update() loop
        self.canvas = Canvas(self.root, bg=BgColor, width=CanvasWidth, height=CanvasHeight)
        self.canvas.place(relx=self.relx, rely=self.rely,
                          relwidth=self.relwidth, relheight=self.relheight)
        self.block = Block(self)
        self.Running = False


    def start(self): #helper for reset update()
        self.resethelp = 0

    def reset(self):
        self.resethelp = 1
        self.canvas.delete('all')
        self.block = Block(self)
        self.canvas.after(50, self.start())
        self.update()
        # create 1 trangles

    def update(self):
            # create trangles
        self.countdown -=1
        if self.countdown == 0:
            self.triangles.append(Triangle(self))
        for i in self.triangles: 
            if i.position < -i.width:
                self.canvas.delete(i)
                self.triangles.remove(i)
            i.move()     
            # move triangles
            # delete triangles
            # collision check
        self.block.move()
        if self.resethelp == 0:
            self.canvas.after(1000 // self.FPS, self.update)  # remember to clear in reset

    def stop(self):
        self.resethelp = 1
    






