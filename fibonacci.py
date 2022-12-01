N = 100000


def primitive_fib():
    a, b = 0, 1
    s = 0
    for _ in range(N-1):
        a, b = b, a+b
        s += a
    return s


class Fibo:
    def __init__(self, n: int):
        self.index = 0
        self.prev = 0
        self.current = 1
        self.limit = n - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.limit:
            self.prev, self.current = self.current, self.prev + self.current
            self.index += 1
            return self.prev
        raise StopIteration


def fib_iter():
    return sum(Fibo(N))


def fib_gen():
    def inner():
        prev, current = 0, 1
        for _ in range(N-1):
            prev, current = current, current + prev
            yield prev
    return sum(inner())


primitive_fib()
fib_iter()
fib_gen()
