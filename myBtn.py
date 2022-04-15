from tkinter import Button

class myBtn(Button):
    def __init__(self, switcher: bool):
        Button.__init__(self)
        self.switcher = True
        self.index = ""

    def getIndex(self):
        return self.index