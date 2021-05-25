#!/usr/bin/python3

import numpy as np
from JorGpi.POSCARloader import POSCARloader
from JorGpi.generate.loadsave import SavePOSCAR
from sys import argv

# SETTINGS TODO: Read them from cmd line

mean     = 0.0
deviance = 0.000001 # 1% change


# Parsing POSCAR file (first arg)
parser = POSCARloader(argv[1])
parser.parse()
data = parser(0)
del parser

print(data)
for i,atom in enumerate(data['cell']):
	data['cell'][i] = (atom[0],np.dot(data['directions'],np.random.normal(mean,deviance,3))+atom[1])

SavePOSCAR(data,fileName='POSCAR.out',multiplyers=[0,0,0])
