from random import randint, choice
Rightedge = 100
TopLineY = 0  # upper line y coord
BottomLineY = 500  # bottom line y coord
movespeed = 4
TriangleColor = 'blue'


class Triangle:
    def __init__(self, movefield, dist):
        print("createtriangle")
        self.level = choice([BottomLineY, TopLineY])
        self.movefield = movefield
        self.movefield.countdown=dist/movespeed
        self.height = randint(10, 100)
        self.width = self.height*0.4
        
        if self.level == BottomLineY:
            self.polygon = self.movefield.canvas.create_polygon(Rightedge, self.level, Rightedge - self.width, Rightedge - self.width/2, self.level - self.height, fill = 'White')
        else:
            self.polygon = self.movefield.canvas.create_polygon(Rightedge, self.level, Rightedge - self.width, Rightedge - self.width / 2, self.level - self.height, fill = 'White')

    def move(self):
        print("Imoved")
        self.movefield.canvas.move(self.polygon, 0, -movespeed)

    def destruct(self):
        print("destruction")