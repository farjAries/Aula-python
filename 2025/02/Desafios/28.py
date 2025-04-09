#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir o numero pelo computardor o progrma devera escrever na tela se o usuario vanceu ou nao 
import random

numero= random.randint(1, 2)
escolha = int(input("Escolha um numero:"))

if escolha == numero:
    print('Voce Ganhou')
else:
    print('Tenta dnv')
#Acertei mas o dele ficou tao legal que vou colocar aqui

from random import randint
from time import sleep
#isso serve para o computador esperar um tempo antes de dar o proximo comando
numero= randint(1, 2)
print("#" * 60)
print("Vou pensar em um numero entre 1 e 2. Tente advinhar.....")
print("#" * 60)
escolha = int(input("Escolha um numero:"))
print("PROCESSANDO.....")
sleep(2)
if escolha == numero:
    print('VOCE GANHOU')
else:
    print('Tenta dnv')