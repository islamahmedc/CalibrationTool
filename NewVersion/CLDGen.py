import os
from pathlib import Path
import CLDVal
import CLDRead



def CLDGen () :
    # TODO : os create output directory
    # Path(Path.cwd()/'hi').mkdir()
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