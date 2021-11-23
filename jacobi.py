import numpy as np
from math import *

# Pedir el tamaño de la matriz
tamaño = int(input('Tamaño de la matriz: '))

# Crear matriz que se utilizará
matriz = np.zeros(tamaño * tamaño).reshape(tamaño, tamaño)
# Vector inicial
vectorColumna = []

# Rellenar matriz desde consola
print("Rellenar matriz de", tamaño, "x", tamaño, "(Una fila en cada linea y las columna separadas por espacios):\n")
for i in range(tamaño):
	fila = input("")
	fila = fila.split(" ")
	for j in range(tamaño):
		matriz[i][j] = float(fila[j])

# Rellenar el vector columna desde consola
print("\nRellenar el vector columna (Cada fila separada por espacios):\n")
fila = input("");
fila = fila.split(" ")
for i in range(tamaño):
	vectorColumna.append(float(fila[i]))


# Algoritmo de Jacobi
def jacobi(mat, vector, X0):
	# Todos los vectoresX que se van a utilizar
	vectoresX = []
	# Inicializamos X
	vectoresX.append(X0)

	# Se ejecuta Jacobi
	bandera = True
	k = 1
	while bandera:
		# Vector de las nuevas X
		vectorXk = []
		# Despejar cada una de las nuevas x
		for i in range(tamaño):
			# Calculamos el despeje de xi
			res = vector[i]
			for j in range(tamaño):
				if j != i:
					res -= mat[i][j] * vectoresX[k - 1][j]
			res /= mat[i][i]

			# Agregamos al vector Xk  el valor de xi
			vectorXk.append(res)

		# Comprobamos el error relativo
		if errorRelativoNormaEuclidiana(vectorXk, vectoresX[k - 1]) < 1e-5:
			bandera = False

		# Agregamos el vector resultante al arreglo de vectoresX
		vectoresX.append(vectorXk)
		k += 1

	return vectoresX.pop()

# Función para calcular el error relativo utilizando la norma euclidiana
def errorRelativoNormaEuclidiana(vector1, vector0):
	numerador = 0
	denominador = 0
	for i in range(len(vector1)):
		numerador += (vector1[i] - vector0[i]) ** 2
		denominador += vector1[i] ** 2
	numerador = sqrt(numerador)
	denominador = sqrt(denominador)

	return numerador / denominador


# PROBAR

vectorX0 = np.zeros(tamaño).reshape(tamaño, 1)

print(jacobi(matriz, vectorColumna, vectorX0))