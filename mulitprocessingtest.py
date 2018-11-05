# -*- coding: utf-8 -*-

import os
import random
import time
from multiprocessing import Process
from multiprocessing.pool import Pool


def fun(name):
    print('Run child process %s (%s), parent process is (%s)' % (name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=fun, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process ends.')

print('==========')


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocesses done.')

print('=================')








