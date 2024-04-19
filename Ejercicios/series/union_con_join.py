import pandas as pd

df_datos_personal = pd.DataFrame({
    "id": [15379,15419,15420],
    "nombre" : ["Hernan", "Carlos", "Elena"],
    "apellido" : ["Maldonado", "Zambrano","Dominguez"],
    "edad" : [35,30,32],
    "email" : ["hmalconado@kineteco.com", "czambrano@kineteco.com","edominguez@kineteco.com"]
})

df_datos_puesto = pd.DataFrame({
    "id" : [15379,15419,46555],
    "puestos" : ["Ingeniero I","vicepresidente RHH", "Manufacturación"],
    "lugar" : ["Texa","California","Maryland"]
})

union_dataframes = pd.merge(df_datos_personal, df_datos_puesto, on="id", how="left")
print("Colaboradores sin puesto asociado: ")
print(union_dataframes)