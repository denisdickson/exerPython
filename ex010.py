""" Desafio 10 :
    Criar um programa que leia saldo disponivel e equivalente em dolares 

    1- ler saldo
    2- converter saldo em dolares
    3 - exiber saldo e equivalente em dolares 
"""

saldo = float(input("Digite seu saldo disponível em reais: "))
conversao = saldo * 0.19
print("Seu saldo em reais é R${} em dolares é US${}".format(saldo, conversao))
