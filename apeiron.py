#!/usr/bin/python3

import numpy as np
from JorGpi.POSCARloader import POSCARloader
from JorGpi.generate.loadsave import SavePOSCAR
from argv import Options
from sys import argv

options = Options(*argv)
# RANDOM GENERATOR
if options('seed') is not None:
	np.random.seed(seed=options('seed'))

def distribution(name,*args,**kwargs):
	try:
		if   name  == 'normal':
			return np.random.normal(*args[:2],**kwargs)
		elif name  == 'uniform':
			return np.random.uniform(*args[:2],**kwargs)
		elif name  == 'beta':
			return np.random.beta(*args[:2],**kwargs)
		elif name  == 'binomial':
			return np.random.binomial(*args[:2],**kwargs)
		elif name  == 'chisquare':
			return np.random.chisquare(*args[:1],**kwargs)
		elif name  == 'dirichlet':
			return np.random.dirichlet(*args[:1],**kwargs)
		elif name  == 'exponential':
			return np.random.exponential(*args[:1],**kwargs)
		elif name  == 'f':
			return np.random.f(*args[:2],**kwargs)
		elif name  == 'gamma':
			return np.random.gamma(*args[:2],**kwargs)
		elif name  == 'geometric':
			return np.random.geometric(*args[:1],**kwargs)
		elif name  == 'gumbel':
			return np.random.gumbel(*args[:2],**kwargs)
		elif name  == 'hypergeometric':
			return np.random.hypergeometric(*args[:3],**kwargs)
		elif name  == 'laplace':
			return np.random.laplace(*args[:2],**kwargs)
		elif name  == 'logistic':
			return np.random.logistic(*args[:2],**kwargs)
		elif name  == 'lognormal':
			return np.random.lognormal(*args[:2],**kwargs)
		elif name  == 'logseries':
			return np.random.logseries(*args[:1],**kwargs)
		elif name  == 'multinomial':
			return np.random.multinomial(*args[:2],**kwargs)
		elif name  == 'multivariate_normal':
			return np.random.multivariate_normal(*args[:2],**kwargs)
		elif name  == 'negative_binomial':
			return np.random.negative_binomial(*args[:2],**kwargs)
		elif name  == 'noncentral_chisquare':
			return np.random.noncentral_chisquare(*args[:2],**kwargs)
		elif name  == 'noncentral_f':
			return np.random.noncentral_f(*args[:3],**kwargs)
		elif name  == 'pareto':
			return np.random.pareto(*args[:1],**kwargs)
		elif name  == 'poisson':
			return np.random.poisson(*args[:1],**kwargs)
		elif name  == 'power':
			return np.random.power(*args[:1],**kwargs)
		elif name  == 'rayleigh':
			return np.random.rayleigh(*args[:1],**kwargs)
		elif name  == 'standard_cauchy':
			return np.random.standard_cauchy(**kwargs)
		elif name  == 'standard_exponential':
			return np.random.standard_exponential(**kwargs)
		elif name  == 'standard_gamma':
			return np.random.standard_gamma(*args[:1],**kwargs)
		elif name  == 'standard_normal':
			return np.random.standard_normal(**kwargs)
		elif name  == 'standard_t':
			return np.random.standard_t(*args[:1],**kwargs)
		elif name  == 'triangular':
			return np.random.triangular(*args[:3],**kwargs)
		elif name  == 'vonmises':
			return np.random.vonmises(*args[:2],**kwargs)
		elif name  == 'wald':
			return np.random.wald(*args[:2],**kwargs)
		elif name  == 'weibull':
			return np.random.weibull(*args[:1],**kwargs)
		elif name  == 'zipf':
			return np.random.zipf(*args[:1],**kwargs)
	except (TypeError,ValueError) as err:
		print("You probably feed the distribution with wrong numbers")
		print(err)
		exit()

sigmoid  = options('sigmoid') 

# Parsing POSCAR file (first arg)
parser = POSCARloader(options('input'))
parser.parse()
data = parser(0)
del parser

if   'atom' in options('mode'):
	for i,atom in enumerate(data['cell']):
		data['cell'][i] = (atom[0],np.dot(data['directions'],distribution(options('distribution'),*sigmoid,size=3))+atom[1])
if 'direct' in options('mode'):
	for i,_ in enumerate(data['directions']):
		data['directions'][i] += np.dot(data['directions'],distribution(options('distribution'),*sigmoid,size=3))

SavePOSCAR(data,fileName=options('output'),multiplyers=[0,0,0])
