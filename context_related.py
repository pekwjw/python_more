# -*- coding:utf-8 -*-
class ContextManager_basic(object):
    def __init__(self):
        print '__init__()'
    def __enter__(self):
        print '__enter__()'
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print "__exit__()"

with ContextManager_basic():
    print "OK, we can do something here~~"

# output:
# __init__()
# __enter__()
# OK, we can do something here~~
# __exit__()

# return to as object

class InnerContext(object):
    def __init__(self,obj):
        print "InnerContext.__init__(%s)" % obj

    def do_something(self):
        print "InnerContext.do_something()"

    def __del__(self):
        print "InnerContext.__del__()"

class ContextManager(object):
    def __init__(self):
        print "ContextManager.__init__()"

    def __enter__(self):
        print "ContextManager.__enter__()"
        return InnerContext(self)

    def __exit__(self,exc_type,exc_val,exc_tb):
        print "ContextManager.__exit__(), %s, %s, %s" % (exc_type,exc_val,exc_tb)

with ContextManager() as obj:
    obj.do_something()
    print "this is do_something."

'''
output:
ContextManager.__init__()
ContextManager.__enter__()
InnerContext.__init__(<__main__.ContextManager object at 0x10b5e2450>)
InnerContext.do_something()
this is do_something.
ContextManager.__exit__(), None, None, None
InnerContext.__del__()
'''
