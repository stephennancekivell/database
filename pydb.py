#!/usr/bin/env python

import sys
from db_error import *
from db_statement import *

store = {}

class dbase:
    def db_put(self,key,value):
        store[key]=value

    def db_get(self,key):
        if key in store:
            return store[key]
        else:
            raise KeyNotFoundError(key)

    def parse_line(self,line):
        x = line.split()
        if x[0] == 'put':
            return self.db_put(x[1],x[2])
        elif x[0] == 'get':
           return self.db_get(x[1])

    def run_from(self,ioin,ioout):
        for line in ioin:
            r =statement.build(line)
            #r = self.parse_line(line)
            ioout.write(str(r)+'\n')

if __name__=='__main__':
    db = dbase()
    db.run_from(sys.stdin,sys.stdout)
