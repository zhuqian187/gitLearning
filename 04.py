#!/usr/bin/env python
#coding=utf-8
#Auther: zhuqian091

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]

if __name__ == '__main__':
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过！')
    else:
        print('测试失败！！！')