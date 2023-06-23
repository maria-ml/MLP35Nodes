# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:23:27 2023

@author: maria
"""

import numpy as np


ruta = 'C:/Users/maria/OneDrive - Fundación Universitaria San Pablo CEU/CEU/Cursos/TERCERO/SEGUNDO CUATRIMESTRE/PROYECTOS II/WEKA/Resultados/Matrices/'
# nombre = 'mtotal35_Files'
nombre = 'mtotal35_Frame'
archivoleer = ruta + nombre +  '.txt'
matriz = np.loadtxt(archivoleer, dtype=int)
print(matriz)




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