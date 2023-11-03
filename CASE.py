"""
Case file creation functions for AVL

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""

def createTrimmedCase(filename, casename, velocity, mass, flaps=True, ailerons=True, elevator=True, rudder=True, rho=1.225, Ixx=0.1, Iyy=0.1, Izz=0.04):
    with open(filename, 'a') as f:
        f.truncate(0)
        f.write(f"---------------------------------------------\nRun case  1:  {casename}\n")
        f.write("alpha        ->  CL          =   0.00000\n")
        f.write("beta         ->  beta        =   0.00000\n")
        f.write("pb/2V        ->  pb/2V       =   0.00000\n")
        f.write("qc/2V        ->  qc/2V       =   0.00000\n")
        f.write("rb/2V        ->  rb/2V       =   0.00000\n")
        f.write("Flaps        ->  Flaps       =   0.00000\n") if flaps else None
        f.write("Aileron      ->  Aileron     =   0.00000\n") if ailerons else None
        f.write("Elevator     ->  Cm pitchmom =   0.00000\n") if elevator else None
        f.write("Rudder       ->  Cn yaw  mom =   0.00000\n\n") if rudder else None

        f.write(f"velocity  =  {velocity}               Lunit/Tunit\n")
        f.write(f"density   =  {rho}              Munit/Lunit^3\n")
        f.write("grav.acc. =  9.81            Lunit/Tunit^2\n")
        f.write(f"mass      =  {mass}             Munit\n\n")

        f.write(f"Ixx = {Ixx}      Munit-Lunit^2\n")
        f.write(f"Ixy = 0      Munit-Lunit^2\n")
        f.write(f"Izx = 0      Munit-Lunit^2\n")
        f.write(f"Iyy = {Iyy}      Munit-Lunit^2\n")
        f.write(f"Iyz = 0      Munit-Lunit^2\n")
        f.write(f"Izz = {Izz}      Munit-Lunit^2\n")
