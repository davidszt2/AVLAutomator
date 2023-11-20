import os
import matplotlib.pyplot as plt
from COMPONENTS import Header, Wing, Horizontal, Vertical
import CASE
import AVL
from PIL import Image
import pandas as pd

geomfile = 'test_geom.avl'
casefile = 'test_case.case'

"""TAPER RATIO TRADE EXAMPLE"""
# wingTaperArr = [.7, .65, .6, .55, .5, .45, .4]
# tradeDict = {}
#
# for wingTaper in wingTaperArr:
#     # Geometry Input
#     wingSpan = 1.524
#     wingAR = 3.8
#
#     horizontalSpan = 0.752
#     horizontalAR = 3
#     horizontalTaper = 1
#
#     verticalSpan = 0.33
#     verticalAR = 1.75
#     verticalTaper = 0.6
#
#     # Derived Values
#     wingSref = wingSpan**2 / wingAR
#     wingCroot = 2*wingSref/(wingSpan*(1+wingTaper))
#     wingCref = (2/3) * wingCroot * (1+wingTaper+wingTaper**2) / (1+wingTaper)
#
#     horizontalSref = horizontalSpan**2 / horizontalAR
#     horizontalCroot = 2*horizontalSref/(horizontalSpan*(1+horizontalTaper))
#     horizontalCref = (2/3) * horizontalCroot * (1+horizontalTaper+horizontalTaper**2) / (1+horizontalTaper)
#
#     verticalSref = verticalSpan**2 / verticalAR
#     verticalCroot = 2*verticalSref/(verticalSpan*(1+verticalTaper))
#     verticalCref = (2/3) * verticalCroot * (1+verticalTaper+verticalTaper**2) / (1+verticalTaper)
#
#     # Miscelaneous Input
#     Xcg = 0.2*wingCref
#     Mach = 0.03
#     geometryName = 'test_geom'
#     groundEffectHeight = 0
#     CD0 = 0.027
#
#     """GEOMETRY FILE"""
#     # Clear
#     open(geomfile, 'w').close()
#
#     # Header
#     Header.createHeader(geomfile, geometryName, Mach, wingSref, wingCref, wingSpan, Xcg, CD0)
#
#     # Wing
#     Wing.createWing(geomfile, wingSpan, wingSref, wingTaper, '1412', NACA=True, flaps=False, ail=False, winglet=False)
#
#     # Horizontal
#     Horizontal.createHorizontal(geomfile, horizontalSpan, horizontalSref, horizontalTaper, 0, 0.7 * wingSpan)
#
#     # Vertical
#     Vertical.createVertical(geomfile, verticalSpan, verticalSref, verticalTaper, 0, 0.7 * wingSpan, rudder=False)
#
#     """CASE FILE"""
#     # Clear
#     open(casefile, 'w').close()
#
#     caseName = 'test_geom_case'
#     CASE.createTrimmedCase(casefile, caseName, 35, 6)
#
#     """RUN PROGRAM"""
#     geomPath = os.path.abspath(geomfile)
#     casePath = os.path.abspath(casefile)
#
#     polar = AVL.steadyLevelRoutine(geomPath, casePath)
#     tradeDict[f'{wingTaper}'] = [polar, wingCroot]
#
# oswaldArr = []
# wingCrootArr = []
#
# for tradeVal in tradeDict.values():
#     oswaldArr.append(tradeVal[0].e)
#     wingCrootArr.append(tradeVal[1])
#
# df = pd.DataFrame({'Taper Ratio': wingTaperArr, 'Oswald Efficiency': oswaldArr, 'Wing Root Chord [m]': wingCrootArr})
# df.to_excel('Taper Trade NACA 1412.xlsx', sheet_name='sheet1', index=False)
#
# fig, ax1 = plt.subplots()
# color = 'b'
# ax1.set_xlabel('Wing Taper Ratio [-]')
# ax1.set_ylabel('Oswald Efficiency [-]', color=color)
# ax1.plot(wingTaperArr, oswaldArr, color=color, marker='.')
# ax1.tick_params(axis='y', labelcolor=color)
# ax1.invert_xaxis()
#
# ax2 = ax1.twinx()
#
# color = 'tab:orange'
# ax2.set_ylabel('Wing Root Chord [m]', color=color)
# ax2.plot(wingTaperArr, wingCrootArr, color=color, marker='.')
# ax2.tick_params(axis='y', labelcolor=color)
#
# fig.tight_layout()
# plt.show()


# Geometry Input
wingSpan = 1.524
wingAR = 3.8
wingTaper = 0.7
wingIncidence = 0

horizontalSpan = 0.752
horizontalAR = 3
horizontalTaper = 0.6
horizontalIncidence = 0

verticalSpan = 0.33
verticalAR = 1.75
verticalTaper = 0.6
verticalIncidence = 0

tailMomentArm = 0.7*wingSpan

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
Xcg = 0.17
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
Wing.createWing(geomfile, wingSpan, wingSref, wingTaper, 'sm701.dat', NACA=False, incidence=wingIncidence, flaps=False, ail=False, winglet=False)

# Horizontal
Horizontal.createHorizontal(geomfile, horizontalSpan, horizontalSref, horizontalTaper, horizontalIncidence, tailMomentArm)

# Vertical
Vertical.createVertical(geomfile, verticalSpan, verticalSref, verticalTaper, verticalIncidence, tailMomentArm, rudder=False)

"""CASE FILE"""
# Clear
open(casefile, 'w').close()

caseName = 'test_geom_case'
# CASE.createTrimmedCase(casefile, caseName, 35, 6)
CASE.createAoACase(casefile, caseName, 35, 6, 10)

"""RUN PROGRAM"""
geomPath = os.path.abspath(geomfile)
casePath = os.path.abspath(casefile)

try:
    # polar = AVL.steadyLevelRoutine(geomPath, casePath)
    polar = AVL.customRoutine(geomPath, casePath)
    print(polar.__dict__)
except Exception as e:
    print(e)
