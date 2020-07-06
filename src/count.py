# Registro de votos
ballot = [
    [1, 2, 3],
    [0, 0, 1],
    [2, 3, 1],
    [0, 2, 1],
    [3, 1, 2],
    [2, 1, 3],
    [3, 2, 1],
    [1, 3, 2],
]

NAMES = [
    "Red",
    "Blue",
    "Green"
]
def mapStarter(options):
    adder = []
    for x in range(options):
        adder.append(0)
    return [1, adder]

def preliminary(map, options, goal):
    print("PRELIMINARY RESULTS:")
    print("\nCandidate\tVotes obtained(1)")
    winner = -1

    for x in range(options):
        got = map[x][0]
        print("\n", NAMES[x], "\t\t", got, end = "" )

        if got > goal:
            winner = x
            print("*", end = "")


    print("\n---------------------------\n")
    if winner > -1:
        print("The winner is: ", NAMES[winner])
    else:
        print("No candidate won in this round")

    return winner

def count(ballot, options):
    voters = len(ballot)
    goal = ( voters / 2 )

    print("Voters: {}\nGoal: {}".format(voters, goal))
    print("")

    map = {} #voto [segundos] [terceros] [cuartos]

    # Getting first voters
    for vote in ballot:
        first = vote.index(1)
        if first in map:
            lists = map[first]
            lists[0] = lists[0] + 1
            map[first] = lists
        else:
            map[first] = mapStarter(options)

    ganador = preliminary(map, options, goal)

    if ganador > -1:
        return

if __name__ == '__main__':
    count(ballot, 3)
