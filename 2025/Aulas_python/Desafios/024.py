#Crie um programa que leia o nome de um cidade e diga se ela começa ou nao com o nome "SANTO".
cid = input("Em que cidade voce nasceu? ")
# Pega os primeiros 5 caracteres do nome da cidade e converte para maiúsculas
# para garantir que a comparação seja feita de forma consistente, independentemente da digitação
# Exemplo: "santo", "SANTO", "SaNto" serão comparados como "SANTO"
print(cid[:5].upper() == 'SANTO')  # Compara se os primeiros 5 caracteres são 'SANTO'
#Explicação:
# cid[:5]: Pega os primeiros 5 caracteres da cidade digitada.

# .upper(): Converte esses 5 primeiros caracteres para maiúsculas, para garantir que a comparação seja feita de forma consistente, independentemente do que o usuário digitar (exemplo: "santo", "SANTO", "SaNto", etc.).

# == 'SANTO': Compara os 5 primeiros caracteres com a palavra 'SANTO'.

# Agora, o código vai funcionar corretamente, verificando se os primeiros 5 caracteres da cidade são "SANTO".