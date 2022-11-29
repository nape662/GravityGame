
class Block:
    def __init__(self, Movefield):
        self.Movefield = Movefield
        self.pos = self.Movefield.canvas_height  # y of lower line of block
        self.width = 50
        self.movespeed = 10.5
        self.XOffset = 100

        self.gravity = 0
        self.gravityhelp = 0  # aid for bufferdistance
        self.bufferdistance = self.movespeed * 10
        # last 2 so you can press gravityswitch before touching ground and will switch gravity right when touch ground

        self.dino = self.Movefield.canvas.create_rectangle(self.XOffset, self.Movefield.canvas_height - self.width, self.XOffset+self.width+1, self.Movefield.canvas_height+1, fill = 'red')

    def move(self):
        self.check_collision_triangle()
        self.check_collision_wall()
        if self.gravity == 1: # goes up, 2 means it's up
            self.Movefield.canvas.move(self.dino, 0, -self.movespeed)
            self.pos -= self.movespeed
        elif self.gravity == 3: # goes down, 0 means it's down
            self.Movefield.canvas.move(self.dino, 0, self.movespeed)
            self.pos += self.movespeed

    def resetpos(self):
        self.gravity = 0
        self.gravityhelp = 0
        self.pos = self.Movefield.canvas_height
        self.dino = self.Movefield.canvas.create_rectangle(self.XOffset, self.Movefield.canvas_height - self.width, self.XOffset+self.width+1, self.Movefield.canvas_height+1, fill = 'red')

    def gravityswitch(self, event):
        if self.pos <= self.bufferdistance + self.width and self.gravity == 1:
                self.gravityhelp = 1
        elif self.pos >= self.Movefield.canvas_height - self.bufferdistance and self.gravity == 3:
            self.gravityhelp = 1
        elif self.gravity % 2 == 0:
            self.gravity += 1

    def check_collision_triangle(self):
        overlap = self.Movefield.canvas.find_overlapping(100, self.pos-self.width, 100+self.width, self.pos)
        if len(overlap) > 1:
            self.Movefield.stop()

    def check_collision_wall(self):
        if self.pos < self.width:
            self.gravity=self.gravityhelp + 2
            self.gravityhelp = 0
            self.pos = self.width
            self.Movefield.canvas.coords(self.dino, self.XOffset, 0, self.XOffset+self.width+1, self.width+1)
        if self.pos > self.Movefield.canvas_height:
            self.gravity = self.gravityhelp
            self.gravityhelp = 0
            self.pos = self.Movefield.canvas_height
            self.Movefield.canvas.coords(self.dino, self.XOffset, self.Movefield.canvas_height - self.width, self.XOffset+self.width+1, self.Movefield.canvas_height+1)





