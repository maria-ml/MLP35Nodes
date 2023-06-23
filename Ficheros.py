# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:19:50 2023

@author: maria
"""

# contar los frames que tienen los ficheros de test
# guardarlos en un array
# utilizar ese array para saber hasta donde llega la clasificación
# utilizar la funcion de tino


# CLASIFICADOR DIAGNOSIS MAYORITARIA POR FICHEROS

from openpyxl import load_workbook
import numpy as np
import csv
import re
import os


ruta = 'C:/Users/maria/OneDrive - Fundación Universitaria San Pablo CEU/CEU/Cursos/TERCERO/SEGUNDO CUATRIMESTRE/PROYECTOS II/WEKA/'

fichero = 'testTotal' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Define variable to load the dataframe
workbook = load_workbook(ruta + fichero + '.xlsx')
 
# Define variable to read sheet
sheet = workbook.active


# Obtener los valores de las cinco columnas
subject = [cell.value for cell in sheet['A']]
print(subject)
files = []
    
for i in range (0, len(subject)):
    # seria hasta len - 1 pero el último indice no se ejecuta
    numero = subject[i]
    # print(numero)
    pattern = re.compile(r'^' + str(numero) + '\D.*\.txt$')

    for filename in os.listdir('.'):

        if pattern.match(filename):
            print(filename)
            files.append(filename)       

print(files)