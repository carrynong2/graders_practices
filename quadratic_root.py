import math
a = float(input())
b = float(input())
c = float(input())
t = math.sqrt((b**2 - 4 * a * c))
x1 = (- b - t)/(2 * a)
x2 = (- b + t)/(2 * a)
x1 = round(x1,3)
x2 = round(x2,3)
print(x1,x2)