# -*- coding:utf-8 -*-

'''
snooper 是一种新的python debug工具，采用装饰器的方式，将函数运行过程以日志输出到文件或终端；
    使用方法参考下面示例，snoop()主要包含四个参数：output、variable(python 2.7中，该参数为watch)、depth、prefix，分别为输出日志文件、打印全局变量、调用函数打印、日志记录时的前缀；
    缺陷：递归调用支持不佳；文件不能区分；跨文件函数调用，不能记录函数文件名；
    
ref： https://github.com/cool-RR/PySnooper
'''

import pysnooper

# basic usage:
@pysnooper.snoop()
def number_to_bits(number):
    if number:
        bits = []
        while number:
            number, remainder = divmod(number,2)
            bits.insert(0,remainder)
        return bits
    else:
        return [0]

number_to_bits(6)

# write debug info to the given log_file by using: output =./log/debug.log'
# debug info add prefix by using: prefix = 'add '
# add middle debug info by using: depth = 2
def add(num1,num2):
    return num1,num2

@pysnooper.snoop('./log/debug.log',prefix = 'add ', depth=2)
def multiplication(num1,num2):
    sum_value = 0
    for i in range(0,num1):
        sum_value = add(sum_value,num2)
    return sum_value

value = multiplication(3,4)


# debug the global info by using: variable = ("self.num1","self.num2")
class Foo(object):
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.sum_v = 0

    def add(self,num1,num2):
        return num1 + num2

    # python 3  : @pysnooper.snoop(output="./log/debug1.log"),variables=("self.num1","self.num2","self.sum_v"))
    # python 2.7: @pysnooper.snoop(output="./log/debug.log",watch=("self.num1","self.num2","self.sum_v"))
    @pysnooper.snoop(output="./log/debug.log",watch=("self.num1","self.num2","self.sum_v"))
    def multiplication(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        sum_v = 0
        for i in range(0,num1):
            sum_v = self.add(sum_v,num2)
        self.sum_v = sum_v
        return sum_v

if __name__ == "__main__":
    foo = Foo()
    foo.multiplication(3,4)
