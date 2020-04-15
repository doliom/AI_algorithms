from heapq import heappush, heappushpop

CONST_K = 3

def local_beam_search(init_state):
    currentStates = [] #список для k станів, що розглядаються одночасно за 1 ітерацію
    visited = [] #список пройдених станів

    for i in range(CONST_K): # формуємо k початкових станів
        startState = init_state
        currentStates.append(startState)

    depth = 0 # глибина (номер ітерації)

    while currentStates:
        nextStates = []
        print(depth)
        for node in currentStates:
            neighbours = node.expand_boat() #формуємо всіх можливих нащадків (список)
            print_nodes(node, neighbours)

            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.append(neighbour)
                    value = neighbour.makeValue()

                    if value is 0:
                        print("finish depth: %d" % depth)
                        return neighbour

                    if len(nextStates) < CONST_K:
                        heappush(nextStates, neighbour) #додаємо в список (heap)
                    else:
                        node = heappushpop(nextStates, neighbour)
                        visited.remove(node)

        currentStates = nextStates
        depth += 1
        print("      ")
    return startState

def print_nodes(node, neighbours):
    print("CURRENT STATE")
    print(node)
    print("NEIGHBOURS")
    for i in range(len(neighbours)):
        print("-", i, "-")
        print(neighbours[i])