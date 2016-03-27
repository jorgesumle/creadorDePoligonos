#!/usr/bin/env python
#-*- coding: utf-8 -*-

import turtle

lados = int(input("Introduce el número de lados que quieres que tenga el polígono\n>>> "))
pixelesPorLado = int(input("Introduce el tamaño cada lado en píxeles\n>>> "))

for lado in range(lados):
	turtle.forward(pixelesPorLado)
	turtle.right(360 / lados)
	
input() #Para que permanezca en pantalla el polígono al terminar la ejecución del bucle.
