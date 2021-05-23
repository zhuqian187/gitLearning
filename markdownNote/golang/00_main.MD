
## Go基础
### Golang内置类型与函数
#### 内置函数
```plain
    append          -- 用来追加元素到数组、slice中,返回修改后的数组、slice
    close           -- 主要用来关闭channel
    delete            -- 从map中删除key对应的value
    panic            -- 停止常规的goroutine  （panic和recover：用来做错误处理）
    recover         -- 允许程序定义goroutine的panic动作
    real            -- 返回complex的实部   （complex、real imag：用于创建和操作复数）
    imag            -- 返回complex的虚部
    make            -- 用来分配内存，返回Type本身(只能应用于slice, map, channel)
    new                -- 用来分配内存，主要用来分配值类型，比如int、struct。返回指向Type的指针
    cap                -- capacity是容量的意思，用于返回某个类型的最大容量（只能用于切片和 map）
    copy            -- 用于复制和连接slice，返回复制的数目
    len                -- 来求长度，比如string、array、slice、map、channel ，返回长度
    print、println     -- 底层打印函数，在部署环境中建议使用 fmt 包
```
#### 内置接口error
```golang
    type error interface { //只要实现了Error()函数，返回值为String的都实现了err接口

            Error()    String

    }
```

### 运算符
##### 逻辑运算符
运算符 ｜ 描述
--- ｜ ---
`&&` ｜ 逻辑AND运算符。如果两边操作数都是True，则为True，否则为False
`||` ｜ 逻辑OR运算符。如果两边操作数有一个为True，则为True，否则为False
`!`  | 逻辑NOT运算符，如果条件为True，则为False，否则为True

##### 位运算符
运算符 ｜ 描述
--- ｜ ---
`&` | 参与运算的两数各对应的二进位相与。（两位均为1才为1）
`|` | 参与运算的两数各对应的二进位相或。（两位有一个为1就为1）
`^` | 参与运算的两数各对应的二进位相异或，当两对应的二进位相异时，结果为1。（两位不一样则为1）
`<<` | 左移n位就是乘以2的n次方。“a<<b”是把a的各二进位全部左移b位，高位丢弃，低位补0。
`>>` | 右移n位就是除以2的n次方。“a>>b”是把a的各二进位全部右移b位。

### 变量与常量
#### 变量
##### 变量声明
变量需要声明后才能使用，在同一个作用域中，不支持变量的重复声明。实际上是不支持没有新声明的变量作用在声明缓环节。
```
var 变量名 变量类型
```

##### 变量的初始化
```
var 变量名 类型 = 表达式 // 标准格式
变量名1, ... := 表达式1, ... // 多个变量的一次声明，短声明格式
var name = "pprof.cn" // 类型推到，编译器更具等号右边的值来推导变量的类型初始化
_, _ := 表达式1， 表达式2
```
