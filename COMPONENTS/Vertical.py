"""
Vertical stabilizer creation function for AVL geometry file

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""

import math
from COMPONENTS import ControlSurface

def writeVerticalSurface(filename, incidence, momentArm):
    with open(filename, 'a') as f:
        f.write("#==============================================================\n")
        f.write(f"SURFACE\nVertical\n")
        f.write("#Nchordwise       Cspace   Nspanwise   Sspace\n")
        f.write(f"12                1.0      10          1.0\n\n")
        f.write(f"YDUP\n0\n")
        f.write(f"ANGLE\n{incidence}\n")
        f.write(f"TRANSLATE\n{momentArm}  0   0\n")


def writeVerticalSection(filename, sectionName, xle, yle, zle, chord, ainc, airfoil, NACA=False):
    with open(filename, 'a') as f:
        f.write("#-------------------------------------------------------\n")
        f.write(f"SECTION | {sectionName}\n")
        f.write(f"#Xle     Yle      Zle      chord    Ainc    Nspan    Sspace\n")
        f.write(f"{xle}        {yle}        {zle}         {chord}      {ainc}      10         1\n\n")
        f.write(f"NACA\n{airfoil}\n\n") if NACA else f.write(f"AFIL 0.0 1.0\n{airfoil}\n\n")


def createVertical(filename, span, Sref, taper, incidence, momentArm, Calignment = 1, rudderFrac=0.3):
    # filename: name of the file
    # span: vertical span in meters
    # Sref: vertical reference area in m^2
    # taper: taper ratio
    # incidence: tail incidence in degrees
    # momentArm: tail moment arm in meters
    # Calignment = root and tip are aligned by this chord fraction (default = trailing edge)
        # In other words, sweep about this chord fraction is 0

    ## ROOT AND TIP CHORDS
    Croot = 2*Sref/(span*(1+taper))
    Ctip = Croot * taper

    ## HINGE VECTORS
    hingeMag = math.sqrt((Croot*(1-taper)*(1-Calignment)**2) + (0.5*span)**2)
    hingeX = Croot*(1-taper)*(1-Calignment) / hingeMag
    hingeY = 0 / hingeMag
    hingeZ = 0.5 * span / hingeMag

    ## XLE AND YLE DISPLACEMENTS
    xLEtip = Calignment*(Croot - Ctip)
    yLEtip = 0
    zLEtip = span

    ## WRITE TO FILE
    # Vertical Surface
    writeVerticalSurface(filename, incidence, round(momentArm, 3))

    # Horizontal Root
    #               filename   name          x  y  z    c            ainc foil     naca
    writeVerticalSection(filename, 'Vertical Root', 0, 0, 0, round(Croot, 3), 0, '0012', NACA=True)
    ControlSurface.writeControlSurface(filename, "Rudder", rudderFrac, round(hingeX,3), round(hingeY,3), round(hingeZ,3), 1)

    # Horizontal Tip
    #               filename   name    x  y  z    c   ainc foil     naca
    writeVerticalSection(filename, 'Vertical Tip', round(xLEtip,3), round(yLEtip,3), round(zLEtip,3), round(Ctip, 3), 0, '0012', NACA=True)
    ControlSurface.writeControlSurface(filename, "Rudder", rudderFrac, round(hingeX, 3), round(hingeY, 3),
                                       round(hingeZ, 3), 1)

