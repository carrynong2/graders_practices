v1 = input()[1:-1].split(",")
v2 = input()[1:-1].split(",")
v1 = [float(v1[0]), float(v1[1]), float(v1[2])]
v2 = [float(v2[0]), float(v2[1]), float(v2[2])]
v3 = [v1[0] + v2[0] , v1[1] + v2[1], v1[2] + v2[2]]
print(v1,"+",v2,"=",v3)  