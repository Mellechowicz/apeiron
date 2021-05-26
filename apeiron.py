#!/usr/bin/python3

import numpy as np
from JorGpi.POSCARloader import POSCARloader
from JorGpi.generate.loadsave import SavePOSCAR
from argv import Options
from sys import argv

options = Options(*argv)

# Read them from cmd line
# RANDOM GENERATOR
mean     = options('mean') 
sigmoid  = options('sigmoid') 
print(mean,*sigmoid)

if options('seed') is not None:
	np.random.seed(seed=options('seed'))

def distribution(name,*args,**kwargs):
	if   name  == 'normal':
		try:
			return np.random.normal(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'uniform':
		try:
			return np.random.uniform(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'beta':
		try:
			return np.random.beta(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'binomial':
		try:
			return np.random.binomial(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'chisquare':
		try:
			return np.random.chisquare(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'dirichlet':
		try:
			return np.random.dirichlet(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'exponential':
		try:
			return np.random.exponential(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'f':
		try:
			return np.random.f(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'gamma':
		try:
			return np.random.gamma(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'geometric':
		try:
			return np.random.geometric(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'gumbel':
		try:
			return np.random.gumbel(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'hypergeometric':
		try:
			return np.random.hypergeometric(*args[:3],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'laplace':
		try:
			return np.random.laplace(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'logistic':
		try:
			return np.random.logistic(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'lognormal':
		try:
			return np.random.lognormal(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'logseries':
		try:
			return np.random.logseries(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'multinomial':
		try:
			return np.random.multinomial(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'multivariate_normal':
		try:
			return np.random.multivariate_normal(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'negative_binomial':
		try:
			return np.random.negative_binomial(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'noncentral_chisquare':
		try:
			return np.random.noncentral_chisquare(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'noncentral_f':
		try:
			return np.random.noncentral_f(*args[:3],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'normal':
		try:
			return np.random.normal(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'pareto':
		try:
			return np.random.pareto(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'poisson':
		try:
			return np.random.poisson(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'power':
		try:
			return np.random.power(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'rayleigh':
		try:
			return np.random.rayleigh(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'standard_cauchy':
		try:
			return np.random.standard_cauchy(**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'standard_exponential':
		try:
			return np.random.standard_exponential(**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'standard_gamma':
		try:
			return np.random.standard_gamma(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'standard_normal':
		try:
			return np.random.standard_normal(**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'standard_t':
		try:
			return np.random.standard_t(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'triangular':
		try:
			return np.random.triangular(*args[:3],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'uniform':
		try:
			return np.random.uniform(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'vonmises':
		try:
			return np.random.vonmises(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'wald':
		try:
			return np.random.wald(*args[:2],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'weibull':
		try:
			return np.random.weibull(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()
	elif name  == 'zipf':
		try:
			return np.random.zipf(*args[:1],**kwargs)
		except (TypeError,ValueError) as err:
			print("You probably feed the distribution with wrong numbers")
			print(err)
			exit()


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
