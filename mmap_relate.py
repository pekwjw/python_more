# -*- coding:utf-8 -*-

import mmap
import contextlib
import time
from optparse import OptionParser

maxnum = 1024*1024*100

def calc_time(func):
    def _decorator(*args,**kwargv):
        begin_time = time.time()
        func(*args,**kwargv)
        cost_time = time.time() - begin_time
        print "cost time: %s" % (cost_time)
    return _decorator

@calc_time
def replace_keyword_all(filename,oldword,newword):
    if len(oldword) == len(newword):
        loc = 0
        print " %s replace to %s " % (oldword,newword)
        with open(filename,'rb+') as fo:
            with contextlib.closing(mmap.mmap(fo.fileno(),0,access=mmap.ACCESS_WRITE)) as mo:
                print mo.size()
                while True:
                    loc_cur = mo.find(oldword,loc)
                    print loc_cur
                    if loc_cur >= 0:
                        mo[loc_cur:loc_cur+len(oldword)] = newword
                    elif loc_cur == -1:
                        break
                    else:
                        pass
    else:
        print "oldword length is not equal to newword length."
        exit()

@calc_time
def replace_keyword_once(filename,oldword,newword):
    if len(oldword) == len(newword) :
        print "%s replace to %s " % (oldword,newword)
        with open(filename,'rb+') as fo:
            with contextlib.closing(mmap.mmap(fo.fileno(),0,access=mmap.ACCESS_WRITE)) as mo:
                loc_cur = mo.find(oldword)
                if loc_cur >= 0:
                    mo[loc_cur:loc_cur+len(oldword)] = newword
    else:
        print "oldword length is not equal to newword length."
        exit()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f","--filename",help="Filename for search",dest="filename")
    parser.add_option("-o","--oldword",help="the ip to use",dest="oldword")
    parser.add_option("-n",'--newword',help="the ip to use",dest="newword")
    options,args = parser.parse_args()
    if not options.filename or not options.oldword or not options.newword:
        print "params lack filename or oldword or newword."
        exit()
    replace_keyword_once(options.filename,options.oldword,options.newword)
    replace_keyword_all(options.filename,options.oldword,options.newword)
    
'''
性能慢于sed替换： (test_sed.txt为一个4G大小文件)
date && sed -i "s/INFO/info/g" test_sed.txt && date 
Thu Jul  4 15:31:12 CST 2019
Thu Jul  4 15:32:18 CST 2019
'''
