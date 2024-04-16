import pandas as pd

serie_empleados = pd.Series({
    15379 : "Hernan Maldonado",
    14419 : None, 
    15420 : "Monica Domínguez",
    46556 : "Teresa Benitez",
    46555 : None
})

print(serie_empleados)

print("Identificar valores faltantes")
print(serie_empleados.isna())

print("Total de valores faltantes")
print(serie_empleados.isna().sum())