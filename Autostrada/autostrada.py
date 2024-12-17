def intervalsKey(t):
    return t[0], -t[1]

def computeInput(filename):
    f = open(filename, "r")
    length = int(f.readline().strip())
    intervals = []

    for line in f.readlines():
        line = line.split()
        intervals.append((int(line[0]), int(line[1])))
    
    intervals.sort(key=intervalsKey)
    return length, intervals

def sectors(sec, rl):
    damagedSectors = []
    safeSectors = []
    minr = sec[0][0]
    maxr = sec[0][1]
    length = 0
    last = 0

    for i in range(1, len(sec)):
        if sec[i][1] <= maxr:
            continue
        elif sec[i][0] <= maxr:
            maxr = sec[i][1]
        else:
            length += maxr - minr
            safeSectors.append((last, minr))
            damagedSectors.append((minr, maxr))
            last = maxr
            minr = sec[i][0]
            maxr = sec[i][1]

    length += maxr - minr
    safeSectors.append((last, minr))
    damagedSectors.append((minr, maxr))

    if (safeSectors[-1][1] != rl):
        safeSectors.append((maxr, rl))

    return length, damagedSectors, safeSectors

for file in range(1, 5):
    filename = "Autostrada/Tests/" + str(file) + ".in"
    
    roadLength, sec = computeInput(filename)
    roadDamagedLength, roadDamagedSectors, roadSafeSectors = sectors(sec, roadLength)
    roadWear = round((roadDamagedLength * 100 / roadLength))

    filename = "Autostrada/Tests/" + str(file) + ".out"
    g = open(filename, "w")
    for sec in roadDamagedSectors:
        g.write("[{}, {}]\n".format(sec[0], sec[1]))
    g.write("\n")
    for sec in roadSafeSectors:
        g.write("({}, {})\n".format(sec[0], sec[1]))
    g.write("\n{}%".format(roadWear))

g.close()