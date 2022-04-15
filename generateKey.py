import random
import tkinter
from time import time, sleep
from tkinter import Label, Button, ttk, Tk
from PIL import Image, ImageTk

from myBtn import myBtn
from helperFuncs import windowPositionCenter, getNameFilesFromDir, keyToFolder

def generateKeySetImages():
    keyApp = Tk(className="generateKey")
    keyApp.geometry("460x150")
    keyApp.resizable(False, False)
    windowPositionCenter(keyApp)

    progressBar = ttk.Progressbar(keyApp, orient= tkinter.HORIZONTAL,
                                  length=440, mode='determinate')
    progressBar.place(x=10, y=130)
    def progressOfWait(currentPosition):
        progressBar["value"] = currentPosition
        keyApp.update()

    xCoord = 10
    yCoord = 10
    fileImages = []
    file = open("key.txt", "w")
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
                tempBtn = myBtn(keyApp)
                tempBtn["image"] = imageRender
                tempBtn["width"] = 100
                tempBtn["height"] = 100
                tempBtn["state"] = tkinter.DISABLED
                tempBtn.image = imageRender
                tempBtn.index = tempStr
                tempBtn.place(x=xCoord, y=yCoord)
                xCoord += 110
                fileImages.append(tempStr)
                file.write(tempBtn.getIndex() + " ")
                break
            else:
                tempStr = ""
                randomFolder = 0

    for i in range(0, 100):
        sleep(0.006)
        progressOfWait(i)

    keyApp.after(3500, lambda: keyApp.destroy())
    keyApp.mainloop()