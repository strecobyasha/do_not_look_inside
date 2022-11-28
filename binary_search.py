from functools import wraps
import random
import time

N = 10**4
REPEAT = 100
data = [i for i in range(1, N+1)]
x = [1, N//2, N]


def timer(name: str, repeat: int = REPEAT):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            for _ in range(repeat):
                func(*args, **kwargs)
            print(f'{name.ljust(20)} >>> {time.perf_counter()-start}')
            return
        return wrapper
    return inner


@timer(name='random')
def random_search():
    for item in x:
        y = 0
        while y != item:
            y = data[random.randrange(0, N)]


@timer(name='linear')
def linear_search():
    for item in x:
        position = 0
        y = data[position]
        while y != item:
            position += 1
            y = data[position]


@timer(name='linear_2')
def linear_search_2():
    for item in x:
        for index, value in enumerate(data):
            if value == item:
                break


@timer(name='list index')
def lst_index():
    for item in x:
        data.index(item)


@timer(name='dictionary get')
def dict_get():
    hash_tab = {item: index for index, item in enumerate(data)}
    for item in x:
        hash_tab.get(item)


@timer(name='iterative')
def iterative():
    for item in x:
        left, right = 0, N-1
        while left <= right:
            middle = (left + right) // 2
            if data[middle] == item:
                break
            if data[middle] < item:
                left = middle + 1
            else:
                right = middle - 1


@timer(name='recursive')
def recursive():
    def contains(value, left, right):
        if left <= right:
            middle = (left + right) // 2
            if data[middle] == value:
                return True
            if data[middle] < value:
                return contains(value, middle+1, right)
            elif data[middle] > value:
                return contains(value, left, middle-1)
        return False

    for item in x:
        contains(item, 0, N-1)


random_search()
linear_search()
linear_search_2()
lst_index()
dict_get()
iterative()
recursive()
