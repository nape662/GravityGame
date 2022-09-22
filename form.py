from tkinter import *
CtrlFont = 'Tahome 11 bold'
SectionFont = 'Tahome 12 bold'
FrameFont = '#D4CBCB'
BrightButtonColor = 'deep pink'
FormWidth = 300
FormHeight = 80
# PROPER DOCUMENTATION: https://tkdocs.com/shipman/


class Form:
    def __init__(self, root, movefield, relx, rely, relwidth, relheight):
        self.movefield = movefield  # Field
        self.root = root
        self.relx = relx
        self.rely = rely
        self.relwidth = relwidth
        self.relheight = relheight
        self.row = 0  # button row
        self.oddity = 0
        self.init_Frame(root)  # create root structure
        self.init_widgets()  # create things on the root structure

    def init_Frame(self, root):
        self.frame = Frame(root, bg=FrameFont,
                           width=FormWidth, height=FormHeight)
        self.frame.place(relx=self.relx, rely=self.rely,
                         relwidth=self.relwidth, relheight=self.relheight)

    def addButton(self, lebel, onbtnclick, font=CtrlFont):
        btn = Button(self.frame, font=font, text=lebel)
        btn.grid(row=self.row, column=self.oddity, columnspan=1, pady=10, padx=10)
        btn.bind('<Button-1>', onbtnclick)
        self.row+=1
        return btn


    def addLabel(self, label, font=CtrlFont):
        Label(self.frame, font=font, text=label).grid(row=self.row, column=0, padx=6, pady=6, sticky=E)
        lbl = Label(self.frame, font=font)
        lbl.grid(row=self.row, column=1, padx=6, pady=6, sticky=W)
        self.row+=1
        return lbl

    #def SpacebarPress(self):
    #    self.root.bind("<KeyPress-a>", self.movefield.block.gravsv())

    def fieldreset(self, event):
        print("murmur")
        self.movefield.reset()
        # self.movefield.reset()
        # start popup but with text reset

    def init_widgets(self):
        print("init_widgets")
        self.resetbutton = self.addButton('reset', self.fieldreset)
        self.gravityswitchbutton = self.addButton('gravity', self.movefield.block.gravsv)
        self.scorelabel = self.addLabel("Score: 12312321321321323131132131232323133")
        # add invis button and call to ball switch
        # label changes score
