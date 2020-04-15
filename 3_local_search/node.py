class Node:
    def __init__(self, maharajaLeft, pariLeft, boatLeft, maharajaRight, pariRight, boatRight, parent=None):
        self.maharajaLeft = maharajaLeft
        self.pariLeft = pariLeft
        self.boatLeft = boatLeft
        self.maharajaRight = maharajaRight
        self.pariRight = pariRight
        self.boatRight = boatRight
        self.parent = parent

# кількість осіб на лівому березі
    @property
    def left_side(self):
        return self.pariLeft + self.maharajaLeft

# кількість осіб на правому березі
    @property
    def right_side(self):
        return self.maharajaRight + self.pariRight

    def makeValue(self):
        if ((self.maharajaLeft > self.pariLeft and
                 self.pariLeft > 0) or
                (self.maharajaRight > self.pariRight and
                 self.pariRight > 0)):
            return -7
        else:
            return (self.maharajaLeft + self.pariLeft + self.boatLeft)*(-1)

    def expand_boat(self):
        if self.boatRight + self.boatLeft != 1:
            raise NotImplementedError('more than one boat')

        if self.boatRight:# якщо лодка біля правого берега
            move = self.move_left# то рухаємось від правого до лівого берега
            maharaja = self.maharajaRight
            pari = self.pariRight
        elif self.boatLeft:
            move = self.move_right
            maharaja = self.maharajaLeft
            pari = self.pariLeft

        # формування вершин станів
        states = []
        if pari > 0:
            states.append(move(pari=1))
        if pari > 1:
            states.append(move(pari=2))
        if maharaja > 0:
            states.append(move(maharaja=1))
        if maharaja > 0 and pari > 0:
            states.append(move(maharaja=1, pari=1))
        if maharaja > 1:
            states.append(move(maharaja=2))
        return states

# рух від правого берега до лівого
    def move_left(self, pari=0, maharaja=0):
        if pari + maharaja > 2 or pari + maharaja < 1: # максимум тільки 2 людини на лодці, та не можна перевозити порожню лодку
            raise RuntimeError('unfeasible transportation')

        return Node(
                self.maharajaLeft + maharaja,
                self.pariLeft + pari,
                self.boatLeft + 1,
                self.maharajaRight - maharaja,
                self.pariRight - pari,
                self.boatRight - 1,
                parent=self)

# рух від лівого берега до правого
    def move_right(self, pari=0, maharaja=0):
        if pari + maharaja > 2 or pari + maharaja < 1:
            raise RuntimeError('unfeasible transportation')

        return Node(
                self.maharajaLeft - maharaja,
                self.pariLeft - pari,
                self.boatLeft - 1,
                self.maharajaRight + maharaja,
                self.pariRight + pari,
                self.boatRight + 1,
                parent=self)

# для порівняння
    def __eq__(self, other):
        return (self.maharajaLeft == other.maharajaLeft and
                self.pariLeft == other.pariLeft and
                self.boatLeft == other.boatLeft and
                self.maharajaRight == other.maharajaRight and
                self.pariRight == other.pariRight and
                self.boatRight == other.boatRight)

# перетворюємо в строкове представлення
    def __str__(self):
        return '%d,%d,%d\n%d,%d,%d' % (
                self.maharajaLeft,
                self.pariLeft,
                self.boatLeft,
                self.maharajaRight,
                self.pariRight,
                self.boatRight)

# перевизначаєм операнд
    def __lt__(self, other):
        return self.makeValue() < other.makeValue()
