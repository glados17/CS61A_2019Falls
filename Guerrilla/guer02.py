def tree(label, branches = []):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def label(tree):
    return tree[0]

def branches(tree):
    if is_leaf(tree):
        return []
    else:
        return tree[1:]

def is_leaf(tree):
    return len(tree) == 1


# A min-heap is a tree with the special property that every nodes value is less than
# or equal to the values of all of its children. 

def is_min_heap(t):
    if is_leaf(t):
        return True
    else:
        return all([label(t) <= label(b) for b in branches(t)] + [is_min_heap(b) for b in branches(t)])

# Write a function largest product path that finds the largest product path possible.
#  A product path is defined as the product of all nodes between the root
# and a leaf. The function takes a tree as its parameter. Assume all nodes have a
# non-negative value.

def largest_product_path(tree):
    if is_leaf(tree):
        return label(tree)
    else:
        return label(tree) * max([largest_product_path(b) for b in branches(tree)])

# Below is the function contains, which takes in an input of a tree, t and a value,
# e. The function returns true if e exists as a label inside t

def contains(t, e):
    if is_leaf(t):
        return label(t) == e
    elif e == label(t):
        return True
    else:
        return any([contains(b, e) for b in branches(t)])

# Implement a function max tree, which takes a tree t. It returns a new tree with
# the exact same structure as t; at each node in the new tree, the entry is the largest
# number that is contained in that node’s subtrees or the corresponding node in t.

def max_tree(t):
    if is_leaf(t):
        return tree(label(t))
    else:
        new_branches = [max_tree(b) for b in branches(t)]
        new_label = max([label(max_tree(b)) for b in branches(t)] + [label(t)])
        return tree(new_label,new_branches)

# Challenge Question: The level-order traversal of a tree is defined as visiting the
# nodes in each level of a tree before moving onto the nodes in the next level. For
# example, the level order of the following tree is: 3 7 8 4

def height(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])


# solution from https://guohangma.herokuapp.com/2018/10/09/cs61a-guerrilla03/
# the idea of define the next level with no branches as [] is great

def level_order(tree):
    def find_next(current_level):
        if current_level == []:
            return []
        else:
            next_level = []
            for b in current_level:
                next_level.extend(branches(b))
            return [label(t) for t in next_level] + find_next(next_level)
    return [label(tree)] + find_next([tree])

# 6 Challenge Question: Write a function all paths which will return a list of lists of
# all the possible paths of an input tree, t. When the function is called on the same
# tree as the problem above, the function would return: [[3, 7], [3, 8], [3, 4]]

# Obveriously not a clear solution
def all_paths(t):
    if is_leaf(t):
        return [label(t)]
    else:
        result = []
        for b in branches(t):
            for paths in all_paths(b):
                if type(paths) != list:
                    paths = [paths]
                result.append([label(t)]+ paths)
        return result
        # return [[label(t)]+ path for path in all_paths(b) for b in branches(t)]

# Write make max finder, which takes in no arguments but returns a function which
# takes in a list. The function it returns should return the maximum value it’s been
# called on so far, including the current list and any previous list. You can assume
# that any list this function takes in will be nonempty and contain only non-negative
# values.

def make_max_finder():
    max_n = float('-inf')
    def max_finder(lst):
        nonlocal max_n
        for x in lst:
            if x > max_n:
                max_n = x
        return max_n
    return max_finder

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label 
        for branch in branches: 
            assert isinstance(branch, Tree) 
        self.branches = list(branches) 
            
    def __repr__(self): 
        if self.branches: 
            branches_str = ', ' + repr(self.branches) 
        else: 
            branches_str = '' 
        return 'Tree({0}{1})'.format(self.label, branches_str) 
    def is_leaf(self): # a leaf has no branches 
        return len(self.branches) == 0

    # def height(self):
    #     if self.is_leaf:
    #         return 0
    #     else:
    #         return 1 + max([b.height() for b in self.branches])

# Define filter tree, which takes in a tree t and one argument predicate function fn.
# It should mutate the tree by removing all branches of any node where calling fn on
# its label returns False. In addition, if this node is not the root of the tree, it should
# remove that node from the tree as well.


# learned from the solution of https://guohangma.herokuapp.com/2018/10/29/cs61a-guerrilla04/
# but his solution is with bug because you have to copy then change a list in a 
def filter_tree(t, fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6, [Tree(7)])])
    >>> filter_tree(t, lambda x: x % 2 != 0)
    >>> t
    tree(1, [Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x != 2)
    >>> t2
    Tree(2)
    """
    if not fn(t.label) and not t.is_leaf():
        t.branches = []
    else:
        t_branches_copy = t.branches[:]
        for b in t_branches_copy:
            if not fn(b.label):
                t.branches.remove(b)
                print(b.label)
            else:
                filter_tree(b, fn)

#  Fill in the definition for nth level tree map, which also takes in a function and a
# tree, but mutates the tree by applying the function to every nth level in the tree,
# where the root is the 0th level.

# borrowed some idea form the level_order,seem it is a good wway to deal with the problems
# on the level of trees
def nth_level_tree_map(fn, tree, n):
    """Mutates a tree by mapping a function all the elements of a tree.
    >>> tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]),
    Tree(2, [Tree(6), Tree(4)])])
    >>> nth_level_tree_map(lambda x: x + 1, tree, 2)
    >>> tree
    Tree(2, [Tree(7, [Tree(4), Tree(5), Tree(6)]),
    Tree(2, [Tree(7), Tree(5)])])
    """
    def find_next(current_level, level = 0):
        next_level = []
        for b in current_level:
            next_level.extend(b.branches)
            if level % n == 0:
                b.label = fn(b.label)
        if next_level != []:
            find_next(next_level, level + 1)  

    find_next([tree],0)  


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# The Link class can represent lists with cycles. That is, a list may contain itself as a
# sublist. Implement has cycle that returns whether its argument, a Link instance,
# contains a cycle. There are two ways to do this: iteratively with two pointers, or
# keeping track of Link objects we’ve seen already. Try to come up with both!

def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """
    key = link
    while(link):
        if link.rest is not Link.empty and link.rest is key:
            return True
        link = link.rest
    return False

# Fill in the following function, which checks to see if sub link, a particular sequence
# of items in one linked list, can be found in another linked list (the items have to be
# in order, but not necessarily consecutive).
def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    while(link):
        if link.first == sub_link.first:
            if sub_link.rest:
                sub_link = sub_link.rest
            else:
                return True
        link = link.rest
    return False

# They can’t stop all of us!!! Write a function generate constant which, a generator
# function that repeatedly yields the same value forever.
def generate_constant(x):
    """A generator function that repeats the same value x forever.
    >>> area = generate_constant(51)
    >>> next(area)
    51
    >>> next(area)
    51
    >>> sum([next(area) for _ in range(100)])
    5100
    """
    while True:
        yield x


# Now implement black hole , a generator that yields items in seq until one of
# them matches trap, in which case that value should be repeated yielded forever.
# You may assume that generate constant works. You may not index into or slice
# seq.
def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in which case that
    value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    trapped = 0
    for i in seq:
        if i == trap:
            trapped = 1
            break
        else:
            yield i
    if trapped:
        while True:
            yield trap
            

# Write a generator function gen inf that returns a generator which yields all the
# numbers in the provided list one by one in an infinite loop.

def gen_inf(lst):
    """
    >>> t = gen_inf([3, 4, 5])
    >>> next(t)
    3
    >>> next(t)
    4
    >>> next(t)
    5
    >>> next(t)
    3
    >>> next(t)
    4
    """
    while True:
        for x in lst:
            yield x


# Implement a generator function called filter(iterable, fn) that only yields elements of iterable for which fn returns True.
def naturals():
    i = 1
    while True:
        yield i
        i += 1
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))
    [0 , 2 , 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for x in iterable:
        if fn(x):
            yield x


# Define tree sequence, a generator that iterates through a tree by first yielding the
# root value and then yielding the values from each branch.
def tree_sequence(t):
    """
    >>> t = tree(1, [tree(2, [tree(5)]), tree(3, [tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    yield label(t)
    if not is_leaf(t):
        for b in branches(t):
            for value in tree_sequence(b):
                yield value
            

#  Write a function make digit getter that, given a positive integer n, returns a
# new function that returns the digits in the integer one by one, starting from the
# rightmost digit.
# Once all digits have been removed, subsequent calls to the function should return
# the sum of all the digits in the original integer.

# tried to use a generator for hours but it turns out to be simply can be solved
#  by using nonlocal, maybe it is really worth to think about which to use.
def make_digit_getter(n):
    """ Returns a function that returns the next digit in n
    each time it is called, and the total value of all the integers
    once all the digits have been returned.
    >>> year = 8102
    >>> get_year_digit = make_digit_getter(year)
    >>> for _ in range(4):
    ... print(get_year_digit())
    2
    0
    1
    8
    >>> get_year_digit()
    11
    """
    sum_n = 0
    def get_digit():
        nonlocal sum_n, n
        if n:
            result = n % 10
            sum_n += n % 10
            n = n // 10
            return result
        return sum_n
    return get_digit