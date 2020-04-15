import sys
from node import Node
from beam import local_beam_search

def main():
    start_state = Node(3, 3, 1, 0, 0, 0)
    #goal_state = Node(0, 0, 0, 3, 3, 1)

    try:
        solution = local_beam_search(start_state)
        # for i in range(len(solution)):
        #     print("depth: ", i)
        print(solution)
    except NotImplementedError:
        sys.exit('is not yet implemented' )

if __name__ == '__main__':
    main()