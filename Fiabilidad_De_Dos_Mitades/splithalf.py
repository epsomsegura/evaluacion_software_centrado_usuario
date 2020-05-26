"""
Exp. educativa: Evaluación de sistemas interactivos
Ejercicio: Fiabilidad de dos mitades
Por: Epsom Enrique Segura Jaramillo

Detalles:
    -Resultado obtenido: 0.16
"""

import sys, pandas, numpy

sum_x = 0
sum_x2 = 0
sum_y = 0
sum_y2 = 0
sum_xy = 0

data_1 = pandas.read_csv(sys.argv[1], delimiter = ';')


for index, row in data_1.iterrows():
    sum_x += row['Nones']
    sum_x2 += numpy.square(row['Nones'])
    sum_y += row['Pares']
    sum_y2 += numpy.square(row['Pares'])
    sum_xy += (row['Nones'] * row['Pares'])

N = data_1['Participante'].size

r = ((N*sum_xy)-(sum_x*sum_y)) / numpy.sqrt(((N * sum_x2) - numpy.square(sum_x)) * ((N * sum_y2) - numpy.square(sum_y)))

salida = (2 * r) / (1 + r)

print(round(salida, 3))