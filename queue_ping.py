import multiprocessing as mp

from multiprocessing import Process
from multiprocessing.queues import Queue
from time import sleep


def producer(queue: Queue):
    while True:
        message = 'ping'
        queue.put(message)
        sleep(1)


def consumer(queue: Queue):
    while message := queue.get():
        print(message)


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    queue = Queue(ctx=ctx)
    producer_ = Process(target=producer, args=(queue,))
    consumer_ = Process(target=consumer, args=(queue,))
    producer_.start()
    consumer_.start()
    producer_.join()
    consumer_.join()
