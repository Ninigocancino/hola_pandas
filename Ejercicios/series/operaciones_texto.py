import pandas as pd

diccionario_empleados = {
    15379 : "Hernan Maldonado",
    15419 : "Carlos Zambrano",
    15420 : "Elena Domínguez",
    46556 : "Teresa Benítez",
    46555 : "Sonia Blaco",
}

serie_empleados = pd.Series(diccionario_empleados)

print("Serie:")
print(serie_empleados)

print("Minúsculas")
print(serie_empleados.str.lower())

print("Mayusculas")
print(serie_empleados.str.upper())

print("Longitud de los nombres")
print(serie_empleados.str.len())

print("Contiene el apellido Blaco")
print(serie_empleados.str.contains("Blaco"))

print("Reemplazar el apellido Blaco")
print(serie_empleados.str.replace("Blaco", "Blanco"))