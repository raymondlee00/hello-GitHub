"""
ID: RAY2L
LANG: PYTHON2
TASK: Sleepy Cow Herding
"""

fin = open('herding.in', 'r')
fout = open('herding.out', 'w')

cowInts = fin.readline()
cowInts = cowInts.split()

cowInts.sort()

cowInts = map(int, cowInts)

def minCow(small, mid, large):
    diff0 = mid - small
    diff1 = large - mid
    if diff0 == 1 and diff1 == 1:
        return 0
    elif diff0 == 2 or diff1 == 2:
        return 1
    else:
        return 2

def maxCow(small, mid, large):
    diff0 = mid - small
    diff1 = large - mid
    if diff0 > diff1:
        return diff0 - 1
    else:
        return diff1 - 1

fout.write(str(minCow(cowInts[0], cowInts[1], cowInts[2])) + '\n')
fout.write(str(maxCow(cowInts[0], cowInts[1], cowInts[2])))
fin.close()
fout.close()
