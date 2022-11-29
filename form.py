from tkinter import *
CtrlFont = 'Tahome 11 bold'
SectionFont = 'Tahome 12 bold'
FrameFont = '#D4CBCB'
BrightButtonColor = 'deep pink'


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
        self.init_frame(root)  # create root structure
        self.init_widgets()  # create things on the root structure
        self.movefield.form = self

    def init_frame(self, root):
        self.frame = Frame(root, bg=FrameFont,
                           width=1, height=1)
        self.frame.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)

    def add_button(self, lebel, on_button_press, font=CtrlFont):
        btn = Button(self.frame, font=font, text=lebel)
        btn.grid(row=self.row, column=self.oddity, columnspan=3, pady=10, padx=10)
        btn.bind('<Button-1>', on_button_press)
        self.row += 1
        return btn

    def add_label(self, label="Score"):
        lbl = Label(self.frame, font=CtrlFont, text=label)
        lbl.grid(row=self.row, column=1, padx=6, pady=6, sticky=S)
        self.row += 1
        return lbl

    def fieldreset(self, event):
        self.movefield.reset()

    def init_widgets(self):
        self.root.bind("<space>", self.movefield.block.gravityswitch)
        self.root.bind("<Return>", self.fieldreset)
        self.reset_button = self.add_button('press Space for graivty and resets', self.fieldreset)
        self.scorelabel = self.add_label()
        self.movefield.label = self.scorelabel
