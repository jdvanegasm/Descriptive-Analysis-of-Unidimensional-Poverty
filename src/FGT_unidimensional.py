#Importar modulos

import pandas as pd

#%% Crear el DataFrame con datos ficticios
data = {'Ingreso': [5, 15, 35, 45, 24]}

df = pd.DataFrame(data)

#%%Fijar los parametros:

# Línea de pobreza

lp = 20

# Parámetros alfa para FGT(0), FGT(1), FGT(2)
alfas = [0, 1, 2]

#%% Función para calcular FGT

def calculate_fgt(df, lp, alfa):
    x = []
    for ingreso in df['Ingreso']:
        if ingreso < lp:
            x.append((1 - ingreso / lp) ** alfa)
        else:
            x.append(0)
    df['x'] = x
    FGT = df['x'].sum() / len(df)
    return FGT

#%% Calcular FGT(0), FGT(1), FGT(2)
fgt_results = {}
for alfa in alfas:
    FGT = calculate_fgt(df, lp, alfa)
    fgt_results[f'FGT({alfa})'] = FGT

# Mostrar resultados
print(fgt_results)