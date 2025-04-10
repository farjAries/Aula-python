distancia = int(input("qual foi a distancia da viagem: "))
preço = distancia * 0.50
desconto = distancia * 0.45
if distancia > 200:
    print(f'Voce esta preste a fazer uma viagem de {distancia}KM')
    print(f"E o preço da sua passagem será de R${desconto:.2f}")
else:
    print(f'Voce esta preste a fazer uma viagem de {distancia}KM')
    print(f'E o preço da sua passagem sera de R${preço:.2f}')