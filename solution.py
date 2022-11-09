postos = [2, 15, 22, 10.2]  # Distancia Posto de Combustivel
km_litro = 8  # km por litro
combustivel = 0
localizacao = 0
distancia = 0


def entrada_usuario():
    global localizacao
    global combustivel

    localizacao = float(input("Qual sua localização?"))
    combustivel = float(input("Quantos litros de combustivel?"))


def calcular():
    entrada_usuario()
    distancia = combustivel / km_litro
    print(distancia)


def p_posto_mais_distante_possivel():
    global distancia
    global postos
    index = 0

    for i, item in enumerate(postos):
        postos[i] = item**2


calcular()
p_posto_mais_distante_possivel()
