import pandas as pd

df_cleintes = pd.DataFrame({
    "nombre" : ["Luis", "Ana", "Sebastián", "Mateo"],
    "Ciudad" : ["Buenos Aires", "Lima", "Santiago", "Mexico"]
})

archivo = "clientes.csv"

df_cleintes.to_csv(archivo, index=False)
print("Archivo exportado")