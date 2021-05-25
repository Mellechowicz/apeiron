#!/usr/bin/python3

import numpy as np
from JorGpi.POSCARloader import POSCARloader
from JorGpi.generate.loadsave import SavePOSCAR
from sys import argv

parser = POSCARloader(argv[1])
parser.parse()
data = parser(0)
del parser

data['cell'][0] = ('W',np.array([-1.,-1.,-1.]))
SavePOSCAR(data,fileName='POSCAR.out',multiplyers=[0,0,0])
