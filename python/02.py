#!/usr/bin/env python
#coding=utf-8
#Auther: zhuqian091

import math

def quadratic(a, b, c):
    _sqrt = (b ** 2) - (4 * a * c)
    x1 = (- b + math.sqrt(_sqrt)) / 2 / a
    x2 = (- b - math.sqrt(_sqrt)) / 2 / a
    return x1, x2

if __name__ == '__main__':
   print('quadratic(2, 3, 1) = {}'.format(quadratic(2, 3, 'zhuqian')))

