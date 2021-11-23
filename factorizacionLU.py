import numpy as np

# Matriz que se utilizará
tamaño = 3
matriz = np.zeros(tamaño*tamaño).reshape(tamaño, tamaño)
vectorColumna = []

# Rellenar matriz desde consola
print("Rellenar matriz de", tamaño, "x", tamaño, "(Una fila en cada linea y las columna separadas por espacios):\n")
for i in range(tamaño):
	fila = input("")
	fila = fila.split(" ")
	for j in range(tamaño):
		matriz[i][j] = float(fila[j])
print("\nRellenar el vector columna (Cada fila separada por espacios):\n")
fila = input("");
fila = fila.split(" ")
for i in range(tamaño):
	vectorColumna.append(float(fila[i]))

# Funcion de resolucion de un sistema triangular inferior (Sustitucion hacia adelante)
def sustitucionAdelante(mat, columna):
	resultadosFilas = []
	for i in range(len(columna)):
		resultadoTemporal = 0.0
		resultadoTemporal = columna[i]
		if i >= 1:
			for j in range(i):
				resultadoTemporal -= mat[i][j] * resultadosFilas[j]

		resultadoTemporal /= mat[i][i]
		resultadosFilas.append(resultadoTemporal)
	return resultadosFilas

# Funcion de resolucion de un sistema triangular superior (Sustitucion hacia atras)
def sustitucionAtras(mat, columna):
	matrizTamaño = len(columna)
	resultadoFilas = np.zeros(matrizTamaño).reshape(matrizTamaño)
	for i in range(1, matrizTamaño + 1):
		resultadoTemporal = 0.0
		resultadoTemporal = columna[matrizTamaño - i]
		if matrizTamaño - i <= matrizTamaño - 2:
			for j in range(1, i):
				resultadoTemporal -= mat[matrizTamaño - i][matrizTamaño - j] * resultadoFilas[matrizTamaño - j]
		resultadoTemporal /= mat[matrizTamaño - i][matrizTamaño - i]
		resultadoFilas[matrizTamaño - i] = resultadoTemporal
	return resultadoFilas


# Factorizacion LU
def factorizacionLU(mat, columna):
	matrices = []
	matrizTamaño = len(columna)

	# Crear Matrices
	U = np.array(mat)
	L = np.zeros(matrizTamaño**2).reshape(matrizTamaño, matrizTamaño)

	# Rellenar diagonal de la matriz L
	for i in range(matrizTamaño):
		L[i][i] = 1
	
	# trabajar matriz U
	for i in range(1, len(mat[0])):
		for j in range(i):
			L[i][j] = U[i][j] / U[j][j]
			U[i] = U[i] - U[i][j] / U[j][j] * U[j]
	
	matrices.append(L)
	matrices.append(U)
	return matrices


haciaAtras = factorizacionLU(matriz, vectorColumna)
print("\nResultado:")
print("\nL = \n", haciaAtras[0])
print("\nU = \n", haciaAtras[1])
