"""

Desafio 021 --- Tocando mp3

"""
from random import shuffle  
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')

lista = [nome1,nome4, nome2, nome3]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)