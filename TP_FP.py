# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:57:33 2023

@author: maria
"""

import numpy as np

def Calcular_Se_PPV (matriz_confusion) :
        
    diagonal = np.diag(matriz_confusion)
    columnas = np.sum(matriz_confusion, 0)
    filas = np.sum(matriz_confusion, 1)
    
    np.seterr(divide='ignore', invalid='ignore') # para que no se impriman los warnings al dividir entre 0 o nan
    
    # SENSIBILIDAD
    sensibilidad = np.divide(diagonal, filas)
    
    # PPV
    PPV = np.divide(diagonal, columnas)

    return sensibilidad, PPV


# EL FICHERO QUE SE LEE ES EL EXCEL

ruta = 'C:/Users/maria/OneDrive - Fundación Universitaria San Pablo CEU/CEU/Cursos/TERCERO/SEGUNDO CUATRIMESTRE/PROYECTOS II/WEKA/Resultados/Matrices/'
nombre = '' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
archivoleer = ruta + nombre + '.txt'
matriz = np.loadtxt(archivoleer, dtype=int)
print(matriz)

true_positives = np.diag(matriz)
# print(true_positives)
false_positives = np.sum(matriz, axis=0) - true_positives
# los false positives se encuentran en la columna de una clase específica (positiva) y fuera de la fila correspondiente a esa clase
# print(false_positives)

TP = np.sum(true_positives)
FP = np.sum(false_positives)
sensibilidad, PPV = Calcular_Se_PPV (matriz)

fichero = ruta + nombre + 'statistics.txt'
with open(fichero, "w") as archivo:
    # Escribir cada variable en una línea separada
    archivo.write('TP: ' + str(TP) + "\n")
    archivo.write('FP: ' + str(FP) + "\n")
    archivo.write('Sens: ' + str(sensibilidad) + "\n")
    archivo.write('PPV: ' + str(PPV) + "\n")


# with open(archivoleer, 'a') as archivo:
#     # Escribe el contenido adicional en el archivo
#     archivo.write("\nhola")