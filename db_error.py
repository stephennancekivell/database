#!/usr/bin/env/ python


class KeyNotFoundError(Exception):
    def __init__(self,key):
        self.key = key
    def __str__(self):
        return "KeyNotFound: "+repr(self.key)
