
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
#### 逻辑运算符
运算符 | 描述
--- | ---
`&&` | 逻辑AND运算符。如果两边操作数都是True，则为True，否则为False
`\|\|` | 逻辑OR运算符。如果两边操作数有一个为True，则为True，否则为False
`!`  | 逻辑NOT运算符，如果条件为True，则为False，否则为True

#### 位运算符
运算符 | 描述
--- | ---
`&` | 参与运算的两数各对应的二进位相与。（两位均为1才为1）
`\|` | 参与运算的两数各对应的二进位相或。（两位有一个为1就为1）
`^` | 参与运算的两数各对应的二进位相异或，当两对应的二进位相异时，结果为1。（两位不一样则为1）
`<<` | 左移n位就是乘以2的n次方。“a<<b”是把a的各二进位全部左移b位，高位丢弃，低位补0。
`>>` | 右移n位就是除以2的n次方。“a>>b”是把a的各二进位全部右移b位。

### 变量与常量
#### 变量声明
变量需要声明后才能使用，在同一个作用域中，不支持变量的重复声明。实际上是不支持没有新声明的变量作用在声明缓环节。
```
var 变量名 变量类型
```

#### 变量的初始化
```
var 变量名 类型 = 表达式 // 标准格式
变量名1, ... := 表达式1, ... // 多个变量的一次声明，短声明格式；注意，短声明格式不能用在函数之外
var name = "pprof.cn" // 类型推到，编译器更具等号右边的值来推导变量的类型初始化
_, _ := 表达式1， 表达式2 // 下划线意味可以丢弃的变量或者包
```

### 基本类型
#### Go基本类型系统
类型 | 长度（字节） | 默认值 | 说明
--- | --- | --- | ---
bool | 1 | false | 
byte | 1 | 0 | uint8
rune | 4 | 0 | Unicode Code Point， int32
int, uint | 4或者8 | 0 | 32位或者64位（取决于操作系统，GOOS）
uintptr | 4或者8 |   | 以存储指针的uint32或者uint64整数
arrary |   |   | 值类型
struct |   |   | 值类型
string |   | "" | UTF-8字符串
slice |   | nil | 引用类型
map |   | nil  | 引用类型
channel |   | nil | 引用类型
interface |   | nil | 接口
function |   | nil | 函数

#### 字符串
字符串的转义符
转义 | 含义
--- | ---
`\r` | 回车符（返回行首）
`\n` | 换行符（直接跳到下一行的同列位置）
`\t` | 制表符
`\'` | 单引号
`\"` | 双引号
`\`  | 反斜杠

多行字符串使用 `反引号` 字符
```Go
    s1 := `第一行
    第二行
    第三行
    `
    fmt.Println(s1)
```

字符串的常用操作，
方法 | 介绍
--- | ---
len(str) | 求长度
package strings | String基本库

#### 切片slice
slice的声明
```golang
全局声明与定义
var arr = [...]int{0, 1, 2, 3, 4} // 定义一个数组，arrary
var slice0 []int = arr[start:end] OR arr[start:] OR arr[:end] OR arr[:]

局部作用域声明与定义：
arr2 = [...]int{5, 6, 7, 8, 9}
slice1 = arr[start:end] OR arr[start:] OR arr[:end] OR arr[:]

通过make来创建切片
全局:
var slice []type = make([]type, len)
局部:
slice := make([]type, len) // cap = len
slice := make([]type, len, cap) // cap >= len
```

> 一个奇怪的slice  
> [][]T, 指元素类型为 []T 的 slice。可以为 slice, struct, map, channel 或者其他一些奇奇怪怪的对象

slice操作含义
操作 | 含义
--- | ---
s[n] | 切片s中索引位置为n的项
s[:] | 从切片s的索引 0 到 len(s)-1 处所获得的切片
s[low:] | 从切片s的索引 low 到 len(s)-1 处所获得的切片
s[:high] | 从切片s的索引 0 到 high 处所获得的切片, len = high
s[low:high] | 从切片s的索引 low 到 high 处所获得的切片, len = high - low
s[low:high:max] | 从切片s的索引 low 到 high 处所获得的切片, len = high - low , cap = max - low
len(s) | 切片s的长度，总是 <= cap(s)
cap(s) | 切片s的容量，总是 >= len(s)

slice的一些函数操作
关键字 | 一些说明
--- | ---
append | 追加写入，向 slice 尾部添加数据，返回新的 slice 对象
copy | 函数 copy 在两个 slice 间复制数据，复制长度以 len 小的为准，两个 slice 可指向同一底层数组，允许元素区间重叠。
range | 通过 range 遍历 slice。 index, value := range slice
\- | 调整 slice 的大小， 参考slice操作含义

#### slice 的底层实现
切片常见的操作有 reslice, append, copy。同时，切片还具有索引， 可迭代的优秀特性。

Go数组是值类型，每次传递参数，都会将数据拷贝一遍。所以，数组建议使用指针方式传递，避免拷贝。
[link](http://www.topgoer.com/go%E5%9F%BA%E7%A1%80/Slice%E5%BA%95%E5%B1%82%E5%AE%9E%E7%8E%B0.html)