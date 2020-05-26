"""
Exp. educativa: Evaluación de sistemas interactivos
Ejercicio: Alpha de Cronbach en Python
Por: Epsom Enrique Segura Jaramillo

Detalles:
    -Resultado obtenido: 0.359
"""

import sys, pandas, numpy

data_1 = pandas.read_csv(sys.argv[1], delimiter = ';')

cabeceras = data_1.columns.values
cabeceras = numpy.delete(cabeceras, 0)

varianzas = []
for c in cabeceras:
    varianzas.append(data_1[c].var())

varianza_total = varianzas[cabeceras.size-1]
del varianzas[cabeceras.size-1]
sum_varianzas = 0
for v in varianzas:
    sum_varianzas += v
num_items = len(varianzas)

salida = ((num_items/(num_items-1))*(1-(sum_varianzas/varianza_total)))

print(round(salida, 3))