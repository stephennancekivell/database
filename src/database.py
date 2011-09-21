#!/usr/bin/env python

import sys
from statement import *

store = {}

class dbase:
    def db_get(self,key):
        if key in store:
            return store[key]
        else:
            raise Exception('key not found, '+key)

    
    def create_table(self, statement1):
        if not isinstance(statement1, createTableStatement):
            raise Exception("need create table statement " +statement1)

        store[statement1.table.title] = statement1.table
        #TODO put to file

    def insert(self,statement1):
        if not isinstance(statement1,insertStatement):
            raise Exception("not insertStatement " + statement1)

        table = store[statement1.table]

        d = {}
        for c,v in statement1.values:    
            d[c]=v

        ins = []
        for i in range(len(table.columns)):
            v = None
            if isinstance(table.columns[i].datatype,string):
                v = d[table.columns[i].label][1:-1]
            elif isinstance(table.columns[i].datatype,integer):
                v = int(d[table.columns[i].label])
            ins.append(v)

        ins = tuple(ins)
        table.data.append(ins)
        #TODO write to file

    def select(self,statement1):
        print statement1
        print statement1.table
        table = store[statement1.table]
        print statement1.expression
        expr = statement1.expression

        results = []

        print expr.left
        print expr.right

        for row in table.data:
            if expr.opp == oppEqual:
                if isinstance(expr.left, string):
                    pass
                print [l.label for l in table.columns]
                #if expr.left in [l in table.columns.labels]:
                    
                pass
            elif isinstance(expr.opp,oppNotEqual):
                pass
            elif isinstance(expr.opp,oppAnd):
                pass
            #if matches row:
                # results.append(row)


    def execute_statement(self,statement1):
        if isinstance(statement1, createTableStatement):
            self.create_table(statement1)
        elif isinstance(statement1, insertStatement):
            self.insert(statement1)
        elif isinstance(statement1, selectStatement):
            self.select(statement1)

    def run_from(self,ioin,ioout):
        for line in ioin:
            #st =statement.build(line)
            #self.execute_statement(st)
            ioout.write(self.run_line(line)+'\n')

    def run_line(self,line):
        return str(self.execute_statement(statement.build(line)))

if __name__=='__main__':
    db = dbase()
    db.run_from(sys.stdin,sys.stdout)
