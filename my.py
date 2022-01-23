import re
from tkinter import filedialog


start=["class hi \n","{\n","    {\n"]
cal=filedialog.askopenfile(mode='r')
end=["}\n","\n","    }\n","\n","        }\n"]
final = open("CalibrationTool/final.java",'w')
group =[]

group+=start
cal = cal.readlines()
print(cal)
cal[-1]+="\n"
group+=cal
group+=end

for line in group :  
    print(line,end="")
    final.write(line)
     
final.close()

      

