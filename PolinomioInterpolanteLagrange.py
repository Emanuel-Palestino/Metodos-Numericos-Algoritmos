import numpy as np
from math import *
from sympy import *
import matplotlib.pyplot as plt

# Funcion que se va a utilizar
def func(x):
	return 1/x

# Obtener los puntos desde la consola
tamaño = 3
puntos = np.array([2, 2.5, 4])

#for i in range(tamaño):
#	texto = "\nIngresa el punto " + str(i) + ": "
#	puntos.append(float(input(texto)))


# Funcion para caluclar Ln,k
def L(nodos, k):
	res = 1
	x = Symbol('x')
	for i in range(len(nodos)):
		if (i != k):
			res *= (x - nodos[i]) / (nodos[k] - nodos[i])
	return res

# Funcion para obtener el polinomio interpolante de Lgrange
def polinomioLagrange(nodos, funcion):
	res = 0
	for k in range(len(nodos)):
		res += funcion(nodos[k]) * L(nodos, k)
	return simplify(res)


## Probando el codigo
polinomio = polinomioLagrange(puntos, func)
print(polinomio)

## Obtener puntos del polinomio
puntosFuncion = []
puntosLagrange = []
puntos2 = np.linspace(1, 5, 1000)
for i in range(len(puntos2)):
	puntosFuncion.append(func(puntos2[i]))
	puntosLagrange.append(polinomio.subs('x', puntos2[i]))

## Mostrar la grafica
y = func(puntos)
plt.plot(puntos, y, 'ro')
plt.plot(puntos2, puntosFuncion)
plt.plot(puntos2, puntosLagrange)
plt.show()