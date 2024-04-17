from numpy import NaN
import pandas as pd

serie_empleados = pd.Series(
    {
        15379 : "hmaaldonado@hotmail.com",
        15419 : None,
        15420 : "edominguez@hotmail.com",
        46556 : "tbenitez@hotmail.com",
        46559 : None
    }
)

print("Eliminar registro")
eliminar_registros = serie_empleados.dropna()
print(eliminar_registros)

print("Remplazar valores faltantes por 'Desconocido' ")
reemplazar_registros = serie_empleados.fillna('desconocido')
print(reemplazar_registros)

diccionario_temperaturas = {
    2010 : 73,
    2011: NaN,
    2012: 75.3,
    2013: 72.4,
    2014: 72.5,
    2015: NaN,
    2016: NaN,
    2017: 73.5,
    2018: 72.7,
}

serie_temperaturas = pd.Series(diccionario_temperaturas)

print("Reemplazar valores faltantes por la media")
reemplazar_temperaturas = serie_temperaturas.fillna(serie_temperaturas.mean)
print(reemplazar_temperaturas)