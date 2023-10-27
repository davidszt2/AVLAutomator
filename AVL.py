"""
AVL automation functions for running AVL subprocess through Python

@Author:    David Moeller Sztajnbok
@Date:      October, 2023
"""

import os
import sys
import subprocess as sp



def saveGeometry(geom, loud=True):
    pavl = sp.Popen(['AVL.exe'], stdin=sp.PIPE, stdout=sp.DEVNULL if loud else None, stderr=None, creationflags=sp.DETACHED_PROCESS)

    def command(command):
        if (sys.version_info > (3, 0)):
            command = command.encode('ascii')
        pavl.stdin.write(command)

    command(f'load {geom}\n')
    command('oper\n')
    command('g\n')
    command('h')
