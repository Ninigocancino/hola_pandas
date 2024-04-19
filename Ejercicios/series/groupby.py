import pandas as pd 

df_ventas = pd.DataFrame({
    'productos' : ['computadora', 'telefono', 'computadora', 'telefono','computadora', 'telefono','computadora', 'telefono'],
    'mes': ['enero', 'enero','febrero','febrero','marzo','marzo','abril','abril'],
    'ventas' : [10000,12000,15000,18000,20000,22000,15000,18000]
})

print("DatFrame original: ")
print(df_ventas)

grupos = df_ventas.groupby('productos')
resultados = grupos.agg({
    'ventas': ['mean', 'sum']
})

print("Resultado del agrupamiento")
print(resultados)