"""
Winglet creation function for AVL geometry file

@Author:    David Moeller Sztajnbok
@Date:      November, 2023
"""

def writeWinglet(filename, xLEr, yLEr, zLEr, Croot, Aroot, xLEt, yLEt, zLEt, Ctip, Atip, angle=0):
    with open(filename, 'a') as f:
        f.write("# ==============================================================\n")
        f.write("COMPONENT\n7\nYDUP\n0\n")
        f.write(f"ANGLE\n{angle}\n")
        f.write("# -------------------------------------------------------\n")
        f.write("SECTION | Winglet Lower\n")
        f.write("# Xle     Yle      Zle      chord    Ainc    Nspan    Sspace\n")
        f.write(f"{xLEr}   {yLEr}  {zLEr}    {Croot}  {Aroot}   10  1\n")
        f.write("# -------------------------------------------------------\n")
        f.write("SECTION | Winglet Upper\n")
        f.write("# Xle     Yle      Zle      chord    Ainc    Nspan    Sspace\n")
        f.write(f"{xLEt}  {yLEt}   {zLEt}    {Ctip}   {Atip}   10  1\n\n")
