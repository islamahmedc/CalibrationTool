import re
from tkinter import filedialog
from CLDVal import CLDVal

def calRead ():
    # TODO : try and catch if no file is selected
    # calFile = filedialog.askopenfile(mode='r')
    calFile = open("CalibrationTool/NewVersion/NewCAL.CLD",'r')
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

print(calRead())
CLDVal(calRead())