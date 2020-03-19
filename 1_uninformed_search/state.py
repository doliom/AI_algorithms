INIT_STATE = (3, 3, 1)
GOAL_STATE = (0, 0, 0)

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def value_of_state(self, state):
        return State(state[0], state[1], state[2])


    def not_equal(self): #on left and rigth side
        return ((self.missionaries == 1 and self.cannibals == 3) or
                (self.missionaries == 2 and self.cannibals == 3) or
                (self.missionaries == 1 and self.cannibals == 2) or
                (self.missionaries == 2 and self.cannibals == 1) or
                (self.missionaries == 3 and self.cannibals == 1) or
                (self.missionaries == 3 and self.cannibals == 2))

    def more_than_one_boat(self):
        return self.boat > 1

    def checked(self):
        if self.value_of_state():
            return False
        elif self.not_equal():
            return False
        else:
            return True