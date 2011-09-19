#!/usr/bin/env python

from db_datatypes import *
from db_opperators import *

class statement:
    """
    meta statement.
    """
    @staticmethod
    def build(line):
        lineSplit = line.split()
        if lineSplit[0] == 'create_table':
            table = lineSplit[1]
            cts = line[line.index('('):line.index(')')].split(',')
            column_type = map(lambda kv: kv.split(), cts)
            return createTableStatement(table,column_type)
        elif lineSplit[0] == 'insert':
            table = lineSplit[1]
            cvs = line[line.index('('):line.index(')')].split(',')
            column_value = map(lambda kv: kv.split(), cvs)
            return insertStatement(table,column_value)
        elif lineSplit[0] == 'select':
            table = lineSplit[1]
            line = line[line.index(table)+len(table)+1:]
            e = expression.build(line)
            return e

class insertStatement(statement):
    def __init__(self,table, variables):
        self.table = ""
        self.variables = variables # a list of tuples [(column,value),..]

class createTableStatement(statement):
    def __init__(self, table_name, column_type):
        self.table_name = table_name
        self.column_type = column_type # ordered_tuple like ((key, int), (name,string), ..)

class select(statement):
    def __init__(self,table, expression):
        self.table = table
        self.expression = expression

class expression(statement):
    def __init__(self,opp, left, right):
        self.opp = opp
        self.left = left
        self.right = right

    @staticmethod
    def build(line):
        return expression.extractExpression(line)[0]
        

    @staticmethod
    def extractExpression(line):
        print "extractExpression",line

        line = line.strip()
        if line[0] =='(':
            line = line[1:]
        else:
            raise Exception('why isnt there a (')
        
        #left
        left,line = expression.extractVar(line)
        print "left", left

        #opp
        opp, line = expression.extractOpp(line)
        print "opp",opp

        #right
        right,line = expression.extractVar(line)
        print "right",right

        line = line.strip()
        if line[0]==')':
            line = line[1:]
        else:
            raise Exception('why isnt there a )')

        print "expression parsed", left,opp,right
        return expression(opp,left,right),line

    @staticmethod
    def extractVar(line):
        line = line.strip()
        print 'extractVar ',line
        if line[0]=='(':
            var, line = expression.extractExpression(line)
            line =line.strip()
        elif line[0]=="\"":
            # its a 'string'
            print "string", line
            line = line[1:] # advance the first "
            var = line[:line.index("\"")]
            var = string(var)
            line = line[len(var)+1:]
            
        else: #column or number
            lsplit = line.split()
            var = lsplit[0]
            try:
                varn = number(var)
            except ValueError:
                var = lsplit[0]

            line = line[line.index(var)+len(var)+1:]

        return var,line

    @staticmethod
    def extractOpp(line):
        line = line.strip()
        if line[:1] == '=':
            return oppEqual, line[1:]
        elif line[:2] == '!=':
            return oppNotEqual, line[2:]
        elif line[:2] == '&&':
            return oppAnd, line[2:]
        else:
            raise Exception('couldnt find opp' + line)