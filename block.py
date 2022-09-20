from Vectors_xy import *

BallStartX=0
BallStartY=0 #modify
class Block:
    def __init__(self, Canvas, self.vel = (0, 0), self.pos = (BallStartX, BallStartY)):
        #aslkdjsal
        self.Canvas=Canvas
        self.grav = 0
    def move(self):
        #thing
        if self.grav%2 == 0:
            #go up
        else:
            #go down
        #4 grav values?

    def gravsv(self):
        self.grav += 1
        # add 1 to score (opt)
    def check_collision_triangle(self):
        #copy balls
    def check_collision_wall(self):
        #check y coord
    def collide(self):
        self.Canvas.drawpopup()
    def disappear(self):





