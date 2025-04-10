#Faça um programa que leia um numero de 0 a 99999 e mostre na tela cada um dos digitos separados
# EX: Digite um número:1834
# unideade:4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input("Digite um número: "))
u = numero % 10
d = (numero // 10) % 10
c = (numero // 100) % 10
m = (numero // 1000) % 10
print(f"Analisando o numero: {numero}")
print(f"Unidade: {u}")
print(f"Unidade: {d}")
print(f"Unidade: {c}")
print(f"Unidade: {m}")