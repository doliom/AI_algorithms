from a_star_search import Astar_search
from node import Node

def showResult(solution):
    pathList = []
    state = solution
    print("init state")
    while state:
        pathList.append(state)
        state = state.parent
    pathList.reverse()
    for i in range(len(pathList)):
        print(pathList[i])
    print("goal state")

def main():
    init_state = Node(0, 0)
    goal_state = Node(3, 0)
    solution = Astar_search(init_state, goal_state)
    showResult(solution)

if __name__ == "__main__":
    main()