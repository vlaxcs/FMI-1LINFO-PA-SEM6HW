from queue import PriorityQueue

def computeInput(filename):
    f = open(filename, "r")
    coeffs = [int(x) for x in f.readline().split()]
    x = int(f.readline())
    return coeffs, x

def maxPoliSortKey(t):
    return -t * x

def maxPoli(coefficients):
    # x > 0
    # abs(a[i]) - max, i % 2 == 0
    # abs(a[i]) - min, i % 2 == 1
    # x < 0
    # abs(a[i]) - min, i % 2 == 0
    # abs(a[i]) - max, i % 2 == 1 
    coefficients.sort(key = maxPoliSortKey)
    return coefficients

for file in range(1, 3):
    filename = "Polinom/Tests/" + str(file) + ".in"
    global x
    coefficients, x = computeInput(filename)
    print(x)
    ans = maxPoli(coefficients)
    print(ans)

    filename = "Polinom/Tests/" + str(file) + ".out"
    g = open(filename, "w")
    for i in range(len(ans) - 1, 0, -1):
        g.write("({})x^{}".format(ans[i], i))
        g.write(" + ")
    g.write("({})".format(ans[0]))
    g.close()