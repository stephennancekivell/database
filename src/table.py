#!/usr/bin/env python

class table:
    def __init__(self,title, columns):
        self.title=title
        self.columns = columns # order list of column
        self.data = [] # the row object entries

    def __str__(self):
        return "<%s %d: %s>" % (self.__class__,id(self), self.title)

class column:
    def __init__(self,label,datatype):
        self.label = label
        self.datatype=datatype

    def __str__(self):
        return "<%s %d: %s>" % (self.__class__, id(self), self.label)

class row:
    def __init__(self,columns,data):
        self.data = data # a ordered tuple that matches the columns

class datatype:
    """
    meta class for datatypes
    """
    disk_size=0 # number of bytes

    @staticmethod
    def build(keyword):
        types = [integer,string]
        for t in types:
            if t.keyword==keyword:
                return t(keyword)
 
class string(datatype):
    keyword = 'string'
    disk_size=200
    def __init__(self,value):
        self.value=value
    def __len__(self):
        return len(self.value)

class integer(datatype):
    keyword='int'
    disk_size=4
    def __init__(self,value):
        self.value=value
