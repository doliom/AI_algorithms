
class State(object):
    def __init__(self, cannibalsLeft, missionariesLeft, boatLeft, cannibalsRight, missionariesRight, boatRight, parent=None):
        self.cannibalsLeft = cannibalsLeft
        self.missionariesLeft = missionariesLeft
        self.boatLeft = boatLeft
        self.cannibalsRight = cannibalsRight
        self.missionariesRight = missionariesRight
        self.boatRight = boatRight
        self.parent = parent

# кількість осіб на лівому березі
    @property
    def left_side(self):
        return self.missionariesLeft + self.cannibalsLeft

# кількість осіб на правому березі
    @property
    def right_side(self):
        return self.missionariesRight + self.cannibalsRight

# умови, які не повинні виконуватись
    def fail(self):
        return ((self.cannibalsLeft > self.missionariesLeft and
                 self.missionariesLeft > 0) or
                (self.cannibalsRight > self.missionariesRight and
                 self.missionariesRight > 0))

    def expand_boat(self):
        if self.boatRight + self.boatLeft != 1:
            raise NotImplementedError('more than one boat')

        if self.boatRight: # якщо лодка біля правого берега
            move = self.move_left # то рухаємось від правого до лівого берега
            cannibals = self.cannibalsRight
            missionaries = self.missionariesRight
        elif self.boatLeft:
            move = self.move_right
            cannibals = self.cannibalsLeft
            missionaries = self.missionariesLeft

        # формування вершин станів
        states = []
        if missionaries > 0:
            states.append(move(missionaries=1))
        if missionaries > 1:
            states.append(move(missionaries=2))
        if cannibals > 0:
            states.append(move(cannibals=1))
        if cannibals > 0 and missionaries > 0:
            states.append(move(cannibals=1, missionaries=1))
        if cannibals > 1:
            states.append(move(cannibals=2))
        return states

# рух від правого берега до лівого
    def move_left(self, missionaries=0, cannibals=0):
        if missionaries + cannibals > 2 or missionaries + cannibals < 1: # максимум тільки 2 людини на лодці, та не можна перевозити порожню лодку
            raise RuntimeError('unfeasible transportation')

        return State(
                self.cannibalsLeft + cannibals,
                self.missionariesLeft + missionaries,
                self.boatLeft + 1,
                self.cannibalsRight - cannibals,
                self.missionariesRight - missionaries,
                self.boatRight - 1,
                parent=self)

# рух від лівого берега до правого
    def move_right(self, missionaries=0, cannibals=0):
        if missionaries + cannibals > 2 or missionaries + cannibals < 1:
            raise RuntimeError('unfeasible transportation')

        return State(
                self.cannibalsLeft - cannibals,
                self.missionariesLeft - missionaries,
                self.boatLeft - 1,
                self.cannibalsRight + cannibals,
                self.missionariesRight + missionaries,
                self.boatRight + 1,
                parent=self)

# для порівняння
    def __eq__(self, other):
        return (self.cannibalsLeft == other.cannibalsLeft and
                self.missionariesLeft == other.missionariesLeft and
                self.boatLeft == other.boatLeft and
                self.cannibalsRight == other.cannibalsRight and
                self.missionariesRight == other.missionariesRight and
                self.boatRight == other.boatRight)

# перетворюємо в строкове представлення
    def __str__(self):
        return '%d,%d,%d\n%d,%d,%d' % (
                self.missionariesLeft,
                self.cannibalsLeft,
                self.boatLeft,
                self.missionariesRight,
                self.cannibalsRight,
                self.boatRight)