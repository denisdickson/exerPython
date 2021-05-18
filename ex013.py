"""
Desafio 013 - Aumento de 15%
    Fazer um algoritmo que leia o salário de um funcionario e mostre seu
    novo salario, com 15% de aumento.

    Passos:
    1- Perguntar salário
    2- Calcular 15% do salário
    3- somar os 15% ao salário
    4- Exibir resultado
"""

salario = float(input("Digite salário do funcionário:R$"))
novoSalario = salario + (salario * 15 / 100)
print("Seu novo salario é R${:.2f}".format(novoSalario))
