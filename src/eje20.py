#!/usr/bin/python
#!encoding: UTF-8

x = -b/a
a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

print 'Solucion: ', x

# Da error porque las variables se declaran despues de la declaracion de la x
# NameError: name 'b' is not defined

