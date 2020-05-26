"""
Exp. educativa: Evaluación de sistemas interactivos
Ejercicio: Equivalencia racional
Por: Epsom Enrique Segura Jaramillo

Detalles:
    -Resultado obtenido: 0.772
"""

import sys, pandas, numpy

data_1 = pandas.read_csv(sys.argv[1], delimiter = ';')
data_2 = pandas.read_csv(sys.argv[2], delimiter = ';')

sum_pq = 0
for p in data_1['P']:
    sum_pq += p * (1-p)

num_items = data_1['Items'].size
varianza = data_2['Score'].var()

salida = (num_items/(num_items-1)) * (1-(sum_pq/varianza))

print(round(salida, 3))