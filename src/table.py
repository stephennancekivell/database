#!/usr/bin/env python

class table:
    def __init__(self,title):
        self.title=title

class column:
    def __init__(self,label,datatype):
        self.label = label
        self.datatype=datatype

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
