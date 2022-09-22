
class Block:
    def __init__(self, Movefield):
        print("create")
        self.Movefield = Movefield
        self.pos = self.Movefield.Canvasheight
        self.grav = 0
        self.gravhelp = 0 #for buffer
        self.movespeed = 10.5
        self.XOffset = 100
        self.bufferdistance = self.movespeed * 10 #so you can press gravsv before touching ground and will switch gravity right when touch ground
        self.width = 50
        self.dino = self.Movefield.canvas.create_rectangle(self.XOffset, self.Movefield.Canvasheight - self.width, self.XOffset+self.width+1, self.Movefield.Canvasheight+1, fill = 'red')
    def move(self):
        self.check_collision_wall()
        print(self.grav, "gravity")
        if self.grav == 1: #goes up, 2 means it's up
            self.Movefield.canvas.move(self.dino, 0, -self.movespeed)
            self.pos -= self.movespeed
        elif self.grav == 3: #goes down, 0 means it's down
            self.Movefield.canvas.move(self.dino, 0, self.movespeed)
            self.pos += self.movespeed
    def gravsv(self, event):
        if self.grav % 2 == 1:
            if self.pos <= self.bufferdistance + self.width or self.pos >= self.Movefield.Canvasheight - self.bufferdistance:
                self.gravhelp = 1
        else:
            self.grav += 1

    def check_collision_triangle(self):
        self.Movefield.canvas
        overlap = self.field.canvas.find_overlapping(100, self.pos-self.width, 100+self.width, self.pos)
        # check + and - in y coords in overlap
        print('overlap type')
        overlap.type()
    def check_collision_wall(self):
        if self.pos < self.width:
            self.grav=self.gravhelp + 2
            self.gravhelp = 0
            self.pos = self.width
            self.Movefield.canvas.coords(self.dino, self.XOffset, 0, self.XOffset+self.width+1, self.width+1)
        if self.pos > self.Movefield.Canvasheight:
            self.grav = self.gravhelp
            self.gravhelp = 0
            self.pos = self.Movefield.Canvasheight
            self.Movefield.canvas.coords(self.dino, self.XOffset, self.Movefield.Canvasheight - self.width, self.XOffset+self.width+1, self.Movefield.Canvasheight+1)
    def collidewithtriangle(self):
        #self.movefield.drawpopup()
        print('collision')





