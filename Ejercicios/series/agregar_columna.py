import pandas as pd

df_clientes = pd.DataFrame({
    "nombre" : ["Luis", "Ana", "Sebastián", "Sofia", "Mateo", "Camila","Valentin"],
    "edad" : [35,30,32,41,47,23,20],
    "ciudad" : ["Buenos Aires", "Lima","México", "Santiago","Alajuela","Nueva York", "Toronto"]
})

lista_profesion = ["Medico", "Ingeniero civil", "Abogado", "Profesora", "Contador", "Enfermera", "Estudiante"]
df_clientes["profesión"] = lista_profesion

print(df_clientes)