# copilot: disable
# 

#Utilizando Módulos 
#para importar uma biblioteca uso o comando import
#se eu quiser uma variavel especifica de um biblioteca devo colocar from NOME_DA_BIBLIOTECA import NOME_DA_VARIAVEL 

from math import sqrt, ceil
num = int(input("Valor: "))
raiz = sqrt(num)
print('A raiz de {} a {}'.format(num, ceil(raiz)))

import random
num = random.randint(1, 5)
print(num)

import emoji
print(emoji.emojize('Python is :thumbs_up:'))

#Desafio 16
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.
import math

valor = float(input('Por favor digite um numero?'))
inteira = math.trunc(valor)
print(inteira)



#Desafio 17 
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math #nao consegui fazer sem ver a resposta

# Passo 1: Receber os valores dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Passo 2: Calcular a hipotenusa usando o Teorema de Pitágoras
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Passo 3: Exibir o resultado
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")

#Desafio 18
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math #nao consegui fazer sem ver a resposta

angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno do angulo {angulo} é {seno:.2f}')
print(f'O cosseno do angulo {angulo} é {cosseno:.2f}')
print(f'A tangente do angulo {angulo} é {tangente:.2f}')

#Desafio 19     
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

alunos = ['Luis', 'Fernando', 'Roberta', 'andre']
escolhido = random.choice(alunos)
print('dos alunos {} quem foi o escolhido foi {}' .format(alunos, escolhido))



#Desafio 20
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto aluno: '))

juncao = [aluno4, aluno3, aluno2, aluno1]
random.shuffle(juncao)
print('A ordem de apresentação será {}'.format(juncao))



#Desafio 21
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame #nao consegui fazer sem ver a resposta
pygame.init()
pygame.mixer.music.load('08ver.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

