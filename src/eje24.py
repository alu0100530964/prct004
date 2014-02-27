#!/usr/bin/python
#!encoding: UTF-8
from math import *

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))
if a != 0:
	x1 = (-b + sqrt(b**2 - 4*(a*c))) / (2 * a)
	x2 = (-b - sqrt(b**2 - 4*(a*c))) / (2 * a)
	print 'Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)
else:
	if b != 0:
		x = -c / b
		print 'La solucion de la ecuacion es: x=%4.3f' % x
	else:
		if c != 0:
			print 'La ecuacion no tiene solucion'
		else:
			print 'La ecuacion tiene infinitas soluciones'
			
# Hace que si a es distinto de cero entonces es una ecuacion de segundo grado y la resuel con la fórmula
# si a es igual a cero entonces la ecuación es de primer grado y se resuelve como en el ejercicio 24
# Notese que a,b,c son del tipo float y las soluciones saldran tipo float. Si en la raíz sale negativa el programa no hace la ecuación de segundo grado porque da error

