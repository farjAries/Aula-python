Ano = int(input("Que ano quer analisar? "))

# Usar a lógica correta de bissexto
bissexto = (Ano % 4 == 0) and ((Ano % 100 != 0) or (Ano % 400 == 0))

if bissexto:
    print("É bissexto")
else:
    print("Não é bissexto")
