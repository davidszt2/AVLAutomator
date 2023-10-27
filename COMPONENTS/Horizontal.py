"""
Horizontal stabilizer creation function for AVL geometry file

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""

import math
from COMPONENTS import ControlSurface

def writeHorizontalSurface(filename, incidence, momentArm):
    with open(filename, 'a') as f:
        f.write("#==============================================================\n")
        f.write(f"SURFACE\nHorizontal\n")
        f.write("#Nchordwise       Cspace   Nspanwise   Sspace\n")
        f.write(f"12                1.0      30          1.0\n\n")
        f.write(f"YDUP\n0\n")
        f.write(f"ANGLE\n{incidence}\n")
        f.write(f"TRANSLATE\n{momentArm}  0   0\n")


def writeHorizontalSection(filename, sectionName, xle, yle, zle, chord, ainc, airfoil, NACA=False):
    with open(filename, 'a') as f:
        f.write("#-------------------------------------------------------\n")
        f.write(f"SECTION | {sectionName}\n")
        f.write(f"#Xle     Yle      Zle      chord    Ainc    Nspan    Sspace\n")
        f.write(f"{xle}        {yle}        {zle}         {chord}      {ainc}      30         1\n\n")
        f.write(f"NACA\n{airfoil}\n\n") if NACA else f.write(f"AFIL 0.0 1.0\n{airfoil}\n\n")


def createHorizontal(filename, span, Sref, taper, incidence, momentArm, Calignment = 0.25, elevatorFrac=0.3):
    # filename: name of the file
    # span: horizontal span in meters
    # Sref: horizontal reference area in m^2
    # taper: taper ratio
    # incidence: tail incidence in degrees
    # momentArm: tail momentarm in meters
    # Calignment = root and tip are aligned by this chord fraction (default = quarter chord)
        # In other words, sweep about this chord fraction is 0

    ## ROOT AND TIP CHORDS
    Croot = 2*Sref/(span*(1+taper))
    Ctip = Croot * taper

    ## HINGE VECTORS
    hingeMag = math.sqrt((Croot*(1-taper)*(1-Calignment)**2) + (0.5*span)**2)
    hingeX = Croot*(1-taper)*(1-Calignment) / hingeMag
    hingeY = 0.5*span / hingeMag
    hingeZ = 0 / hingeMag

    ## XLE AND YLE DISPLACEMENTS
    xLEtip = Calignment*(Croot - Ctip)
    yLEtip = span/2

    ## WRITE TO FILE
    # Horizontal Surface
    writeHorizontalSurface(filename, incidence, round(momentArm,3))

    # Horizontal Root
    #               filename   name          x  y  z    c            ainc foil     naca
    writeHorizontalSection(filename, 'Horizontal Root', 0, 0, 0, round(Croot,3), 0, '0012', NACA=True)
    ControlSurface.writeControlSurface(filename, "Elevator", elevatorFrac, round(hingeX,3), round(hingeY,3), round(hingeZ,3), 1)

    # Horizontal Tip
    #               filename   name    x  y  z    c   ainc foil     naca
    writeHorizontalSection(filename, 'Horizontal Tip', xLEtip, yLEtip, 0, round(Croot, 3), 0, '0012', NACA=True)
    ControlSurface.writeControlSurface(filename, "Elevator", elevatorFrac, round(hingeX, 3), round(hingeY, 3),
                                       round(hingeZ, 3), 1)
