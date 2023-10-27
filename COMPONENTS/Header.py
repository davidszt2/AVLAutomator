"""
Header creation function for AVL geometry file

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""


def createHeader(filename, geometryName, mach, sref, cref, bref, xcg, cd0, groundEffect=False, groundEffectHeight=0):
    with open(filename, 'a') as f:
        f.write(f"{geometryName}\n")
        f.write(f"{mach}                          	| Mach\n")
        f.write(f"0 {1 if groundEffect else 0} {groundEffectHeight if groundEffect else 0}                            | iYsym  iZsym  Zsym\n")
        f.write(f"{round(sref,3)}   {round(cref,3)}   {round(bref,3)}	        | Sref   Cref   Bref\n")
        f.write(f"{round(xcg,3)}   0   0               | Xcg   Ycg   Zcg\n")
        f.write(f"{cd0}                             | CD0\n\n")
