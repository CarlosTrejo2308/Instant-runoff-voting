# Registro de votos
votos = [
    [1, 2, 3],
    [0, 0, 1],
    [2, 3, 1],
    [0, 2, 1],
    [3, 1, 2],
    [2, 1, 3],
    [3, 2, 1],
    [1, 3, 2],
]

def mapaStarter(candidatos):
    adder = []
    for x in range(candidatos):
        adder.append(0)
    return [1, adder]

def preliminari(map, candidatos, goal):
    print("PRELIMINARI RESULTS:")
    print("\nCandidato\tVotos obtenidos(1)")
    ganador = -1
    for x in range(candidatos):
        obtenido = map[x][0]
        print("\n", x, "\t\t", obtenido, end = "" )
        if obtenido > goal:
            ganador = x
            print("*", end = "")
    print("\n---------------------------\n")
    if ganador > -1:
        print("El ganador es el candidato: ", ganador)
    else:
        print("Ningun candidato supero la meta en esta ronda")

    return ganador

def count(votos, candidatos):
    votantes = len(votos)
    goal = ( votantes / 2 )

    print("Votantes: {}\nGoal: {}".format(votantes, goal))
    print("")

    mapa = {} #voto [segundos] [terceros] [cuartos]

    # Getting first voters
    for votacion in votos:
        primero = votacion.index(1)
        if primero in mapa:
            listas = mapa[primero]
            listas[0] = listas[0] + 1
            mapa[primero] = listas
        else:
            mapa[primero] = mapaStarter(candidatos)

    ganador = preliminari(mapa, candidatos, goal)



    if ganador > -1:
        return

if __name__ == '__main__':
    count(votos, 3)
