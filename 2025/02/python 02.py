# Potência (**)
print(5 ** 2)  # 5² = 25

# Divisão normal (/)
print(5 / 2)   # 5 ÷ 2 = 2.5

# Divisão inteira (//)
print(5 // 2)  # 5 ÷ 2 = 2 (descarta a parte decimal)

# Módulo (%)
print(5 % 2)   # Resto de 5 ÷ 2 = 1

# Parênteses () → Sempre resolvidos primeiro.
# Exponenciação ** → Potência.
# Multiplicação *, Divisão /, Divisão inteira //, e Módulo % → São resolvidos da esquerda para a direita.
# Soma + e Subtração - → São resolvidos por último, da esquerda para a direita.

resultado = 5 + 2 * 3  # Multiplicação antes da soma
print(resultado)  # 11 (pois 2 * 3 = 6, depois 5 + 6 = 11)

resultado = (5 + 2) * 3  # Parênteses antes da multiplicação
print(resultado)  # 21 (pois 5 + 2 = 7, depois 7 * 3 = 21)

resultado = 2 ** 3 * 4  # Exponenciação antes da multiplicação
print(resultado)  # 32 (pois 2³ = 8, depois 8 * 4 = 32)

resultado = 10 // 3 + 1  # Divisão inteira antes da soma
print(resultado)  # 4 (pois 10 // 3 = 3, depois 3 + 1 = 4)

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:<20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:=>20}!'.format(nome))
print('Prazer em te conhecer! {:^20}' .format(nome))

#Desafio 5
n1 = int(input('Digite um valor: '))
sucessor = n1 + 1 
antecessor = n1 -1
print('o sucessor de {} é {} e antecessor é {}'.format(n1, sucessor, antecessor))

#Desafio 6
n2 = int(input("Digite um Numero:"))
dobro = n2 * 2
triplo = n2 * 3
rquadrada = n2 ** n2
print("O numero {}, o Dobro é{} o triblo é {} e a raiz quadrada é {}".format(n2, dobro, triplo, rquadrada))
#Desafio 7
nota1 = float(input("Qual a primeira nota do aluno? "))
nota2 = float(input("Qual a segunda nota do aluno? "))
media = (nota1 + nota2) / 2
print("A primeira nota do aluno é {}, a segunda nota do aluno é {}, e a media dele é {}".format(nota1, nota2, media))
#Desafio 08
metros = float(input("Quantos metros: "))
cm = metros * 100
mm = metros *1000
print(f"{metros}Metros convertido em centimetros é {cm:.0f} e em milimetro é {mm:.0f}")
#um novo jeito de fazer o print é colocar em vez de print("{} bla bla".format(variavel)) posso so colocar print(f"{variavel} bla bla")