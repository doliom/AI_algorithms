class Node:

    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def child_node(self, problem, action):
        """Отримати нащадка після дії (даної)."""
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action)