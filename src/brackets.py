#!/usr/bin/env python

line = "(oauu ( eou ( oe ) htsn ))"

print line

def pb3(line):
    depth=0
    while len(line) != 0:
        if '(' in line:
            istart = line.index('(')
            if ')' in line:
                iend = line.index(')')
                if istart < iend:
                    print depth*' '+line[:istart+1]
                    line = line[istart+1:]
                    depth+=1
                    continue
                else:
                    print depth*' '+line[:iend+1]
                    line = line[iend+1:]
                    depth-=1
                    continue
        if ')' in line:
            iend = line.index(')')
            print depth*' '+line[:iend+1]
            line = line[iend+1:]
            depth-=1
        else:
            print depth*' '+line
            line = ""

pb3(line)
