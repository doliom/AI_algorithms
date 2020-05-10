MAX_JUG_9 = 9
MAX_JUG_5 = 5

class Node:
    def __init__(self, jug9, jug5, parent=None):
        self.jug9 = jug9
        self.jug5 = jug5
        self.parent = parent
        self.g_score = 0
        self.f_score = 0
        self.h_score = abs(self.jug9 - 3)

# умови, які не повинні виконуватись
    def fail(self):
        return ((self.jug9 > 9) or
                (self.jug5 > 5))

    def makeStates(self):
        states = []

        if self.jug9 < MAX_JUG_9:
            states.append(self.fillJug9())
        if self.jug5 < MAX_JUG_5:
            states.append(self.fillJug5())
        if self.jug9 > 0:
            states.append(self.emptyJug9())
        if self.jug5 > 0:
            states.append(self.emptyJug5())
        if self.jug5 > 0 and self.jug9 + self.jug5 > 0 and self.jug5 + self.jug9 >= MAX_JUG_9:
            states.append(self.pourToFillJug9())
        if self.jug9 > 0 and self.jug9 + self.jug5 > 0 and self.jug5 + self.jug9 >= MAX_JUG_5:
            states.append(self.pourToFillJug5())
        if self.jug5 >= 0 and self.jug5 + self.jug9 > 0 and self.jug9 + self.jug5 <= MAX_JUG_9:
            states.append(self.pourToJug9())
        if self.jug9 >= 0 and self.jug9 + self.jug5 > 0 and self.jug5 + self.jug9 <= MAX_JUG_5:
            states.append(self.pourToJug5())

        return states

# наповнення 9ти літрового відра
    def fillJug9(self):
        return Node(
            MAX_JUG_9,
            self.jug5,
            parent=self
        )

# наповнення 5ти літрового відра
    def fillJug5(self):
        return Node(
            self.jug9,
            MAX_JUG_5,
            parent=self
        )

# виливання всієї води з 9ти літрового відра
    def emptyJug9(self):
        return Node(
            0,
            self.jug5,
            parent=self
        )

# виливанн всієї води з 5ти літрового відра
    def emptyJug5(self):
        return Node(
            self.jug9,
            0,
            parent=self
        )

# переливання з 5ти літрового в 9ти літрове відро, поки воно не буде повним
    def pourToFillJug9(self):
        return Node(
            MAX_JUG_9,
            self.jug5 - (MAX_JUG_9 - self.jug9),
            parent=self
        )

# переливання з 9ти літрового в 5ти літрове відро, поки воно не буде повним
    def pourToFillJug5(self):
        return Node(
            self.jug9 - (MAX_JUG_5 - self.jug5),
            MAX_JUG_5,
            parent=self
        )

# переливання з 5ти літрового в 9ти літрове відро
    def pourToJug9(self):
        return Node(
            self.jug9 + self.jug5,
            0,
            parent=self
        )

# переливання з 9ти літрового в 5ти літрове відро
    def pourToJug5(self):
        return Node(
            0,
            self.jug5 + self.jug9,
            parent=self
        )


    def __eq__(self, other):
       return (self.jug9 == other.jug9 and
               self.jug5 == other.jug5)

# перетворюємо в строкове представлення
    def __str__(self):
        return '%d,%d' % (
            self.jug9,
            self.jug5)
