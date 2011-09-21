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

    def create_table(self, statement1):
        if not isinstance(statement1, createTableStatement):
            raise Exception("need create table statement " +statement1)

        store[statement1.table.title] = statement1.table
        #TODO put to file

    def insert(self,statement1):
        print 'yay'
        print statement1.table
        print statement1.values


    def execute_statement(self,statement1):
        if isinstance(statement1, createTableStatement):
            self.create_table(statement1)
        if isinstance(statement1, insertStatement):
            self.insert(statement1)
        

    def run_from(self,ioin,ioout):
        for line in ioin:
            st =statement.build(line)
            self.execute_statement(st)
            ioout.write(str(st)+'\n')

if __name__=='__main__':
    db = dbase()
    db.run_from(sys.stdin,sys.stdout)
