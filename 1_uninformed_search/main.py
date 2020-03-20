from state import State
import sys
from iddfs import iddfs

INITIAL = 'left'

def solve(start_state, goal_state, mode):
    solution = None
    expanded = -1
    if mode == 'iddfs':
        solution, expanded = iddfs(start_state, goal_state)
    else:
        raise ValueError('invalid mode: %s' % mode)
    if solution and mode != 'iddfs':
        solution_list = []
        current = solution
        while current:
            solution_list.append(current)
            current = current.previous
        solution_list.reverse()
        return solution_list, expanded
    else:
        return solution, expanded


def main():
    global INITIAL
    mode = 'iddfs'
    start_state = State(3, 3, 1, 0, 0, 0)
    goal_state = State(0, 0, 0, 3, 3, 1)

    if start_state.left_side > 0:
        INITIAL = 'left'
    else:
        INITIAL = 'right'
    print ('initial: %s' % INITIAL)

    try:
        solution, expanded = solve(start_state, goal_state, mode)
        for i in range(len(solution)):
            print("depth: ", i)
            print(solution[i])
    except NotImplementedError:
        sys.exit('%s is not yet implemented' % mode)

if __name__ == '__main__':
    main()