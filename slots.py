# -*- coding:utf-8 -*-

class Base:
    __slots__ = 'foo', 'bar'

class Right(Base):
    __slots__ = 'baz','baz1','baz2' 

class Wrong(Base):
    __slots__ = 'foo', 'bar', 'baz','baz1','baz2'   

from sys import getsizeof
print getsizeof(Right()),getsizeof(Wrong())

# output:
# 64 80
'''
__slots__：
    特殊属性，显式声明对象示例具有哪些属性；
    使用集合存储值引用，而不是__dict__
    sys.getsizeof()可以查看对象空间；
'''
