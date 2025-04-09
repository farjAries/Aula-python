Velocidade = float(input("Qual a velocidade do carro: "))
multa = (Velocidade - 80 ) * 7
if Velocidade< 80:
    print("\033[33m Tenha um otimo dia\033[0m")
else:
    print(f"\033[31m Como voce estava a {Velocidade}KMs voce foi Multado em \033[33mR${multa}\033[0m")