import numpy as np
from math import *

# Número de ecuaciones
numEcuaciones = 3

## Vector columna inicial
vectorColumna = []
for i in range(numEcuaciones):
	vectorColumna.append(0.1)

def newthonRaphson(vector, ecuaciones, tolerancia, ii):

	return 0

# EJECUCION

## Ecuaciones originales
def ecuacion1(x1, x2, x3):
	return 3 * x1 - cos(x2 * x3) - 0.5

def ecuacion2(x1, x2, x3):
	return x1 ** 2 - 81 * (x2 + 0.1) ** 2 + sin(x3) + 1.06

def ecuacion3(x1, x2, x3):
	return exp(-x1 * x2) + 20 * x3 + (10 * pi - 3) / 3

## Matriz Jacobiana
### ec00
def ec00(x1, x2, x3):
	return 3

def ec01(x1, x2, x3):
	return x3 * sin(x2 * x3)

def ec02(x1, x2, x3):
	return x2 * sin(x2 * x3)

def ec10(x1, x2, x3):
	return 2 * x1

def ec11(x1, x2, x3):
	return -162 * (x2 + 0.1)

def ec12(x1, x2, x3):
	return cos(x3)

def ec20(x1, x2, x3):
	return -x2 * exp(-x1 * x2)

def ec21(x1, x2, x3):
	return -x1 * exp(-x1 * x2)

def ec22(x1, x2, x3):
	return 20

### Rellenar la matriz Jacobiana
J = [[ec00, ec01, ec02], [ec10, ec11, ec12], [ec20, ec21, ec22]]