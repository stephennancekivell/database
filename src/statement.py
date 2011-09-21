#!/usr/bin/env python

from table import *

class statement:
    """
    meta statement.
    """
    @staticmethod
    def build(line):
        lineSplit = line.split()
        if lineSplit[0] == 'create_table':
            return createTableStatement(line)
        elif lineSplit[0] == 'insert':
            return insertStatement(line)
        elif lineSplit[0] == 'select':
            table = lineSplit[1]
            line = line[line.index(table)+len(table)+1:]
            e = expression.build(line)
            return selectStatement(table,e)

class insertStatement(statement):
    statement_title = 'insert'

    def __init__(self,line):
        if line[:len(self.statement_title)] != self.statement_title:
            raise Exception('not insert command: '+line)

        line = line[len(self.statement_title):]
        lineSplit = line.split()
        self.table = lineSplit[0]
        line = line[line.index(self.table)+len(self.table)+1:]
        cvs = line[line.index('(')+1:line.index(')')].split(',')
        cv2 = []
        for cv in cvs:
            cv = cv.strip()
            column = cv.split()[0]
            value = cv[cv.index(column)+len(column):].strip()
            #check datatype
            cv2.append((column,value))
        self.values =cv2

class createTableStatement(statement):
    statement_title = 'create_table'

    def __init__(self, line):
        print 'create'
        print line
        if line[:len(self.statement_title)] != self.statement_title:
            raise Exception('not createTable command: '+line)
        lineSplit = line[len(self.statement_title):].split()
        table_name = lineSplit[0]
        cvs = line[line.index('(')+1:line.index(')')].split(',')
        column_value = map(lambda kv: kv.split(), cvs)
        cv2 = []
        for c,v in column_value:
            cv2.append(column(c,datatype.build(v)))

        self.table = table(table_name, cv2)

class selectStatement(statement):
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
        line = line.strip()
        if line[0] =='(':
            line = line[1:]
        else:
            raise Exception('why isnt there a (')
        
        left,line = expression.extractVar(line)

        opp, line = expression.extractOpp(line)

        right,line = expression.extractVar(line)

        line = line.strip()
        if line[0]==')':
            line = line[1:]
        else:
            raise Exception('why isnt there a )')

        return expression(opp,left,right),line

    @staticmethod
    def extractVar(line):
        line = line.strip()
        if line[0]=='(':
            var, line = expression.extractExpression(line)
            line =line.strip()
        elif line[0]=="\"": # its a 'string'
            line = line[1:] # advance the first "
            var = line[:line.index("\"")]
            var = string(var)
            line = line[len(var)+1:]
            
        else: #column or number
            lsplit = line.split()
            var = lsplit[0]
            try:
                varn = integer(var)
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

################# statements #################

class oppEqual:
    pass

class oppNotEqual:
    pass

class oppAnd:
    pass
