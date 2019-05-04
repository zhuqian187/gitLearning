#!/usr/bin/env python
#coding=utf-8
#Auther: zhuqian091

def fib(n):
    a, b = 1, 1
    _list = [a, b]
    while b < n:
        a, b = b, a + b
        _list.append(b)
    return _list

if __name__ == '__main__':
    print(fib(25))