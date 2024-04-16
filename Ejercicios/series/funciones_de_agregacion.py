import pandas as pd

salariosAnuales = [120000.0, 55346.0, 60089.9, 75020.8]
serie_salarios = pd.Series(salariosAnuales)
print(serie_salarios)

print("Total salarios:")
total_salarios = serie_salarios.sum()
print(total_salarios)

print("Promedio de salarios:")
promedio_salarios = serie_salarios.mean()

print("Salario Máximo:")
maximo_salarios = serie_salarios.max()
print(maximo_salarios)

print("Salario Mínimo:")
salario_minimo = serie_salarios.min()
print(salario_minimo)

print("Mediana salario")
mediana_salarios = serie_salarios.median()
print(mediana_salarios)