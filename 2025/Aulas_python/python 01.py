#Desafio 01
nome = input('Digite seu nome: ')
print('È um prazer te conhecer ', nome)
#outro jeito mais para o futuro
print('È um prazer {}' .format(nome))

# Aula 06 Tipos primitivos e Saida de Dados
# https://www.youtube.com/watch?v=hdDHg1p3YVc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=9
#int numero inteiro (7, -4, 0, 1121)
# float Numeros Flutantes ou real (4.5, 0.0052, -15.223) 
# bool só aceita dois valores True e False
# str String 'Ola', '7.5' ""
n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma vale', s)
#um outro jeito de fazer isso, sinxtase nova python
print('A soma do valor {}'.format(s))
#Para ver o tipo do valor coloco um type
print(type(s))
#desafio 02
print('A soma entre {} e {} vai dar {}'.format(n1, n2, s))

#Desafio 02
numero01 = int(input("Digite um numero:"))
numero02 = int(input("Digite outro numero:"))
valor = numero01 + numero02
print("A soma de {} e {} da {}".format(numero01, numero02, valor))

#Desafio 03
palavra = input('Digite alguma coisa:')
print (type(palavra))
print ('Só tem espaço',palavra.isspace()) 
print('È um numero', palavra.isnumeric())
print('è alfabetico', palavra.isalpha())
print('È Alfanumerico ',palavra.isalnum())
print('Esta em maiscula: ', palavra.isupper())
print('esta em minuscula', palavra.islower())
print('Esta capitalizada? ', palavra.istitle())