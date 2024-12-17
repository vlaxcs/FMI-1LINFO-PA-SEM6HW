def computeInput(filename):
    f = open(filename, "r")
    coeffs = [int(x) for x in f.readline().split()]
    x = int(f.readline())
    return coeffs, x

def PPolSortKey(t):
    return -t

def PPol(coefficients):
    coefficients.sort(key = PPolSortKey)
    print(coefficients)
    return coefficients

for file in range(1, 3):
    filename = "Polinom/Tests/" + str(file) + ".in"
    coefficients, x = computeInput(filename)
    print(coefficients, x)
    if (x >= 0):
        ans = PPol(coefficients)
   # else:
   #    ans = NPol(coefficients)

    filename = "Polinom/Tests/" + str(file) + ".out"
    g = open(filename, "w")
    g.close()