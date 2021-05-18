""" Desafio 11 : 
   Leia largura e altura, calcule a área  
   E quantas latas de tintas são necessárias para pintar     
    sabe-se 1lt de tinta == Área de 2m²
"""

largura = float(input("Qual a largura de sua parede? m²"))
altura = float(input("Qual a altura de sua parede? m²"))
area = largura * altura
tinta = area /  2

print("Para pintar a área equivalente a {}m², são necessários {} latas de tinta ".format(area, tinta))
