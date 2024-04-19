import pandas as pd

df_empleados = pd.DataFrame({
    'nombre' : ['Hernan', 'Carlos', 'Elena', 'Teresa'],
    'apellido' : ['Maldonado', 'Zambrano', 'Dominguez', 'Benitez'],
    'edad' : [35,30,32,41],
    'email': ['hmaldonano@interinc.com', 'czambrano@interinc.com','edominguez@interinc.com', 'tbenitez@test.com']
})

print("Dataframe original: ")
print(df_empleados)

print("Nombres en mayúsculas: ")
df_empleados['nombre'] = df_empleados['nombre'].str.upper()
print(df_empleados['nombre'])

print("")

print("Correos electrónicos que tienen la palabra ez")
print(df_empleados[df_empleados['email'].str.contains('ez', case=False)])

print("Todos los correos electrónicos finalizan con interinc.com")
print(df_empleados[~df_empleados['email'].str.endswith('interinc.com')])