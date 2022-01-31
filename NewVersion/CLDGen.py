import os
from pathlib import Path
import CLDVal
import CLDRead




def ParameterToLine (L_Parameter) :
    # Remove not used values
    del L_Parameter [2:4]

    # Update Parameter name
    L_Parameter[0] = L_Parameter[0].replace("KU8" , "public static int ")
    L_Parameter[0] += " = "
    L_Parameter[1] += ";" +  " " * CLDRead.Biggest_Length + "// "

    L_Parameter = "".join(L_Parameter)
    return L_Parameter


###################################################
def RemoveOldFiles () :
    # Remove the old Err file if it exists
    if os.path.exists("Output Files/Errors.txt") :
        os.remove("Output Files/Errors.txt")

    # Remove the old C.java file if it exists
    if os.path.exists("Output Files/C.java") :
        os.remove("Output Files/C.java")    


###################################################
def CreateOutputFolder () :
    if os.path.exists(Path.cwd()/'Output Files') :
        RemoveOldFiles()
    else :
        Path(Path.cwd()/'Output Files').mkdir()

###################################################
def CreateErrorsFile () :
    # create new ErrFile
    ErrFile = open("Output Files/Errors.txt",'a')
    for error in CLDVal.L_ErrParameters :
        ErrFile.write(error+"\n")
    ErrFile.close()

###################################################
def CreateCJavaFile () :
    # create new C.java
    CJava = open("Output Files/C.java",'a')
    for Parameter in CLDVal.CLD_List :
        # print(ParameterToLine(Parameter))
        CJava.write(ParameterToLine(Parameter))
    CJava.close()

###################################################
def CLDGen () :
    CreateOutputFolder()

    if CLDVal.genStop == 1 :
        print("Generation is failed -> Please check the errors")
        CreateErrorsFile()
        print("Errors file is generated ...")

        # exit in case of errors are found in the CLD
        print("Press any key to exit")
        x=input()
    else :
        print("CLD is ok -> P.java Generating ....")
        CreateCJavaFile()
        # TODO : P.java generation
