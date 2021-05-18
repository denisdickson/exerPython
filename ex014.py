"""
Desafio 014 - Conversor de medidas Cº para F¹
    Faça um algoritmo que: Converta uma medida em Celsius para Farenheit
Passos:
    1- Obter temperatura em Celsius
    2- Fazer conversão para Farenheit
    3- exibir resultado
"""

temperaturaCelsius = float(
    input("Digite a temperatura em ºC que deseja converter: _Cº "))
farenheit = 9*temperaturaCelsius/5+32
print("A temperatura {:.2f}Cº é equivalente à {:.2f}Fº".format(
    temperaturaCelsius, farenheit))
