"""
Desafio 015 - Aluguel de carros 
    Faça um algoritmo que : Pergunte a quantidade de Km percorridos 
    e quantidade de dias alugado, Calcule o valor a pagar 
    Diaria R$60 Km rodado R$0.15

Passos
1- Verificar quantidade de Km percorrido
2- Verificar quantidade de Dias alugado
3 - Calcular valor a ser pago 
4 - Exibir total 
"""

kmPercorrido = float(input("Digite a kilometragem percorrida: "))
diasAlugado = float(input("Digite a quantidade de dias que foi alugado:"))
valorTotal = (kmPercorrido*60.00)+(diasAlugado*0.15)
print("O valor total a ser pago é de R${:.2f}".format(valorTotal))
