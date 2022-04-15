from tkinter import Tk
from os import walk
from PIL import Image, ImageTk
from myBtn import myBtn

MAIN_PATH_CATS = "Dataset/cats"
MAIN_PATH_DOGS = "Dataset/dogs"
MAIN_PATH_FLOWERS = "Dataset/flowers"
MAIN_PATH_SHIPS = "Dataset/ships"

keyToFolder = {0: MAIN_PATH_CATS, 1: MAIN_PATH_DOGS,
               2: MAIN_PATH_FLOWERS, 3: MAIN_PATH_SHIPS}

def getNameFilesFromDir(path: str):
    path, dirs, files = next(walk(path))
    return files

def windowPositionCenter(helper: Tk):
    helper.wm_geometry("+%d+%d" %
                       (
                           (
                                   helper.winfo_screenwidth() - helper.winfo_reqwidth()) / 2
                           - helper.winfo_reqwidth() / 2,
                           (
                                   helper.winfo_screenheight() - helper.winfo_reqheight()) / 2
                           - helper.winfo_reqheight() / 2 - 100
                       )
                       )
    return 0

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