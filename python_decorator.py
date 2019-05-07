# -*- coding:utf-8 -*-

from functools import wraps

# decorator class example:
class logit(object):
    def __init__(self,logfile = 'class_out.log'):
        self.logfile = logfile
    
    def __call__(self,func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__ + ' was called.'
            print log_string
            with open(self.logfile,'a') as opened_file:
                opened_file.write(log_string + '\n')
            self.notify()
            return func(*args,**kwargs)
        return wrapped_function
    
    def notify(self):
        print 'class father'
        pass

class email_logit(logit):
    def __init__(self,email = 'admin@admin.com',logfile = 'class_2_out.log',*args,**kwargs):
        self.email = 'admin@admin.com'
        super(email_logit,self).__init__(*args,**kwargs)
   
    def notify(self):
        print 'send to ' + self.email

@logit()
def myfunc1():
    pass

@email_logit()
def myfunc2():
    pass

myfunc1()
# output:
# myfunc1 was called.
# class father

myfunc2()
# output:
# myfunc2 was called.
# send to admin@admin.com


# decorator function example:
def logit_function(logfile = 'function_out.log'):
    def log_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string = func.__name__ + ' was called in function.'
            print log_string 
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args,**kwargs)
        return wrapped_function
    return log_decorator

@logit_function()
def myfunc3():
    pass

myfunc3()
# output:
# myfunc3 was called in function.

myfunc1()
# output:
# myfunc1 was called.
# class father

myfunc2()
# output:
# myfunc2 was called.
# send to admin@admin.com
