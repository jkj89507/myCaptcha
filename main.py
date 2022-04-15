import random
import tkinter
from time import time, sleep
from tkinter import Label, Button, ttk, Tk
from PIL import Image, ImageTk
from functools import partial
from os import walk
from os.path import exists

MAIN_PATH_CATS = "Dataset/cats"
MAIN_PATH_DOGS = "Dataset/dogs"
MAIN_PATH_FLOWERS = "Dataset/flowers"
MAIN_PATH_SHIPS = "Dataset/ships"

keyToFolder = {0: MAIN_PATH_CATS, 1: MAIN_PATH_DOGS,
               2: MAIN_PATH_FLOWERS, 3: MAIN_PATH_SHIPS}
class myBtn(Button):
    def __init__(self, switcher: bool, index: str):
        Button.__init__(self)
        self.switcher = True
        self.index = ""

    def getIndex(self):
        return self.index

def getNameFilesFromDir(path: str):
    path, dirs, files = next(walk(path))
    return files

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

def checkValueInMatrix(temp: str, arrayForCheck: list):
    for i in range(0, len(arrayForCheck)):
        if arrayForCheck[i] == temp:
            return i
    return -1

def myCaptcaha():
    mainApp = Tk(className="myCAPTCHA")
    mainApp.geometry("460x460")
    mainApp.resizable(False, False)

    xCoord = 10
    yCoord = 10
    arrayOfListButtons = []
    useImages = []
    for i in range(0, 16):
        tempStr = ""
        randomFolder = 0
        while (True):
            randomFolder = int(random.random() * 10 % 4)

            tempStr = keyToFolder[randomFolder] + \
                      "/" + \
                      getNameFilesFromDir(keyToFolder[randomFolder])[int(random.random() * 10 % 10)]
            if tempStr not in useImages:
                useImages.append(tempStr)
                break
            else:
                tempStr = ""
                randomFolder = 0


        imageLoader = Image.open(tempStr) \
            .resize((100, 100), Image.ANTIALIAS)

        imageRender = ImageTk.PhotoImage(imageLoader)
        tempBtn = myBtn(mainApp, tempStr)
        tempBtn["image"] = imageRender
        tempBtn["width"] = 100
        tempBtn["height"] = 100
        tempBtn["command"] = partial(changeBtnState, tempStr,
                                     tempBtn, ())
        tempBtn.image = imageRender
        arrayOfListButtons.append(tempBtn)
        arrayOfListButtons[len(arrayOfListButtons) - 1].place(x=xCoord, y=yCoord)
        xCoord += 110

        if xCoord >= 440:
            yCoord += 110
            xCoord = 10

    mainApp.mainloop()

def generateKeySetImages():
    keyApp = Tk(className="generateKey")
    keyApp.geometry("460x120")
    keyApp.resizable(False, False)

    xCoord = 10
    yCoord = 10
    fileImages = []
    for i in range(0, 4):
        tempStr = ""
        randomFolder = 0
        while (True):
            randomFolder = int(random.random() * 10 % 4)

            tempStr = keyToFolder[randomFolder] + \
                      "/" + \
                      getNameFilesFromDir(keyToFolder[randomFolder])[int(random.random() * 10 % 10)]
            if tempStr not in fileImages:
                imageLoader = Image.open(tempStr) \
                    .resize((100, 100), Image.ANTIALIAS)
                imageRender = ImageTk.PhotoImage(imageLoader)
                tempBtn = myBtn(keyApp, tempStr)
                tempBtn["image"] = imageRender
                tempBtn["width"] = 100
                tempBtn["height"] = 100
                tempBtn["state"] = tkinter.DISABLED
                tempBtn.image = imageRender
                tempBtn.place(x=xCoord, y=yCoord)
                xCoord += 110
                fileImages.append(tempStr)
                print(tempBtn.getIndex())
                break
            else:
                tempStr = ""
                randomFolder = 0

    keyApp.after(3000, lambda: keyApp.destroy())
    keyApp.mainloop()

generateKeySetImages()
sleep(3)
myCaptcaha()