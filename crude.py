#!/usr/bin/python3

import numpy as np
from JorGpi.POSCARloader import POSCARloader
from JorGpi.generate.loadsave import SavePOSCAR
from argv import Options
from sys import argv

options = Options(*argv)

# SETTINGS TODO: Read them from cmd line

mean     = options('mean') 
sigmoid  = options('sigmoid') 


# Parsing POSCAR file (first arg)
parser = POSCARloader(options('input'))
parser.parse()
data = parser(0)
del parser

#print(data)
for i,atom in enumerate(data['cell']):
	data['cell'][i] = (atom[0],np.dot(data['directions'],np.random.normal(mean,sigmoid[0],3))+atom[1])

SavePOSCAR(data,fileName=options('output'),multiplyers=[0,0,0])
