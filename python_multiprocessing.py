# -*- coding:utf-8 -*-

import multiprocessing
import time
from multiprocessing import Pool
import os
import random

def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print int(time.time())
    print "end worker_1"

def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print int(time.time())
    print "end worker_2"

def worker_3(interval):
    print "worker_3"
    time.sleep(interval)
    print int(time.time())
    print "end worker_3"

def multi_processing_test():
    p1 = multiprocessing.Process(target = worker_1, args = (5,))
    p2 = multiprocessing.Process(target = worker_2, args = (10,))
    p3 = multiprocessing.Process(target = worker_3, args = (15,))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"
 
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
 
def multi_processing_pool_test():
    print 'Parent process %s.' % os.getpid()
    p = Pool(4)   
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

if __name__ == '__main__':
    multi_processing_test()
    '''
    output:
    The number of CPU is:56
    child   p.name:Process-1	p.id46198
    child   p.name:Process-2	p.id46199
    child   p.name:Process-3	p.id46200
    END!!!!!!!!!!!!!!!!!
    worker_1
    worker_2
    worker_3
    1558519403
    end worker_1
    1558519408
    end worker_2
    1558519413
    end worker_3
    '''
    time.sleep(20)
    multi_processing_pool_test()
    '''
    output:
    Parent process 46197.
    Waiting for all subprocesses done...
    Run task 0 (46569)...
    Run task 1 (46570)...
    Run task 2 (46571)...
    Run task 3 (46572)...
    Task 1 runs 2.23 seconds.
    Run task 4 (46570)...
    Task 3 runs 2.30 seconds.
    Task 0 runs 2.91 seconds.
    Task 2 runs 2.95 seconds.
    Task 4 runs 2.42 seconds.
    All subprocesses done.
    ''' 
