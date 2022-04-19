import math

def compoundInterest(p, r, n, t):
    return round(math.pow((r/n + 1), (n*t))*p, 2)
    
print(compoundInterest(5000, 0.03, 12, 6))