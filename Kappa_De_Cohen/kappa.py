"""
Exp. educativa: Evaluación de sistemas interactivos
Ejercicio: Kappa de Cohen
Por: Epsom Enrique Segura Jaramillo

Detalles:
    -Resultado obtenido: 0.185
"""

import sys, pandas, numpy

data_1 = pandas.read_csv(sys.argv[1], delimiter = ';')

# Coincidencias
ccb = 0
ccr = 0
ccm = 0

# Evaluador 1
ce1b = 0
ce1r = 0
ce1m = 0

# Evaluador 2
ce2b = 0
ce2r = 0
ce2m = 0

for index, row in data_1.iterrows():    
    if row['Evaluador 1'] == 'Bueno': ce1b += 1
    elif row['Evaluador 1'] == 'Regular': ce1r += 1
    elif row['Evaluador 1'] == 'Malo': ce1m += 1

    if row['Evaluador 2'] == 'Bueno': ce2b += 1
    elif row['Evaluador 2'] == 'Regular': ce2r += 1
    elif row['Evaluador 2'] == 'Malo': ce2m += 1

    if(row['Evaluador 1'] == row['Evaluador 2']):
        if row['Evaluador 1'] == 'Bueno': ccb += 1
        elif row['Evaluador 1'] == 'Regular': ccr += 1
        elif row['Evaluador 1'] == 'Malo': ccm += 1

N = data_1['Sistema'].size        

Po = (1 / N) * (ccb + ccr + ccm)
Pe = (1 / numpy.square(N)) * ((ce1b * ce2b) + (ce1r * ce2r) + (ce1m * ce2m))

salida = (Po - Pe) / (1 - Pe)

print(round(salida, 3))