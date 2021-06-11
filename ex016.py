"""
Desafio 016 - Quebrano número 
    Criar um programa para ler um número real e mostrar apenas parte inteira

from math import trunc 

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,trunc(num)))

"""

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))