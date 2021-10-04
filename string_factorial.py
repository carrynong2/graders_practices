import math
n = int(input())
s = math.sqrt(2*math.pi) * n**(n+1/2)
lower = s * math.e**(-n + 1 / (12 * n + 1))
upper = s * math.e**(-n + 1 / (12 * n))
print(lower)
print(upper)