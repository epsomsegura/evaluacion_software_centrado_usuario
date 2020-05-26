"""
Exp. educativa: Evaluación de sistemas interactivos
Ejercicio: Test-Retest
Por: Epsom Enrique Segura Jaramillo

Detalles:
    -Resultado obtenido: 286
"""

import sys, pandas, numpy

data_1 = pandas.read_csv(sys.argv[1], delimiter = ';')

sum_x = 0
sum_x2 = 0
sum_y = 0
sum_y2 = 0
sum_xy = 0

for index, row in data_1.iterrows():
    sum_x += row['Test Score']
    sum_x2 += numpy.square(row['Test Score'])
    sum_y += row['Retest Score']
    sum_y2 += numpy.square(row['Retest Score'])
    sum_xy += (row['Test Score'] * row['Retest Score'])

N = data_1['Participant'].size

salida = ((N * sum_xy) - (sum_x * sum_y))/(numpy.sqrt(((N * sum_x2) - numpy.square(sum_x)) * ((N * sum_y2) - numpy.square(sum_y))))

print(round(salida, 3))