def Astar_search(init_state, goal_state):
    visitedNodes = [] #як буфер для вершин, що відвідали
    init_state.f_score = init_state.g_score + init_state.h_score #евристична функція
    path = [init_state]
    while path:
        currentNode = path[0]
        for node in path[1:]:
            if node.f_score < currentNode.f_score:
                currentNode = node

        path.remove(currentNode)
        visitedNodes.append(currentNode)

        if currentNode == goal_state:
            return node

        if currentNode.fail():
            continue

        for node in currentNode.makeStates():
            possibleG_score = currentNode.g_score + 1

            if node in visitedNodes:
                if possibleG_score >= node.g_score:
                    continue

            if node not in path or possibleG_score < node.g_score:
                node.g_score = possibleG_score
                node.f_score = node.g_score + node.h_score
                if node not in path:
                    path.append(node)
    return None

