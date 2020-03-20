from state import State
import sys
from iddfs import iddfs

def main():
    start_state = State(3, 3, 1, 0, 0, 0)
    goal_state = State(0, 0, 0, 3, 3, 1)

    try:
        solution = iddfs(start_state, goal_state)
        for i in range(len(solution)):
            print("depth: ", i)
            print(solution[i])
    except NotImplementedError:
        sys.exit('is not yet implemented' )

if __name__ == '__main__':
    main()