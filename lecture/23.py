# Lists

def lists():
    """List mutation.

    >>> t = [1, 2, 3]
    >>> t[1:3] = [t]
    >>> t.extend(t)
    >>> t
    [1, [...], 1, [...]]

    >>> t = [[1, 2], [3, 4]]
    >>> t[0].append(t[1:2])
    >>> t
    [[1, 2, [[3, 4]]], [3, 4]]
    """

# Work

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

def work():
    """Working.

    >>> Worker().work()
    'Sir, I work'
    >>> jack
    Peon
    >>> jack.work()
    'Maam, I work'
    >>> john.work()
    Peon, I work
    'My job is to gather wealth'
    >>> john.elf.work(john)
    'Peon, I work'
    """

# Cycles

def cycle_demo():
    """A linked list can contain cycles.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first = 5
    >>> t = s.rest
    >>> t.rest = s
    >>> s.first
    5
    >>> s.rest.rest.rest.rest.rest.first
    2
    """

