#Crie um Programa que leia o nome completo de uma pessoa e mostre:
# o Nome com todas as letras maisculas
# o nome com todas minuculas.
# Qunatas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input("Qual o seu nome? ")
print("Analisando seu nome...")
print("Seu nome em maiusculas é " + nome.upper()) #o Nome com todas as letras maisculas
print("Seu nome em minúsculas é " + nome.lower()) # O nome com todas minuculas.
print("Seu nome tem ao todo " + str(len(nome.strip().replace(" ","")))) #Conta quantas letras tem sem os espaços

#Pega o primeiro nome e conta quantas letras tem somente o primeiro nome
primeiro_nome = nome.split()[0]
print("Seu nome é {} e ele tem {} letras" .format(primeiro_nome.capitalize(), len(primeiro_nome)))


