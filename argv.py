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
        self.opt.__dict__['sigmoid']         = np.array(self.opt.__dict__['sigmoid'])
        self.opt.__dict__['distribution']    = self.opt.__dict__['distribution'].lower()
        self.opt.__dict__['mode']            = self.opt.__dict__['mode'].lower()
        if 'all' in self.opt.__dict__['mode']:
            self.opt.__dict__['mode'] = 'atoms;directions'
        if self.opt.__dict__['mean'] is not None:
            self.opt.__dict__['sigmoid']         = np.array([self.opt.__dict__['mean'],
		                                            *self.opt.__dict__['sigmoid']])
        if self.opt.__dict__['distribution'] in ['beta', 'binomial', 'f', 'gamma', 'gumbel',
			                         'laplace', 'logistic', 'lognormal', 
						 'multinomial', 'multivariate_normal',
						 'negative_binomial', 'noncentral_chisquare',
						 'normal', 'uniform', 'vonmises', 'wald',
						 'hypergeometric', 'noncentral_f', 'triangular'] \
						 and len(self.opt.__dict__['sigmoid']) < 2:
            self.opt.__dict__['sigmoid']         = np.array([0.0, *self.opt.__dict__['sigmoid']])
        if self.opt.__dict__['distribution'] in ['hypergeometric', 'noncentral_f', 'triangular'] \
			                         and len(self.opt.__dict__['sigmoid']) < 3:
            self.opt.__dict__['sigmoid']         = np.array([0.0, *self.opt.__dict__['sigmoid']])

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
                                \"uniform\", \"beta\", \"binomial\", \"chisquare\", \"dirichlet\",\
				\"exponential\", \"f\", \"gamma\", \"geometric\", \"gumbel\",\
				\"hypergeometric\", \"laplace\", \"logistic\", \"lognormal\",\
				\"logseries\", \"multinomial\", \"multivariate_normal\",\
				\"negative_binomial\", \"noncentral_chisquare\", \"noncentral_f\",\
				\"pareto\", \"poisson\", \"power\", \"rayleigh\", \"standard_cauchy\",\
				\"standard_exponential\", \"standard_gamma\", \"standard_normal\",\
				\"standard_t\", \"triangular\", \"vonmises\", \"wald\", \"weibull\",\
				\"zipf\" cf. https://numpy.org/doc/stable/reference/random/generator.html')
        self.parser.add_argument('--seed', '-S', type=int, default=None,
			help='seed for the pseudorandom number generator')
        self.parser.add_argument('--mean', '-m', type=np.float, default=None,
                help='mean value of the distribution; if set will prepend sigmoid list')
        self.parser.add_argument('--sigmoid', '-s', default=[1e-4],nargs='+',type=np.float,
			help='parameters of the distribution (number may vary; default: 1e-4 each)')

    def __call__(self, key):
        try:
            return self.opt.__dict__[key]
        except KeyError:
            print("No key \"%s\" defined, please try: "%key)
            print("%s"%(str(self.keys)))
            exit(Error.access)
