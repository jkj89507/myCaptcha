from tkinter import Button

class myBtn(Button):
    def __init__(self):
        Button.__init__(self)
        self.switcher = True if (str(self["state"]) == "NORMAL") else False
        self.index = ""

    def getIndex(self):
        return self.index