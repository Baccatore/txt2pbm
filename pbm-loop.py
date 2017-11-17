import sys
import re

if __name__ == "__main__":
    filenb = sys.argv[1]
    filename = str(filenb) + ".txt"
    cell = [[ 0 for x in range(151)] for y in range(151)]
    
    with open(filename) as f:
        for line in f:
            cord = re.split("\s+",line)
            cord = int(cord)
            cell[int(cord[1])][int(cord[2])] = 1
    print "P1"
    print "151 151"
    for x in range(151):
       record = " ".join(map(str,cell[x]))
       print record

