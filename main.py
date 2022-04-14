import tkinter
from tkinter import Label, Button, ttk, Tk
from PIL import Image, ImageTk
from stegano import lsb
from functools import partial
import os

MAIN_PATH_CATS = "Dataset/cats"
MAIN_PATH_DOGS = "Dataset/dogs"
MAIN_PATH_FLOWERS = "Dataset/flowers"
MAIN_PATH_SHIPS = "Dataset/ships"

def getNameFilesFromDir(path: str):
    path, dirs, files = next(os.walk(path))
    return files

class myBtn(Button):
    def __init__(self, switcher: bool):
        Button.__init__(self)
        self.switcher = True

def changeBtnState(path: str, btn: myBtn, func, *args):
    placeBtn = btn.place_info()
    if btn.switcher:
        imageLoader = Image.open(path)\
            .resize((90, 90))\
            .convert('L')

        imageRender = ImageTk.PhotoImage(imageLoader)
        btn["image"] = imageRender
        btn["width"] = 90
        btn["height"] = 90
        btn.switcher = False
        btn.image = imageRender
        btn.place(x=int(placeBtn['x']) + 5, y=int(placeBtn['y']) + 5)
    else:
        imageLoader = Image.open(path)\
            .resize((100, 100))

        imageRender = ImageTk.PhotoImage(imageLoader)
        btn["image"] = imageRender
        btn["width"] = 100
        btn["height"] = 100
        btn.switcher = True
        btn.image = imageRender
        btn.place(x=int(placeBtn['x']) - 5, y=int(placeBtn['y']) - 5)


mainApp = Tk()
mainApp.geometry("460x460")
mainApp.resizable(False, False)

arrayOfButtons = []

xCoord = 10
yCoord = 10
for i in range(0, 16):
    tempStr = MAIN_PATH_CATS + "/" + getNameFilesFromDir(MAIN_PATH_CATS)[0]
    imageLoader = Image.open(tempStr) \
        .resize((100, 100), Image.ANTIALIAS)

    imageRender = ImageTk.PhotoImage(imageLoader)
    temp = myBtn(mainApp)
    temp["image"] = imageRender
    temp["width"] = 100
    temp["height"] = 100
    temp["command"] = partial(changeBtnState, tempStr,
                              temp, ())
    temp.image = imageRender
    arrayOfButtons.append(temp)
    arrayOfButtons[len(arrayOfButtons) - 1].place(x=xCoord, y=yCoord)

    if xCoord <= 330:
        xCoord += 110
    else:
        xCoord = 10
        yCoord += 110

mainApp.mainloop()