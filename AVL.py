"""
AVL automation functions for running AVL subprocess through Python

@Author:    David Moeller Sztajnbok
@Date:      November, 2023
"""

import subprocess
import os

avlGeom = 'test_geom.avl'
avlCase = 'test_case.case'


class OutputAVL:
    def __init__(self, alphaTrim, CLtot, CDtot, e, Elevator, Flaps, Ailerons, Rudder):
        self.alphaTrim = alphaTrim
        self.CLtot = CLtot
        self.CDtot = CDtot
        self.e = e
        self.Elevator = Elevator
        self.Flaps = Flaps
        self.Ailerons = Ailerons
        self.Rudder = Rudder


def steadyLevelCommands(geom, case, stOut='stOut.txt', filename='commands.run'):
    routine = f"""\
LOAD {geom}
CASE {case}
OPER
C1

x
st
{stOut}
t
h

quit
"""
    with open(filename, 'w') as file:
        file.write(routine)


def runAvl(routine='commands.run', avlPath='avl'):
    avl_command = f"{avlPath} < {routine}"
    subprocess.run(avl_command, shell=True, stderr=subprocess.STDOUT)

def parseOutput(stOut='stOut.txt'):
    with open(stOut, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    alpha = None
    CLtot = None
    CDtot = None
    e = None
    Elevator = None
    Flaps = None
    Ailerons = None
    Rudder = None

    # Iterate through each line and check for the required values
    for line in lines:
        try:
            if 'Alpha' in line:
                alpha = float(line.split('=')[1].split()[0])
            elif 'CLtot' in line:
                CLtot = float(line.split('=')[1].strip().split()[0])
            elif 'CDtot' in line:
                CDtot = float(line.split('=')[1].strip().split()[0])
            elif 'e =' in line and 'Plane' in line:
                e = float(line.split('=')[2].strip().split()[0])
            elif 'Elevator' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    Elevator = float(parts[1].strip().split()[0])
            elif 'Flaps' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    Flaps = float(parts[1].strip().split()[0])
            elif 'Ailerons' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    Ailerons = float(parts[1].strip().split()[0])
            elif 'Rudder' in line:
                parts = line.split('=')
                if len(parts) > 1:
                    Rudder = float(parts[1].strip().split()[0])
        except ValueError as ve:
            print(f"ValueError: {ve} on line: {line}")
        except IndexError as ie:
            print(f"IndexError: {ie} on line: {line}")

    return alpha, CLtot, CDtot, e, Elevator, Flaps, Ailerons, Rudder


def steadyLevelRoutine(avlGeom, avlCase):
    # Creates command file
    steadyLevelCommands(avlGeom, avlCase)

    # Runs AVL with command file created
    runAvl()

    # Parses ST output
    alpha, CLtot, CDtot, e, Elevator, Flaps, Ailerons, Rudder = parseOutput()

    # Delete the stability derivatives output file
    os.remove('stOut.txt')
    os.remove('commands.run')

    # Output the results
    print(f"Alpha: {alpha}")
    print(f"CLtot: {CLtot}")
    print(f"CDtot: {CDtot}")
    print(f"Oswald Efficiency (e): {e}")
    print(f"Elevator: {Elevator}") if Elevator else None
    print(f"Flaps: {Flaps}") if Flaps else None
    print(f"Ailerons: {Ailerons}") if Ailerons else None
    print(f"Rudder: {Rudder}") if Rudder else None

    polar = OutputAVL(
        alphaTrim=alpha,
        CLtot=CLtot,
        CDtot=CDtot,
        e=e,
        Elevator=Elevator,
        Flaps=Flaps,
        Ailerons=Ailerons,
        Rudder=Rudder)

    return polar
