"""Desafio Conversor de Medidas

Escrever programa que irá ler valor em metros e retornará em centimetros e milimetros

Passos: 
1 - Coletar número em metros
2 - fazer conversão para centimetro
3 - fazer conversão para milimetros
4 - exibir conversão na tela

"""

medidaMetro = float(input("Digite uma medida em metros: "))

medidaKm = medidaMetro * 100
medidaMm = medidaMetro * 1000

print("A medida de {} em centimetros é {}cm e em milimetros é {}mm".format(
    medidaMetro,medidaKm, medidaMm))
