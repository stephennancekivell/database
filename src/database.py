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
        print "SELECT %s" % statement1
        table = store[statement1.table]
        expr = statement1.expression
        results = []
        
        # to use
        #left,right = None,None
        #lref,rref = True,True # refresh for each row.

        #if isinstance(expr.right,datatype):
        #    right = expr.right.getValue()
        #    rref = False
        #if isinstance(expr.left,datatype):
        #    left = expr.left.getValue()
        #    lref = False

        for row in table.data:
            # so much can be optimized with this.
            # column index's dont change.
            # raw values dont change.
            if dbase.expression_matches(expr.left,expr.right,expr.opp,row,table):
                results.append(row)

        return results #todo classify

    @staticmethod
    def expression_matches(leftV,rightV,opp,row,table):
        """does the expression match the row """
        if isinstance(leftV,expression):
            leftV = dbase.expression_matches(leftV.left,leftV.right,leftV.opp,row,table)
        if isinstance(rightV,expression):
            rightV = dbase.expression_matches(rightV.left,rightV.right,rightV.opp,row,table)

        if isinstance(leftV,datatype): leftV=leftV.getValue()
        else:
            i = table.columnIndex(leftV)
            if i==None: raise Exception("not a column, leftV",leftV)
            leftV = row[i]

        if isinstance(rightV,datatype): rightV=rightV.getValue()
        else:
            i = table.columnIndex(rightV)
            if i==None: raise Exception("not a column, rightV",rigthV)
            rightV = row[i]

        if opp == oppEqual:
            matches = leftV==rightV
        elif opp == oppNotEqual:
            matches = leftV != rightV
        elif opp == oppAnd:
            matches = leftV & rightV
        else:
            raise Exception("opp not an opp?", opp)

        return matches

    def execute_statement(self,statement1):
        if isinstance(statement1, createTableStatement):
            self.create_table(statement1)
        elif isinstance(statement1, insertStatement):
            self.insert(statement1)
        elif isinstance(statement1, selectStatement):
            print self.select(statement1)

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
