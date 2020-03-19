"""(Місcіонери на лівому березі, каннібали на лівому березі, лодка: 0 - біля правого берега, 1 - біля лівого берега)"""
INIT_STATE = (3, 3, 1)
GOAL_STATE = (0, 0, 0)

from state import State

class Action:
    def __init__(self):
        self.init_state = State.value_of_state(INIT_STATE)
        self.goal_state = State.value_of_state(GOAL_STATE)

    """Можливі варіанти пасажирів лодки і її розміщення"""
    def get_actions(self):
        return {
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1),
            (1, 0, 0),
            (2, 0, 0),
            (0, 1, 0),
            (0, 2, 0),
            (1, 1, 0)
        }

    """Чи досягнено ціль"""
    def is_goal_state(self, state):
        return state == self.goal_state