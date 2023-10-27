"""
Wing creation function for AVL geometry file

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""

import math
from COMPONENTS import ControlSurface


def writeWingSurface(filename, incidence):
    with open(filename, 'a') as f:
        f.write("#==============================================================\n")
        f.write(f"SURFACE\nWing\n")
        f.write("#Nchordwise       Cspace   Nspanwise   Sspace\n")
        f.write(f"12                1.0      50          1.0\n\n")
        f.write(f"YDUP\n0\n")
        f.write(f"ANGLE\n{incidence}\n")
        f.write(f"TRANSLATE\n0  0   0\n")


def writeWingSection(filename, sectionName, xle, yle, zle, chord, ainc, airfoil, NACA=False):
    with open(filename, 'a') as f:
        f.write("#-------------------------------------------------------\n")
        f.write(f"SECTION | {sectionName}\n")
        f.write(f"#Xle     Yle      Zle      chord    Ainc    Nspan    Sspace\n")
        f.write(f"{xle}        {yle}        {zle}         {chord}      {ainc}      50         1\n\n")
        f.write(f"NACA\n{airfoil}\n\n") if NACA else f.write(f"AFIL 0.0 1.0\n{airfoil}\n\n")


def createWing(filename, span, Sref, taper, incidence=0, Calignment = 0.25, ail=True, flaps=True, ailFrac=0.3, flapFrac=0.3):
    # filename: name of the file
    # span: wing span in meters
    # Sref: wing reference area in m^2
    # taper: taper ratio
    # Calignment = root and tip are aligned by this chord fraction (default = quarter chord)
        # In other words, sweep about this chord fraction is 0
    # ail, flaps: booleans defining whether wing has control surfaces (default = True)
    # ailFrac, flapFrac: aileron and flap chord fraction (default = 30%)

    ## ROOT AND TIP CHORDS
    Croot = 2*Sref/(span*(1+taper))
    Ctip = Croot * taper

    ## HINGE VECTORS
    hingeMag = math.sqrt((Croot*(1-taper)*(1-Calignment)**2) + (0.5*span)**2)
    hingeX = Croot*(1-taper)*(1-Calignment) / hingeMag
    hingeY = 0.5*span / hingeMag
    hingeZ = 0 / hingeMag

    ## CHORD AT HALF SPAN
    Cmid = 0.5*(Croot-Ctip) + Ctip

    ## XLE AND YLE DISPLACEMENTS
    xLEmid = Calignment*(Croot - Cmid)
    yLEmid = 0.5*(span/2)

    xLEtip = Calignment*(Croot - Ctip)
    yLEtip = span/2

    ## WRITE TO FILE
    # Wing Surface
    writeWingSurface(filename, incidence)

    # Wing Root
    #               filename   name    x  y  z    c   ainc foil     naca
    writeWingSection(filename, 'Wing Root', 0, 0, 0, round(Croot,3), 0, '0012', NACA=True)
    if flaps:
    #                       filename   name    chordfrac      hinge vector     sgndup
        ControlSurface.writeControlSurface(filename, 'Flaps', flapFrac, round(hingeX,3), round(hingeY,3), hingeZ, 1)

    # Wing Mid
    #               filename   name    x  y  z    c   ainc foil     naca
    writeWingSection(filename, 'Wing Mid', round(xLEmid,3), round(yLEmid,3), 0, round(Cmid,3), 0, '0012', NACA=True)
    if flaps:
        #                       filename   name    chordfrac      hinge vector     sgndup
        ControlSurface.writeControlSurface(filename, 'Flaps', flapFrac, round(hingeX,3), round(hingeY,3), hingeZ, 1)
    if ail:
        #                       filename   name    chordfrac      hinge vector     sgndup
        ControlSurface.writeControlSurface(filename, 'Ailerons', ailFrac, round(hingeX,3), round(hingeY,3), hingeZ, -1)

    # Wing Tip
    #               filename   name    x  y  z    c   ainc foil     naca
    writeWingSection(filename, 'Wing Tip', round(xLEtip,3), round(yLEtip,3), 0, round(Ctip,3), 0, '0012', NACA=True)
    if ail:
        #                       filename   name    chordfrac      hinge vector     sgndup
        ControlSurface.writeControlSurface(filename, 'Ailerons', ailFrac, round(hingeX,3), round(hingeY,3), hingeZ, -1)
