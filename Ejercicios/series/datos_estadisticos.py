import pandas as pd 

df_ventas = pd.DataFrame({
    'productos' : ['computadora', 'telefono', 'computadora', 'telefono','computadora', 'telefono','computadora', 'telefono'],
    'mes': ['enero', 'enero','febrero','febrero','marzo','marzo','abril','abril'],
    'ventas' : [10000,12000,15000,18000,20000,22000,15000,18000]
})

print("DatFrame original: ")
print(df_ventas)

print("")

print("Estadística Descriptiva: ")
print(df_ventas.describe())

print("")

print("Medidas de tendencia central: ")
print(f"Media: {df_ventas["ventas"].mean()}")
print(f"Mediana: {df_ventas['ventas'].median()}")
print(f"Moda: {df_ventas['ventas'].mode()}")