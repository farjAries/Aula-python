#<!---------------- CONDIÇÕES  SIMPLES E COMPOSTAS------------------------------------------------!>

tempo = int(input("Quantos anos tem seu carro?"))

if tempo<=3:
    print("carro ta novo")
else:
    print("carro velho")
#SE o tempo do carro for menor(<) ou igual(=) ele printa oque eu falei(print("carro ta novo")) se nao ele printa a outra palavra(print("carro velho"))

nome = str(input("Qual o seu nome?"))
if nome == 'Fernando':
    print(f"oi Fernando")
else:
    print(f'salve fpd')
#Ele pergunta meu nome SE o nome digitado for igual a Fernando ele imprimi oi fernando se nao ele fla salve fdp; Isso é condiçao

Nm = str(input('Qual o seu nome'))
if Nm == 'ze':
    print('Que nome bonito')
print(f'Boa tarde {Nm}')
#Copia do video mas entendi ja 
#nome = str(input("Qual o seu nome?"))
#if nome == 'Fernando':
#    print(f"oi {Nome}")
#else:
#    print(f'salve fpd {nome}')
#Eu fiz desse jeito tmb, nao muda muita coisan mas achei bom tmb


n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))

media = (n1 + n2)/2
if media >= 5:
    print(f'Parabens Voce passou, voce tirou {media}')
else:
    print(f"Vish ta feio a coisa voce so tioru {media}")
#De uma outra forma
#print('PARABENS' if m>=6 else 'ESTUDE MAIS')