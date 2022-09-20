from tkinter import *
CtrlFont = 'Tahome 11 bold'
SectionFont = 'Tahome 12 bold'
FormWidth = 300
FormHeight = 800
# PROPER DOCUMENTATION: https://tkdocs.com/shipman/
class Form:
    def __init__(self, parent, box, relx, rely, relwidth, relheight):
        self.box = box  # Field
        self.parent = parent
        self.relx = relx
        self.rely = rely
        self.relwidth = relwidth
        self.relheight = relheight
        self.row = 0 #button row
        self.oddity = 0
        self.init_Frame(parent) #create parent structure
        self.init_widgets() #create things on the parent structure

    def init_Frame(self, parent):
        self.frame = Frame(parent, bg=FrameFont,
                           width=FormWidth, height=FormHeight)
        self.frame.place(relx=self.relx, rely=self.rely,
                         relwidth=self.relwidth, relheight=self.relheight)

    def addLebel(self, lebel, font=CtrlFont):
        Label(self.frame, font=font, text=lebel).grid(row=self.row, column=0, padx=6, pady=6, sticky=E)
        lbl = Label(self.frame, font=font)
        lbl.grid(row=self.row, column=1, padx=6, pady=6, sticky=W)
        self.row += 1
        return lbl

    def addSwitchButton(self, lebel, gravsv, font=Black): #make it insivible
        btn = Button(self.frame, font=font, text=lebel)
        btn.grid(row=self.row, column=self.oddity, columnspan=1, pady=10, padx=10)
        #bind to space
        btn.bind('<Button=1>', gravsv)

        return btn

    def createstartpopup(self):
        #with text start
    def resetpopup(self):
        #start popup but with text reset
    def init_widgets(self):
        # add invis button and call to ball switch
        #label changes score