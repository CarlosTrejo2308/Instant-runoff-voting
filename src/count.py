# Ballot count
ballot = [
    [1, 2, 3],
    [0, 0, 1],
    [2, 3, 1],
    [0, 1, 2],
    [3, 1, 2],
    [2, 1, 3],
    [3, 2, 1],
    [1, 3, 2],
]

#Names of the candidates by position
NAMES = [
    "Red",
    "Blue",
    "Green"
]

# Initializes the counting map for each candidate
def mapStarter(options):
    adder = []
    for x in range(options):
        adder.append(0)
    return [1, adder]

#Shows the preliminary results of the first count
def preliminary(map, options, goal):
    print("PRELIMINARY RESULTS:")
    print("\nCandidate\tVotes obtained(1)")

    #Keeping track if there's a clesar winner, and who is the loser in the
    #first round
    winner = -1
    loser = [-1, -1] #index - votes

    # For each candidate
    # check the map to count the voters
    # and keep track of winners and losers
    for candidate in range(options):
        got = map[candidate][0]
        print("\n", NAMES[candidate], "\t\t", got, end = "" )

        #If there's a clear winner, show it and keep track
        if got > goal:
            winner = candidate
            print("*", end = "")

        #Keeping track of loser
        if loser[1] == -1:
            loser = [candidate, got]
        elif loser[1] > got:
            loser = [candidate, got]

    #Show conclusions and return
    print("\n---------------------------\n")
    if winner > -1:
        print("The winner is: ", NAMES[winner])
    else:
        print("No candidate won in this round")
        print("Eliminating ", NAMES[loser[0]])

    return winner, loser

def count(ballot, options):
    #Showing field of play
    voters = len(ballot)
    goal = ( voters / 2 )

    print("Voters: {}\nGoal: {}".format(voters, goal))
    print("")

    map = {} # [ votes, [ [2º], [3º], ..., [nº] ] ]

    # Getting first voters
    for vote in ballot:
        first = vote.index(1)
        if first in map:
            lists = map[first]
            lists[0] = lists[0] + 1
            map[first] = lists
        else:
            map[first] = mapStarter(options)

    win, loser = preliminary(map, options, goal)

    if win > -1:
        return

    noWinner = True

    counter = 0

    while noWinner:
        #Eliminate loser
        counter = counter + 1
        return

        pass

if __name__ == '__main__':
    count(ballot, 3)
