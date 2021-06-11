"""
Desafio 018 ---  Seno, Cosseno e Tangente

"""

#import math
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno =sin(radians(angulo))
print('O angulo de {} tem o seno de{:.2f}'.format(angulo, seno))

cosseno = cos(radians(angulo))
print('O angulo de {} tem o cosseno de{:.2f}'.format(angulo, cosseno))

tangente =tan(radians(angulo))
print('O angulo de {} tem a tangente de {:.2}'.format(angulo,tangente))
