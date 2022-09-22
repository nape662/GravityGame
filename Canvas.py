from triangle import *
from block import *

Canvasheight = 525
Canvaswidth = 980

BgColor = '#222'
FG_COLOR = '#00000'
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
        self.countdown = 0
        self.FPS = FPS
        self.resethelp = 1  #helps to break update() loop

        self.canvas = Canvas(self.root, bg=BgColor, width=Canvaswidth, height=Canvasheight)
        self.canvas.place(relx=self.relx, rely=self.rely,
                          relwidth=self.relwidth, relheight=self.relheight)
        self.block = Block(self)

    def start(self): #helper for reset update()
        self.resethelp = 0

    def reset(self):
        self.resethelp = 1
        # self.block.disappear()
        #for i in self.triangles:
        #    i.destruct()
        self.canvas.after(50, self.start())
        self.update()

    def update(self):
            # create trangles
            # move triangles
            # delete triangles
            # collision check
        self.countdown -= 1
        self.block.move()
        if self.resethelp == 0:
            self.canvas.after(1000 // self.FPS, self.update)  # remember to clear in reset





