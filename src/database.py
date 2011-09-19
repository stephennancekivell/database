#!/usr/bin/env python

import sys
from statement import *

store = {}

class dbase:
    def db_put(self,key,value):
        store[key]=value

    def db_get(self,key):
        if key in store:
            return store[key]
        else:
            raise Exception('key not found, '+key)

    def parse_line(self,line):
        x = line.split()
        if x[0] == 'put':
            return self.db_put(x[1],x[2])
        elif x[0] == 'get':
           return self.db_get(x[1])

    def execute_statement(self,statement1):
        if isinstance(statement1, createTableStatement):
            
            print 'yay'
        
        pass

    def run_from(self,ioin,ioout):
        for line in ioin:
            st =statement.build(line)
            self.execute_statement(st)
            ioout.write(str(st)+'\n')

if __name__=='__main__':
    db = dbase()
    db.run_from(sys.stdin,sys.stdout)
