import sys

def iddfs(init_state, goal_state):
    for depth in range(sys.maxsize):
        result, expanded = dls(init_state, goal_state, depth)
        if result:
            return result, expanded
    return None


def dls(node, goal_state, depth):
    expanded = 0
    if node == goal_state:
        return [node], expanded
    elif node.fail():
        return None, expanded
    elif depth > 0:
        expanded += 1
        for child in node.expand_boat():
            result, exp = dls(child, goal_state, depth - 1)
            expanded += exp
            if result:
                result.append(node)
                return result, expanded
        return None, expanded
    else:
        return None, expanded