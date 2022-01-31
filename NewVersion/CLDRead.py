import re
from tkinter import filedialog

def getBiggestLength (str_line) :
    global Biggest_Length
    Biggest_Length = 0
    if Biggest_Length < len(str_line) :
        Biggest_Length = len(str_line)

###################################################
def CLDRead ():
    # TODO : try and catch if no file is selected
    # calFile = filedialog.askopenfile(mode='r')
    calFile = open("NewCAL.CLD",'r')
    calList =[]
    calList=calFile.readlines()
    for line in calList :
        # get the biggest length of line string
        getBiggestLength(line)

        locList =line.split(";")
        del locList[7]
        del locList[2]
        del locList[4]
        calList[calList.index(line)]=locList
    calList[-1][-1] ="\n"
    print(Biggest_Length)
    return calList
