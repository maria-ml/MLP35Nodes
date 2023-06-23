# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:41:45 2023

@author: maria
"""

import numpy as np


ruta = 'C:/Users/maria/OneDrive - Fundación Universitaria San Pablo CEU/CEU/Cursos/TERCERO/SEGUNDO CUATRIMESTRE/PROYECTOS II/WEKA/Resultados/Matrices/'
nombre = 'mtotal35_' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
tipo = 'Files' + '_H_NH'
archivoleer = ruta + nombre + tipo + '.txt'
matriz = np.loadtxt(archivoleer, dtype=int)
print(matriz)



def Calcular_acc_err (matriz_confusion) :
        
    diagonal = np.diag(matriz_confusion)
    columnas = np.sum(matriz_confusion, 0)
    filas = np.sum(matriz_confusion, 1)
    
    np.seterr(divide='ignore', invalid='ignore') # para que no se impriman los warnings al dividir entre 0 o nan
    
    # SENSIBILIDAD
    accuracy = np.divide(diagonal, filas)
    fAccuracy = accuracy*100
    
    # PPV
    error_rate = 100 - fAccuracy
    
    suma = np.sum(matriz_confusion, dtype=np.int32)
    d = np.sum(diagonal, dtype=np.int32)
    # print(suma)
    # print(d)
    
    totalA = (d/suma ) * 100
    totalE = 100 - totalA
    

    return fAccuracy, error_rate, totalA, totalE

acc, err, totalA, totalE = Calcular_acc_err(matriz)
# print(acc, err)


fichero = ruta + nombre + tipo + 'statistics.txt'
with open(fichero, "w") as archivo:
    # Escribir cada variable en una línea separada
    archivo.write("Accuracy of the system: "+ str(totalA) + "\n")
    archivo.write("Error_rate of the system: "+ str(totalE) + "\n")
    for i in range(len(acc)):
        print("Class", i+1, "Accuracy:", acc[i])
        archivo.write("Class " + str(i+1) + " Accuracy: "+ str(acc[i]) + "\n")
        print("Class", i+1, "Error Rate:", err[i])
        archivo.write("Class " + str(i+1) + " Error Rate: " + str(err[i]) + "\n")



# num_classes = matriz.shape[0]

# accuracies = []
# error_rates = []

# for i in range(num_classes):
#     true_positive = matriz[i, i]
#     # print(true_positive)
#     false_positive = np.sum(matriz[:, i]) - true_positive
#     # print(false_positive)
#     false_negative = np.sum(matriz[i, :]) - true_positive
#     # print(false_negative)
#     true_negative = np.sum(matriz) - (true_positive + false_positive + false_negative)
#     # print(true_negative)
    
#     accuracy = (true_positive + true_negative) / np.sum(matriz)
#     error_rate = 1 - accuracy
    
#     accuracies.append(accuracy)
#     error_rates.append(error_rate)

# # Print results



# if num_classes == 8:
#     fichero = ruta + nombre + tipo + 'statistics.txt'
#     with open(fichero, "w") as archivo:
#     # Escribir cada variable en una línea separada
#         for i in range(num_classes):
#             print("Class", i+1, "Accuracy:", accuracies[i])
#             archivo.write("Class " + str(i+1) + " Accuracy: "+ str(accuracies[i]) + "\n")
#             print("Class", i+1, "Error Rate:", error_rates[i])
#             archivo.write("Class " + str(i+1) + " Error Rate: " + str(error_rates[i]) + "\n")
# else:
    
#     fichero = ruta + nombre + tipo + '_statistics.txt'
#     with open(fichero, "w") as archivo:
#     # same values for both classes
#         print("Accuracy:", accuracies[0])
#         archivo.write("Accuracy: " + str(accuracies[0]) + "\n")
#         print("Error Rate:", error_rates[0])
#         archivo.write("Error Rate: " + str(error_rates[0]) + "\n")
    