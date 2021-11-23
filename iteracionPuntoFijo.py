from math import *

def raizCubica(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root

# Metodo de Iteración de Punto Fijo
def iPuntoFijo(forma, p0, tolerancia):
	p = p0
	i = 0
	while(True):
		i += 1
		pn = forma(p)
		# Error porcentual
		if (abs(pn - p)/abs(pn)) * 100 < tolerancia or i == 1 or i == 2 or i == 3:
			if i >= 10:
				return pn
			else:
				p = pn
		else:
			return 'La forma no converge'


# EJECUCION

# Funciones
def funcion1(x):
	return -2 * sin(pi * x)

# Pruebas
punto = iPuntoFijo(funcion1, 1.5, 10)
print(punto)