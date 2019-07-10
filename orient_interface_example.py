# -*- coding:utf-8 -*-

'''
面向接口编程
各个容器类型实现的接口协议定义了容器；编写代码时，更应关注容器的抽象属性；而非容器本身；便于写出更优雅、扩展性更好的代码；
'''

def add_ell(comments, max_length = 12):
    for com in comments:
        com = com.strip()
        if len(com) > max_length:
            yield com[:max_length] + "..."
        else:
            yield com

# list
comments = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]
print "\n".join(add_ell(comments))

# tuple
co = tuple(comments)
print "\n".join(add_ell(co))

# file
with open("comments") as fp:
    for comment in add_ell(fp):
        print comment
