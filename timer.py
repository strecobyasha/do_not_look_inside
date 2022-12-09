import functools
import time


class Timer:

    def __init__(self, name: str = '', repeat: int = 1):
        self._start_time = None
        self.name = name
        self.repeat = repeat

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            with self:
                result = None
                for _ in range(self.repeat):
                    result = func(*args, **kwargs)
                return result

        return wrapper_timer

    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f'{self.name.ljust(15)}-> {elapsed_time}')
        return elapsed_time

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
