# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:34:54 2023

@author: maria
"""
from openpyxl import load_workbook
import numpy as np

rutaleer = 'C:/Users/maria/OneDrive - Fundación Universitaria San Pablo CEU/CEU/Cursos/TERCERO/SEGUNDO CUATRIMESTRE/PROYECTOS II/WEKA/Resultados/Excels/'

grupo = 10
nodos = [59]

total = []

for n in nodos:
    archivoleer = rutaleer + 'G' + str(grupo) + '_' + str(n) + 'data'
    
    # LEER FICHEROS
    workbook = load_workbook(archivoleer + '.xlsx')
    
    # Seleccionar la hoja de trabajo
    sheet = workbook.active
    
    # Obtener los valores de las cinco columnas
    # frame = [cell.value for cell in sheet['A']]
    # actual = [cell.value.hour for cell in sheet['B']]
    # predicted = [cell.value.hour for cell in sheet['C']]
    error = [cell.value for cell in sheet['D']]
    # prediction = [cell.value for cell in sheet['E']]
    
    contador = 0
    for mas in error:
        if mas == '+':
            contador += 1
    
    print(contador)
    total.append(contador)