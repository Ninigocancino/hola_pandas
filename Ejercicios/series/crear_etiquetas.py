import pandas as pd

list_mail = [ "uno@empresa.com", "dos@emresa.com", "tres@empresa.com"]

etiquetas_id = [15001,15002,15003]
serie_mail = pd.Series(list_mail,index=etiquetas_id)

print(serie_mail)

print(serie_mail[15002])