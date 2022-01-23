import re
from tkinter import filedialog


start=filedialog.askopenfile(mode='r')
CAL=filedialog.askopenfile(mode='r')
end=filedialog.askopenfile(mode='r')
final = open("C:\\Users\\hp\\Desktop\\New\\final.java",'w')
filesgroup = [start,CAL,end]
group =[]


for workfile in filesgroup :
    workFileList = workfile.readlines()
    workFileList[-1]+="\n"
    # print(workFileList)
    group+=workFileList

for line in group :  
    print(line,end="")
    final.write(line)
     
final.close()
start.close()
CAL.close()
end.close()       

