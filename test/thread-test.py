# -*- coding: utf-8 -*-

import time, thread, threading


# def print_time(threadName,delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#
# #创建两个线程
# try:
#     thread.start_new_thread(print_time,('lining',2,))
#     thread.start_new_thread(print_time, ('wangwei', 4,))
# except:
#     print  'Error: unable to start thread'
#
# while 1:
#     pass

# threadLock = threading.Lock()
# threads = []
#
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print '%s: %s' % (threadName, time.ctime(time.time()))
#         counter -= 1
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print 'Starting ' + self.name
#
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         threadLock.release()
#
# #创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
#
# threads.append(thread1)
# threads.append(thread2)
#
# for t in threads:
#     t.join()
#
# print "Exiting Main Thread"

# def test():
#     print 'test'
#
# class lnThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         test()
#
#
# t1 = lnThread()
#
# print '1'
# t1.start()
# t1.join()
# print '2'


# def test():
#     count = 0
#     while count < 5:
#         print 'test'
#         count += 1
#
# try:
#     thread.start_new_thread(test,())
# except:
#     print "Error: unable to start thread"
#
#
# time.sleep(0.001)
# print 'dddd'
#
#
# def run():
#     time.sleep(2)
#     print u'当前线程的名字是：'+ threading.current_thread().name
#     time.sleep(2)
#
# if __name__ == '__main__':
#     start_time = time.time()
#
#     print u'这是主线程：', threading.current_thread().name
#     thread_list = []
#     for i in xrange(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)
#
#     for r in thread_list:
#         r.setDaemon(True)
#         r.start()
#
#     for r in thread_list:
#         r.join()
#
#
#     print u'主线程结束！', threading.current_thread().name
#     print u'一共用时：', time.time() - start_time

import random


class Producer(threading.Thread):

    def __init__(self, integers, condition):
        super(Producer,self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            integer = random.randint(0, 1000)
            self.condition.acquire()  # 获取条件锁
            print('condition acquired by %s' % threading.current_thread().name)
            self.integers.append(integer)
            print('%d appended to list by %s' % (integer, threading.current_thread().name))
            print('condition notified by %s' % threading.current_thread().name)
            self.condition.notify()  # 唤醒消费者线程
            print('condition released by %s' % self.name)
            self.condition.release()  # 释放条件锁
            time.sleep(1)


class Consumer(threading.Thread):

    def __init__(self, integers, condition):
        super(Consumer,self).__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            self.condition.acquire()
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print('%d popped from list by %s' % (integer, self.name))
                    break
                print('condition wait by %s' % self.name)
                self.condition.wait()  #等待状态，等待被唤醒，才会继续执行

        self.condition.release()

if __name__ == '__main__':
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers,condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()