#!Python3
""" Desafio 12 - Calcular descontos :
        Algoritmo parar ler o preço de um produto e 
       aplicar um desconto de 5%.
    Passos:
     1 - Ler preço
     2 - Calcular desconto
     3 - Calcular novo preço com desconto
     4 - Exibir valores

"""
preco = float(
    input("Digite o preço do produto que deseja aplicar o desconto: R$"))
desconto = preco * 5/100
descontoAplicado = preco - desconto
print("O desconto para R${:.2f}  é de R${:.2f}, totalizando R${:.2f}".format(
    preco, desconto, descontoAplicado))
