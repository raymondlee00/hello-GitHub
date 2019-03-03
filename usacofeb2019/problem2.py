"""
ID: RAY2L
LANG: PYTHON2
TASK:
"""

fin = open('revegetate.in', 'r')
fout = open('revegetate.out', 'w')

NMarr = fin.readline().replace('\n', '').split()
N = int(NMarr[0])
M = int(NMarr[1])

favPastures = []
for i in range(0, M):
    el = fin.readline().replace('\n', '').split()
    el.sort()
    el = map(int, el)
    favPastures.append(el)

fout.write(str(favPastures))

result = []

for i in range(0, N):
    result.append(1)

for i in range(0, N):
    checkDigit = 0
    for j in range(0, M):
        if favPastures == i and checkDigit < result[favPastures[j][0]]:
            checkDigit = result[favPastures[j][0]]
    result[i] = checkDigit + 1

fout.write(str(result))

fin.close()
fout.close()
