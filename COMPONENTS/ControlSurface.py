"""
Control surface creation function for AVL geometry file

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""


def writeControlSurface(filename, surfName, surfFrac, surfXHinge, surfYHinge, surfZHinge, sgndup):
    with open(filename, 'a') as f:
        f.write("#Cname   Cgain    Xhinge   HingeVec   SgnDup\n")
        f.write("CONTROL\n")
        f.write(f"{surfName} 1.0 {1 - surfFrac} {surfXHinge} {surfYHinge}  {surfZHinge} {sgndup}\n")