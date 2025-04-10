
# Potência (**)
print(5 ** 2)  # 5² = 25

# Divisão normal (/)
print(5 / 2)   # 5 ÷ 2 = 2.5
#Desafio 10
dinheiro = float(input("Quanto dinhero voce tem na carteira? "))
dolar = float(input("quanto esta a cotaçao do dolar? "))

# Divisão inteira (//)
print(5 // 2)  # 5 ÷ 2 = 2 (descarta a parte decimal)
valor = dinheiro /  dolar

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
print(f"com {dinheiro} voce pode comprar US${valor:.2f}")
# Desafio 10
reais = float(input("Quantos reais você quer converter? "))
cotacao = float(input("Qual a cotação atual do dólar? "))

dolares = reais / cotacao

print(f"Com R${reais:.2f}, você terá aproximadamente ${dolares:.2f} dólares.")

# Desafio 11
largura = float(input("Quanto de largura tem:"))
altura = float(input("Quanto de altura tem: "))
metros = largura * altura
litros = metros / 2
print(f"Sua parede tem {largura}X{altura} e sua area é de {metros}m Para pintar essa parede, voce precisa de {litros}Litros de tinta")

# Desafio 12 
valor = float(input("Qual o valor? "))
Desconto = valor * 5 / 100
sub = valor - Desconto
print(f"O Produto que custava R${valor} , na promoçao vai custar {sub:.2f}")

#Desafio 13
salario = float(input("Qual o salario do Funcionario: R$"))
aumento = salario * 15 / 100
total = salario + aumento
print(f"O Funcionario que ganhava {salario} agora com o aumento de 15% esta ganhando {total:.2f}")

#Desafio 14
c = float(input("Informe a temperatura em celcius: "))
f = (c * 1.8 ) + 32
print(f"A temperatura de {c}C corresponde a {f:.2f}F")
#Desfio 15
dias = float(input("Qunatos dias o carro foi alugado? "))
km = float(input("Quantos km foi percorrido")) 
final = (dias  * 60) + (km * 0.15)
print(f"O total a pagar é {final:.2f}")