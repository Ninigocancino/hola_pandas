import pandas as pd

diccionario_empleados = {
    15379 : "Hernan Maldonado",
    15419 : "Carlos Zambrano",
    15420 : "Elena Dominguez",
    46556 : "Teresa Benitez",
    46555 : "Sonia Blanco"
}

#covierte el diccionario en una serie
serie_empleados = pd.Series(diccionario_empleados)

print("Serie")
print(serie_empleados)

serie_ordenada_valores = serie_empleados.sort_values(ascending=True)

#ordena la serie por valores
print("Serie ordenada por valores:")
print(serie_ordenada_valores)

#ordena la serie por indice
serie_ordenada_indice = serie_empleados.sort_index()
print("Serie ordenada por indice:")
print(serie_ordenada_indice)