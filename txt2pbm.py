# Txt to .pbm converter
# Author: Yuihchiro SUGA
# Organisation: Doshihsa
# Created: 2017-11-17
# Updated: 2017-11-17

import sys
import re

xmax, ymax, zmax = 151, 151, 151

if __name__ == "__main__":
    cell = [[[ 0 for z in range(xmax)] for x in range(ymax)] \
            for y in range(zmax)]
    with open(sys.argv[1]) as f:
        for line in f:
            cord = re.split("\s+",line)
            cord = map(int,cord[1:4])
            print cord
            cell[cord[2]][cord[0]][cord[1]] = 1
    
    for z in range(zmax):
        with open(str(z+1)+".pbm", "w") as of:
            of.write("P1\n")
            of.write(str(xmax)+" "+str(ymax)+"\n")
            for x in range(xmax):
                record = " ".join(map(str,cell[z][x])) + "\n"
                of.write(record)
