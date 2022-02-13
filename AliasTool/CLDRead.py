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
    # calFile = filedialog.askopenfile(mode='r')
    # # Check that the extension is correct
    # if type(calFile) == type(None) :
    #     sys.exit()
    # extension = pathlib.Path(calFile.name).suffix
    # if extension != ".CSV" and extension != ".csv" :
    #     print("Incorrect File Type")
    #     print("Press Any Key To Exit....")
    #     x = input()
    #     sys.exit()

    calFile = open("Alias.csv",'r')
    calList =[]
    calList=calFile.readlines()
    del calList[0]
    for line in calList :
        locList =line.split(",")
        del locList[-1]
        locList+=['\n']
        calList[calList.index(line)]=locList
    return calList
