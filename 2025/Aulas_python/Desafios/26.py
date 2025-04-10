Palavra = str(input("Digite uma palavra: ")).upper().strip()
vezes = Palavra.count('A')


print(f"A letra A aparece {vezes} vezes na frase ")
print("A letra esta na posiçao {} Pela primeira vez".format(Palavra.find('A')+1))
print('A lerta A esta na posiçao {} pela ultima vez'.format(Palavra.rfind('A')+1))
#Como ele Começa do 0 vai dar 'errado' ja que a gente prefere a posiçao humana que começa com 1 ent colocamos +1 para que ele pegue a posiçao e forme mais +1 
