# 第2章 C语言概述
---
## 2.4 提高程序的可读性技巧
1. 多写注释
2. 选择有意义的函数名火变量名

## 多个函数
```c
/* two_func.c -- 一个文件中包含两个函数 */

#include <stdio.h>

void butler(void);  // 原型函数，告知编译器在程序中要使用该函数

int main(void) {
    printf("I will summon the butler function.\n");
    butler();   // 函数调用
    printf("Yes. Bring me some tea and writable DVD.\n");
    return 0;
}

// 定义函数
void butler(void) {
    printf("You rang, sir?\n");
}
```
输出
> I will summon the butler function.
You rang, sir?
Yes. Bring me some tea and writable DVD

函数原型
> 函数原型是一种声明，告知编译器正在使用的某函数，因此，函数原型也被称为函数声明。
通常被调函数会向主调函数返回一个值.

> tips:
> 1. 无论main函数位于源代码中的什么位置，程序执行的入口都是从main函数开始的。按照惯例，C语言将main函数放在开头，提供程序的基本骨架。

## 第2章复习题
提问 | 回答
--- | ---
C语言的基本模块是什么？ | 函数是否也是C语言中的一等公民
什么是语法错误，写出一个英语例子与C语言错误？ | 未能按照C语言的语法范式编码
什么是语义错误 | 没有按照需要实现功能编码，未能实现设计功能
