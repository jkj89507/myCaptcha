import random
import tkinter
from time import sleep
from tkinter import Tk, Label, messagebox
from PIL import Image, ImageTk
from functools import partial
from os.path import exists

from helperFuncs import windowPositionCenter, \
                        changeBtnState, \
                        getNameFilesFromDir, \
                        keyToFolder
from generateKey import generateKeySetImages
from myBtn import myBtn

def myCaptcaha():
    mainApp = Tk(className="myCAPTCHA")
    mainApp.geometry("460x600")
    mainApp.resizable(False, False)
    windowPositionCenter(mainApp)

    def login():
        amountImagesNeedTouch = 0

        keyFile = open("key.txt", "r")
        getKey = keyFile.readline().split(" ")
        keyFile.close()
        nameForChoose = []
        imagesTouchedPath = []
        for i in arrayOfListButtons:
            nameForChoose.append(i.getIndex())
            print(nameForChoose[len(nameForChoose) - 1],  i.switcher)
            if i.switcher == True:
                imagesTouchedPath.append(i.getIndex())

        for i in range(0, len(getKey)):
            for j in range(0, len(nameForChoose)):
                if getKey[i] == nameForChoose[j]:
                    amountImagesNeedTouch += 1
        print(amountImagesNeedTouch)

        if len(imagesTouchedPath) != amountImagesNeedTouch:
            messagebox.showwarning("Access abort", "Auth is not success!")
            exit(0)
            mainApp.destroy()
        elif amountImagesNeedTouch != 0:
            for i in imagesTouchedPath:
                if i not in getKey:
                    messagebox.showwarning("Access abort", "Auth is not success!")
                    exit(0)
        messagebox.showinfo("Access denied", "Auth is success! Welcome!")
        mainApp.destroy()


    xCoord = 10
    yCoord = 110
    arrayOfListButtons = []
    useImages = []

    mainLabel = Label(mainApp, text= "Выберите элементы в \nсоответствии с ключем\nбезопасности:",
                      anchor=tkinter.W,  font="Batang 20 bold",
                      bg="#1992fc", fg="#fcfcfc",
                      justify=tkinter.LEFT, width=25,
                      height=3)
    mainLabel.place(x=12, y=5)

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

        imageLoader = Image.open(tempStr) \
            .resize((100, 100), Image.ANTIALIAS)

        imageRender = ImageTk.PhotoImage(imageLoader)
        tempBtn = myBtn()
        tempBtn.index = tempStr
        tempBtn["image"] = imageRender
        tempBtn["width"] = 100
        tempBtn["height"] = 100
        tempBtn["command"] = partial(changeBtnState, tempStr, tempBtn)
        tempBtn.image = imageRender
        arrayOfListButtons.append(tempBtn)
        arrayOfListButtons[len(arrayOfListButtons) - 1].place(x=xCoord, y=yCoord)
        xCoord += 110

        if xCoord >= 440:
            yCoord += 110
            xCoord = 10

    checkLoginBtn = myBtn()
    checkLoginBtn["font"] = "Batang 14 bold"
    checkLoginBtn["text"] = "Войти"
    checkLoginBtn["bg"] = "#1992fc"
    checkLoginBtn["activebackground"] = "#fcfcfc"
    checkLoginBtn["fg"] = "#fcfcfc"
    checkLoginBtn["activeforeground"] = "#1992fc"
    checkLoginBtn["command"] = lambda: login()
    checkLoginBtn.place(x=370, y=550)

    mainApp.mainloop()

if exists("key.txt") == False:
    generateKeySetImages()
    sleep(2)
myCaptcaha()