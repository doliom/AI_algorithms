from heapq import heappush, heappushpop

CONST_K = 3

def local_beam_search(init_state):
    successors = []
    visited = []

    for i in range(CONST_K): # формуємо k початкових станів
        currentState = init_state
        successors.append((init_state.makeValue(), currentState))

    depth = 0 # глибина (номер ітерації)

    while successors:
        nextSuccessors = []
        for val, node in successors:
            neighbours = node.expand_boat()

            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.append(neighbour)
                    value = neighbour.makeValue()

                    if value is 0 :
                        print("depth: %d" % depth)
                        return neighbour

                    if len(nextSuccessors) < CONST_K:
                        heappush(nextSuccessors, (value, neighbour))

                    else:
                        val, node = heappushpop(nextSuccessors, (value, neighbour))
                        visited.remove(node)

        print("__________________________________")
        print(nextSuccessors)
        print("__________________________________")

        successors = nextSuccessors
        depth += 1
    return currentState