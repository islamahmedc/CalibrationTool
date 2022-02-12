import re
from tkinter import filedialog
from tkinter import Tk
import pathlib
import sys

# hide Tk window
root = Tk()
root.withdraw()



###################################################
def CLDRead ():
    calFile = filedialog.askopenfile(mode='r')
    # Check that the extension is correct
    if type(calFile) == type(None) :
        sys.exit()
    extension = pathlib.Path(calFile.name).suffix
    if extension != ".CLD" and extension != ".cld" :
        print("Incorrect File Type")
        print("Press Any Key To Exit....")
        x = input()
        sys.exit()

    # calFile = open("NewCAL.CLD",'r')
    calList =[]
    calList=calFile.readlines()
    for line in calList :
        locList =line.split(";")
        del locList[7]
        del locList[2]
        del locList[4]
        calList[calList.index(line)]=locList
    calList[-1][-1] ="\n"
    return calList
