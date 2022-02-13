import os
from pathlib import Path
import CLDRead
import CJavaTemplate
import sys

# NOT USED For NOW
###################################################
# class Max :
#     Biggest_Length =0
###################################################
# NOT USED For NOW
###################################################
# def getBiggestLength (str_line) :
#     if Max.Biggest_Length < len(str_line) :
#         Max.Biggest_Length = len(str_line)

###################################################
# NOT USED For NOW
###################################################
# def ParameterToLine_AftrCommnt (L_Parameter_Aftr) :
#     L_Parameter_Aftr[0] += "     " + " " * (Max.Biggest_Length-len(L_Parameter_Aftr[0])) + "// "
    
#     L_Parameter_Aftr = "".join(L_Parameter_Aftr)
#     return L_Parameter_Aftr

###################################################
# NOT USED For NOW
###################################################
# def ParameterToLine_PreCommnt (L_Parameter_Pre) :
#     # Remove not used values
#     del L_Parameter_Pre [2:4]

#     # Update Parameter name
#     # TODO : add Replace function
#     L_Parameter_Pre[0] = L_Parameter_Pre[0].replace("KU8" , "public static int ")
#     L_Parameter_Pre[0] += " = "
#     L_Parameter_Pre[1] += ";"
#     L_Parameter_Pre[0] = "".join(L_Parameter_Pre[:-2])
#     del L_Parameter_Pre[1]
#     getBiggestLength(L_Parameter_Pre[0])
    

#     return L_Parameter_Pre

###################################################
def ParameterToLine () :
    Final_List = []
    for Parameter in CLDRead.CLDRead() :
        Parameter.insert(0,"public static int ")
        Parameter.insert(2," = ")
        Parameter.insert(4,";")
        Parameter = "".join(Parameter)
        Final_List += [Parameter]
    print(Final_List)
    return Final_List

###################################################
def RemoveOldFiles () :
    # NOT USED For NOW
    ###############################################
    # # Remove the old Err file if it exists
    # if os.path.exists("Output Files/Errors.txt") :
    #     os.remove("Output Files/Errors.txt")

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
# NOT USED For NOW
###################################################
# def CreateErrorsFile () :
#     # create new ErrFile
#     ErrFile = open("Output Files/Errors.txt",'a')
#     for error in CLDVal.L_ErrParameters :
#         ErrFile.write(error+"\n")
#     ErrFile.close()

###################################################
def CreateCJavaFile () :
    # create new C.java
    CJava = open("Output Files/C.java",'a')
    # Write Start of C.Java file
    for line in CJavaTemplate.start :
        CJava.write(line)

    # Write Calibration of C.Java file
    for Parameter_line in ParameterToLine () :
        CJava.write(Parameter_line)

    # Write End of C.Java file
    for line in CJavaTemplate.end :
        CJava.write(line)

    CJava.close()

###################################################
def CLDGen () :
    CreateOutputFolder()
    # NOT USED For NOW
    ###############################################
    # if CLDVal.genStop == 1 :
    #     print("Generation is failed -> Please check the errors")
    #     CreateErrorsFile()
    #     print("Errors file is generated ...")

    #     # exit in case of errors are found in the CLD
    #     print("Press any key to exit")
    #     x=input()
    #     sys.exit()
    # else :
    #     print("CLD is ok -> C.java Generating ....")
    CreateCJavaFile()
    sys.exit()


###################################################