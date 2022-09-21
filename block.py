
BallStartX=0
BallStartY=0 #modify
class Block:
    def __init__(self, Movefield):
        print("create")
        self.pos = (BallStartX, BallStartY)
        self.Movefield = Movefield
        self.grav = 0
        self.gravhelp = 0
        self.ball = self.Movefield.drawline
    def move(self):
        if self.grav % 4 == 0:
            pass
        elif self.grav % 4 == 1:
            pass
        elif self.grav % 4 == 2:
            pass
        else:
            pass

    def gravsv(self):
        if self.grav % 2 == 1:
            self.gravhelp = 1
        else:
            self.grav +=1
        print('SPAAAAACE')
    def check_collision_triangle(self):
        print('wetrykilltriangle')
    def check_collision_wall(self):
        print('destroywalls')
    def collide(self):
        #self.movefield.drawpopup()
        print('collision')
    def disappear(self):
        print('I, the block, died')





