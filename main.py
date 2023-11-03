import os
from COMPONENTS import Header, Wing, Horizontal, Vertical
import CASE
import AVL

geomfile = 'test_geom.avl'
casefile = 'test_case.case'

"""INPUT AND DERIVED PARAMETERS"""
# Geometry Input
wingSpan = 1.524
wingAR = 3.8
wingTaper = 0.7

horizontalSpan = 0.752
horizontalAR = 3
horizontalTaper = 1

verticalSpan = 0.33
verticalAR = 1.75
verticalTaper = 0.6

# Derived Values
wingSref = wingSpan**2 / wingAR
wingCroot = 2*wingSref/(wingSpan*(1+wingTaper))
wingCref = (2/3) * wingCroot * (1+wingTaper+wingTaper**2) / (1+wingTaper)

horizontalSref = horizontalSpan**2 / horizontalAR
horizontalCroot = 2*horizontalSref/(horizontalSpan*(1+horizontalTaper))
horizontalCref = (2/3) * horizontalCroot * (1+horizontalTaper+horizontalTaper**2) / (1+horizontalTaper)

verticalSref = verticalSpan**2 / verticalAR
verticalCroot = 2*verticalSref/(verticalSpan*(1+verticalTaper))
verticalCref = (2/3) * verticalCroot * (1+verticalTaper+verticalTaper**2) / (1+verticalTaper)

# Miscelaneous Input
Xcg = 0.2*wingCref
Mach = 0.03
geometryName = 'test_geom'
groundEffectHeight = 0
CD0 = 0.027

"""GEOMETRY FILE"""
# Clear
open(geomfile, 'w').close()

# Header
Header.createHeader(geomfile, geometryName, Mach, wingSref, wingCref, wingSpan, Xcg, CD0)

# Wing
Wing.createWing(geomfile, wingSpan, wingSref, wingTaper, flaps=False, ail=False)

# Horizontal
Horizontal.createHorizontal(geomfile, horizontalSpan, horizontalSref, horizontalTaper, 0, 0.7 * wingSpan)

# Vertical
Vertical.createVertical(geomfile, verticalSpan, verticalSref, verticalTaper, 0, 0.7 * wingSpan, rudder=False)

"""CASE FILE"""
# Clear
open(casefile, 'w').close()

caseName = 'test_geom_case'
CASE.createTrimmedCase(casefile, caseName, 35, 6)

"""RUN PROGRAM"""
geomPath = os.path.abspath(geomfile)
casePath = os.path.abspath(casefile)

# AVL.getStabilityDerivatives(geomPath, casePath, 'test', loud=False)
