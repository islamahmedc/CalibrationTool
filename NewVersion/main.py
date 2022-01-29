from CLDRead import CLDRead
from CLDVal import CLDVal
from CLDGen import CLDGen

import os
import pathlib

print(CLDRead())
CLDVal(CLDRead())
CLDGen()

print()
print(pathlib.Path().cwd())
