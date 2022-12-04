import logging
import threading
import concurrent.futures
import time


class Pipeline:

    def __init__(self):
        self.lock_a = threading.Lock()
        self.lock_b = threading.Lock()
        self.lock_a.acquire()
        self.message = ''

    def add_a(self):
        self.lock_a.acquire()
        self.message += 'a'
        logging.info(self.message)
        time.sleep(1)
        logging.info('Release lock_b')
        self.lock_b.release()

    def add_b(self):
        self.lock_b.acquire()
        self.message += 'b'
        logging.info(self.message)
        time.sleep(1)
        logging.info('Release lock_a')
        self.lock_a.release()


def func_a(pipeline):
    for _ in range(3):
        time.sleep(3)
        pipeline.add_a()


def func_b(pipeline):
    for _ in range(3):
        time.sleep(1)
        pipeline.add_b()


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(func_a, pipeline)
        executor.submit(func_b, pipeline)
