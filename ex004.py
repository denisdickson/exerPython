#Dissecando uma váriavel : Fazer um programa que leia algo -
# pelo teclado e mostre na tela o seu:
#Tipo primitivo e todas informações possíveis

a = input('Digite algo: ')
print(" o tipo primitivo desse valor é" ,  type(a))
print('Só tem espaços?', a.isspace())
print('is numeric?', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumeric?', a.isalnum())
print('esta maisculo?', a.isupper())
print('esta minusculo?', a.islower())
print('esta capitalizada?', a.istitle())