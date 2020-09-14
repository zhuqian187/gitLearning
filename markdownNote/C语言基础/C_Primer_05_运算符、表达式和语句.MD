# 第5章 运算符、表达式和语句
---

## 5.5 类型转换
基本转换规则：
1. 当类型转换出现在表达式时，无论时unsinged还是signed的char和short都会被自动转换成int，如有必要会被转换成unsigned int（比如short与int的大小相同，unsigned short就比int大。
2. 涉及两种类型的运算，两个值会被分别转换成两种类型更高的级别。
3. 类型的级别葱高至低是： long double > double > float > unsigned long long > long long > unsigned long > long > unsigned int > int。例外的情况是，当long和int的大小类型相同时，unsigned int比long的级别高。之所以short和char类型没有列出，因为他们已经被升级到 int 或者 unsigned int。
4. 当赋值表达式语句中，计算的最终结果会被转换成被赋值变量的类型。
5. 当作为函数参数传递时，char 和 short 被转换成 int， float 被转换成 double。