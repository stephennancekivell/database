
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
    def __init__(self,value):
        self.value = value

    @staticmethod
    def build(line):
        line = line.strip()
        #if line[0] == '('

        return None
