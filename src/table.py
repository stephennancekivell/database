#!/usr/bin/env python

class table:
    pass

class column:
    pass


class datatype:
    """
    meta class for datatypes
    """
    disk_size=0 # number of bytes

class string(datatype):
    disk_size=200
    def __init__(self,value):
        self.value=value
    def __len__(self):
        return len(self.value)

class number(datatype):
    disk_size=4
    def __init__(self,value):
        self.value=value
