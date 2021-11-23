import numpy as np
from math import *

# vector solucion
vectorColumna = [0, 0, 0]
# cantidad de las ecuaciones
numEcuaciones = 3

# Arreglo de ecuaciones
arrEcuaciones = []

def jacobi(vector, ecuaciones, tolerancia, ii):
	ii += 1
	# hacer para todas las ecuaciones
	nuevoVector = []
	for i in range(numEcuaciones):
		variables = [0, 1, 2]
		# Obtener el valor de xi en la ecuacion i
		variables.remove(i)
		nuevoVector.append(ecuaciones[i](vector[variables[0]], vector[variables[1]]))
	
	# Obtenemos el error relativo para saber si terminamos
	if (errorRelativoNormaInfinita(nuevoVector, vector) < tolerancia):
		return [nuevoVector, ii]
	else:
		# actualizar vector de soluciones
		return jacobi(nuevoVector, ecuaciones, tolerancia, ii)


def errorRelativoNormaInfinita(vectorK, vectorK0):
	# Recorrer el tamaño de los vectores
	vectorNumerador = []
	vectorDenominador = []
	for i in range(len(vectorK)):
		vectorNumerador.append(abs(vectorK[i] - vectorK0[i]))
		vectorDenominador.append(abs(vectorK[i]))

	# obtener el maximo de cada vector y retornar el resultado de la division
	return max(vectorNumerador) / max(vectorDenominador)


# EJECUTAR

## Ecuaciones originales
def ecuacion1(x1, x2, x3):
	return 3 * x1 - cos(x2 * x3) - 0.5

def ecuacion2(x1, x2, x3):
	return x1 ** 2 - 81 * (x2 + 0.1) ** 2 + sin(x3) + 1.06

def ecuacion3(x1, x2, x3):
	return exp(-x1 * x2) + 20 * x3 + (10 * pi - 3) / 3


## Ecuaciones despejadas
def ec1(x2, x3):
	return (cos(x2 * x3) + 0.5) / 3

def ec2(x1, x3):
	return sqrt(x1 ** 2 + sin(x3) + 1.06) / 9 - 0.1

def ec3(x1, x2):
	return -(exp(-x1 * x2) / 20) + (3 - 10 * pi) / 60

## Insertar ecuaciones en el arreglo de ecuaciones

arrEcuaciones.append(ec1)
arrEcuaciones.append(ec2)
arrEcuaciones.append(ec3)

## LLamar a jacobi
resultado = jacobi(vectorColumna, arrEcuaciones, 1e-5, 0)
print("\nResultado con ", resultado[1], " iteraciones = ", resultado[0])
resultado = resultado[0]
print("\nEcuacion 1 evaluada = ", ecuacion1(resultado[0], resultado[1], resultado[2]))
print("\nEcuacion 2 evaluada = ", ecuacion2(resultado[0], resultado[1], resultado[2]))
print("\nEcuacion 3 evaluada = ", ecuacion3(resultado[0], resultado[1], resultado[2]))