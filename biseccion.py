import math
from math import *

def fun(x):
	return exp(x) - x - 2

val = 1e-10

def find(a, b, p1):
	p = a + (b - a) / 2
	if abs(fun(p)) < val:
		return p
	elif abs(p1 - p) < val:
		return p
	elif abs(p1 - p) / abs(p) < val:
		return p
	else:
		if fun(p) * fun(a) > 0:
			return find(p, b, p)
		else:
			return find(a, p, p)

point = find(0, 5, 0)

print(point)