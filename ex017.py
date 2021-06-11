"""
Desafio 017 - cateto e hipotenusa 



catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto Adjacente: '))
hipotenusa= (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print("A hipotenusa mede {:.2f}".format(hipotenusa))

"""
#import math
from math import hypot
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto Adjacente: '))
hipotenusa = hypot(catetoOposto,catetoAdjacente)
print("A hipotenusa mede {:.2f}".format(hipotenusa))
