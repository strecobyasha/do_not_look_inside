import itertools


def active1():
    x = itertools.count(start=2, step=3)
    print(next(x))  # 2
    print(next(x))  # 5
    print(next(x))  # 8


def active2():
    iterable = [2, 4, 3]
    x = itertools.cycle(iterable)
    print(next(x))  # 2
    print(next(x))  # 4
    print(next(x))  # 3
    print(next(x))  # 2
    print(next(x))  # 4
    b = (12, 34, 22)
    x = itertools.cycle(b)
    print(next(x))  # 12
    print(next(x))  # 34
    c = {2, 4, 2, 6, 2, 3, 2, 7}
    print(c)  # {2, 3, 4, 6, 7}
    x = itertools.cycle(c)
    print(next(x))  # 2
    print(next(x))  # 3
    print(next(x))  # 4
    d = {'a': 12, 'b': 54, 'c': 21}
    x = itertools.cycle(d)
    print(next(x))  # a
    print(next(x))  # b
    print(next(x))  # c
    print(next(x))  # a


def active3():
    elem = 5
    x = itertools.repeat(elem, 2)
    print(next(x))  # 5
    print(next(x))  # 5
    print(next(x))  # StopIteration


def active4():
    iterable = [1, 3, 8]
    x = itertools.accumulate(iterable)
    print(next(x))  # 1
    print(next(x))  # 4
    print(next(x))  # 12
    print(next(x))  # StopIteration


def active5():
    iterA = [3, 8]
    iterB = [2, 12]
    iterC = [9, 4]
    x = itertools.chain(iterA, iterB, iterC)
    print(next(x))  # 3
    print(next(x))  # 8
    print(next(x))  # 2
    print(next(x))  # 12


def active6():
    iterable = [2, 3, 7, 9]
    x = itertools.combinations(iterable, 3)
    print(next(x))  # (2, 3, 7)
    print(next(x))  # (2, 3, 9)
    print(next(x))  # (2, 7, 9)
    print(next(x))  # (3, 7, 9)
    print(next(x))  # StopIteration


def active7():
    iterable = [2, 3, 7, 9]
    x = itertools.combinations_with_replacement(iterable, 3)
    print(next(x))  # (2, 2, 2)
    print(next(x))  # (2, 2, 3)
    print(next(x))  # (2, 2, 7)
    print(next(x))  # (2, 2, 9)
    print(next(x))  # (2, 3, 3)


def active8():
    data = [12, 23, 7, 9]
    selectors = [1, 2, 3]
    x = itertools.compress(data, selectors)
    print(next(x))
    print(next(x))
    print(next(x))


def active9():
    iterA = [3, 8]
    iterB = [2, 12]
    iterC = [9, 4]
    x = itertools.product(iterA, iterB, iterC, repeat=1)
    print(next(x))  # (3, 2, 9)
    print(next(x))  # (3, 2, 4)
    print(next(x))  # (3, 12, 9)


def func(*args):
    return sum(args)


def active10():
    iterA = [3, 8]
    iterB = [2, 12]
    iterC = [9, 4]
    iterable = [iterA, iterB, iterC]
    x = itertools.starmap(func, iterable)
    print(next(x))  # 11
    print(next(x))  # 14
    print(next(x))  # 13


def active11():
    iterable = [2, 9, 7, 11, 5]
    x = itertools.tee(iterable, 3)
    for i in x:
        print(next(i))  # 2
        print(next(i))  # 9
        print(next(i))  # 7
        print(next(i))  # 11


def active():
    iterable = [2, 9, 7, 11, 5]
    x = itertools.permutations(iterable)
    print(next(x))  # (2, 9, 7, 11, 5)
    print(next(x))  # (2, 9, 7, 5, 11)
    print(next(x))  # (2, 9, 11, 7, 5)
