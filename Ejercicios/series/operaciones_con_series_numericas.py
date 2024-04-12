import pandas as pd

lista_numerica = [20,30,40,50,60,70,80]
serie_numerica = pd.Series(lista_numerica)


print("suma")
#con operadores de python
resultado_suma = serie_numerica + 5
print(resultado_suma)
#con el método incluido en Pandas
resultado_suma = serie_numerica.add(5)
print(resultado_suma)


print("resta")
#Con operadores de Python
resultado_resta = serie_numerica - 10
print(resultado_resta)
#Con método de Pandas
resultado_resta= serie_numerica.subtract(10)
print(resultado_resta)

print("Multiplicar")
resultado_multiplicar = serie_numerica * 3
print(resultado_multiplicar)
resultado_multiplicar = serie_numerica.multiply(3)
print(resultado_multiplicar)

print("dividir")
resultado_division = serie_numerica / 2
print(resultado_division)
resultado_division = serie_numerica.div(2)
print(resultado_division)

print("Modulo")
resultado_mod = serie_numerica % 2
print(resultado_mod)
resultado_mod = serie_numerica.mod(2)
print(resultado_mod)

print("Exponente")
resultado_exponente = serie_numerica ** 2
print(resultado_exponente)
resultado_exponente = serie_numerica.pow(2)
print(resultado_exponente)