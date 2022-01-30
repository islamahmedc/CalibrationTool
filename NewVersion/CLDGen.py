import os
from pathlib import Path
import CLDVal
import CLDRead


def CreateOutputFolder () :
    try :
        Path(Path.cwd()/'Output Files').mkdir()
    except FileExistsError :
        pass


def CLDGen () :
    # TODO : try and catch when file is alreeady created
    CreateOutputFolder()

    if CLDVal.genStop == 1 :
        print("Generation is failed -> Please check the errors")
        # TODO : Generate Errors file
        print("Errors file is generated")
        print("Press any key to exit")
        x=input()
        # TODO : os exit
    else :
        print("CLD is ok -> P.java Generating ....")
        # TODO : P.java generation
