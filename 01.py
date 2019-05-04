#!/usr/bin/env python
#coding=utf-8
#Auther: zhuqian091

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

if __name__ == '__main__':
    a = move(100, 100, 60, math.pi / 6)
    print('a = {0}, type(a) = {1};'.format(a, type(a)))
    print(a.__repr__)