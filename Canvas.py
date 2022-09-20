from triangle import *
from block import *

BgColor = '#222'
FG_COLOR = '#000000'
CanvasWidth = 1000
CanvasHeight = 800

class Canvas:
    def __init__(self, block, root, FPS, relx, rely, relheight, relwidth):
        self.root = root
        self.relx = relx
        self.rely = rely
        self.block = block
        self.relheight = relheight
        self.relwidth = relwidth
        self.triangles = list()
        self.triangles_IDs = dict()
        self.FPS = FPS
        self.init_canvas()

        self.canvas = Canvas(self.root, bg=BgColor,
                             width=CanvasWidth,
                             height=CanvasHeight)
        self.canvas.place(relx=self.relx, rely=self.rely,
                          relwidth=self.relwidth, relheight=self.relheight)
        #create lines


        def reset(self):
            self.update()
            #delete popup?
            self.block.disappear()
            for i in self.triangles:
                i.disappear()
        def update(self):
            #create trangles
            #move triangles
            #delete triangles
            #collision check
            #block move
            self.canvas.after(1000 // self.FPS, self.update) #remember to clear in collision




