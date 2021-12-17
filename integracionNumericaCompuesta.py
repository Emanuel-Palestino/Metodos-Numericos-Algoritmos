import numpy as np
from math import *

# Funcion Trapecio
def reglaCompuestaTrapecio(func, a, b, n):
	h = (b - a) / n
	res = 0
	# f(a)
	res = func(a)
	# Sumatoria
	suma = 0
	for i in range(1, n + 1):
		# sum(f(xi))
		suma += func(a + i * h)
	# 2*sum(f(xi))
	suma *= 2
	# f(b)
	res += suma + func(b)
	# h / 2
	res *= h / 2
	return res

# Funcion Simpson
def reglaCompuestaSimpson(func, a, b, n):
	h = (b - a) / n
	res = 0
	# f(x0)
	res = func(a)

	# Primer sumatoria
	suma = 0
	for i in range(n/2):
		suma += func((a + (2 * i + 1) * h))
	# 4 sum(f(2i + 1))
	suma *= 4
	res += suma

	# Segunda sumatoria
	suma = 0
	for i in range(n/2):
		suma += func(a + (2 * i) * h)
	
	# sum 2sum(f(x2i))
	suma *= 2
	res += suma + func(b)

	res *= h / 3
	return res


# Funciones de prueba
def funcion1(x):
	return exp(x)

def funcion2(x):
	return exp(x ** 2)

def funcion3(x):
	return x

# Prueba
print("Integracion Regla Compuesta del Trapecio\n")
print("Integral 1", reglaCompuestaTrapecio(funcion1, 0, 5, 1000))
print("Integral 2", reglaCompuestaTrapecio(funcion2, 0, 1, 1000))
print("Integral 2", reglaCompuestaTrapecio(funcion2, -5, 5, 1000))

print("Integracion Regla Compuesta de Simpson\n")
print("Integral 1", reglaCompuestaSimpson(funcion1, 0, 5, 1000))
print("Integral 2", reglaCompuestaSimpson(funcion2, 0, 1, 1000))
print("Integral 2", reglaCompuestaSimpson(funcion2, -5, 5, 1000))