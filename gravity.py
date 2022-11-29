from tkinter import *
from form import *
from canvas import *
FPS = 100


# OUTDATED (YET NOT REALLY) DOCUMENTATION: https://tkdocs.com/shipman/


class Game:
    def __init__(self):
        self.root = Tk(screenName="GravitySwitch")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.movefield = Movefield(self.root, FPS, relx=0.01, rely=0.1, relwidth=0.98, relheight=0.7)
        # edit where game is
        # self.box.pack(side='left', fill='both', expand=1)

        self.form = Form(self.root, self.movefield, relx=0.33, rely=0.6, relwidth=0.33, relheight=0.1)
        self.form.frame.pack(side='bottom', fill='y', expand=0)
        self.root.update()

    def run(self):
        self.root.mainloop()


def main():
    game = Game()
    game.run()

main()

