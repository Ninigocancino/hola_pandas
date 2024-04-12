import pandas as pd

dic_empleados = {
    15000 : "Pepe Pecas",
    15001 : "Quijote Hidalgo",
    15002 : "Periquillo Zarniento"
}

s_empleados = pd.Series(dic_empleados)

print(s_empleados)
print(type(s_empleados))