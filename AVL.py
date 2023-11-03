"""
AVL automation functions for running AVL subprocess through Python

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""

import os
import sys
import subprocess as sp


def saveGeometry(geom, loud=True):
    pavl = sp.Popen(['AVL.exe'], stdin=sp.PIPE, stdout=None if loud else sp.DEVNULL, stderr=None)

    def command(command):
        if (sys.version_info > (3, 0)):
            command = command.encode('ascii')
        pavl.stdin.write(command)

    command(f'load {geom}\n')
    command('oper\n')
    command('g\n')
    command('h')


def getStabilityDerivatives(geom, case, output, loud=True):
    # pavl = sp.Popen(['avl.exe'], stdin=sp.PIPE, stdout=None if loud else sp.DEVNULL, stderr=None, universal_newlines=True)
    pavl = sp.Popen(['avl.exe', f'load {geom}\n', f'case {case}\n', f'oper\nc1\n\nx\nst\n{output}.txt\n\nquit\n'], stdin=sp.PIPE, stdout=None if loud else sp.DEVNULL, stderr=None, universal_newlines=True)

    def command(command):
        pavl.stdin.write(command)

    # # Load geometry and case
    # command(f'load {geom}\n')
    # command(f'case {case}\n')
    #
    # # Oper routine and set straight level trim, execute flow
    # command('oper\n')
    # command('g\n\n')
    # command('c1\n\n')
    # command('x\n')
    #
    # # Get stability derivatives and output
    # command(f'st\n{output}.txt\n\n')
    # command('quit\n')
