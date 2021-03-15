import math

def CalcPi(n):
    t = 0
    xi = 0
    yi = 1
    for i in range(n):
        v = xi
        z = yi
        xi = i * (1/n)
        yi = math.sqrt(1 - xi**2)
        li = math.sqrt(((xi - v)**2) + ((yi - z)**2))
        t += li
    return 2 * t

print("{}".format(CalcPi(4000000)))
