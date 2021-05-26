# -*- coding: utf-8 -*-
import argparse as ap
import numpy as np
import re

class Error:
    access = 123

class Options:
    keys = [ "input", "output", "mode", "seed", "distribution", "mean", "sigmoid" ]

    def __init__(self, *args):
        self.parser = ap.ArgumentParser(description='Find minimal number of unique spin-flips')
        self.add_arguments_io()
        self.add_arguments_mode()
        self.add_arguments_distribution()

        self.opt = self.parser.parse_args(args[1:])
        self.fix_data()

    def fix_data(self):
        print( self.opt.__dict__['sigmoid'])
        self.opt.__dict__['sigmoid'] = np.array(self.opt.__dict__['sigmoid'])


    def add_arguments_io(self):
        self.parser.add_argument('--input', '-i', default='POSCAR',
             help='input POSCAR file')
        self.parser.add_argument('--output', '-o', default='output.vasp',
             help='output POSCAR file')

    def add_arguments_mode(self):
        self.parser.add_argument('--mode','-M', default='atoms',
             help='mode name (default \"atoms\"); modyfies\
                     (\"atoms\")       all atomic positions\
		     (\"directions\")  all directions\
		     (\"all\")         everything')

    def add_arguments_distribution(self):
        self.parser.add_argument('--distribution', '-d', default='normal',
			help='Probablity density function used for random number generator:\
				\"normal\"(default)\
				\"uniform\"')
        self.parser.add_argument('--seed', '-S', type=int, default=None,
			help='pseudorandom number generator')
        self.parser.add_argument('--mean', '-m', type=np.float, default=0.0,
                help='mean value of the distribution (default 0)')
        self.parser.add_argument('--sigmoid', '-s', default=[1e-4],nargs='+',type=np.float,
			help='parameters of the distribution (number may vary; default: 1e-4 each)')

    def __call__(self, key):
        try:
            return self.opt.__dict__[key]
        except KeyError:
            print("No key \"%s\" defined, please try: "%key)
            print("%s"%(str(self.keys)))
            exit(Error.access)
