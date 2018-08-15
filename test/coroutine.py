#_*_ coding: UTF-8 _*_

import time


def myGe():
    r = 0
    while True:
        n = yield r
        print 'n', n
        if not n:
            return
        r = r + 1
        print 'r', r


ge = myGe()

print ge.next()
print ge.send(2)