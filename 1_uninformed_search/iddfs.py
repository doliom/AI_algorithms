import sys

def iddfs(init_state, goal_state):
    for depth in range(sys.maxsize):
        result = dls(init_state, goal_state, depth)
        if result:
            return result
    return None


def dls(node, goal_state, limit):
    if node == goal_state:
        return [node]
    elif node.fail():
        return None
    elif limit > 0:
        for child in node.expand_boat():
            result = dls(child, goal_state, limit - 1)
            if result:
                result.append(node)
                return result
        return None
    else:
        return None