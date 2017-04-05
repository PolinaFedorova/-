import math
v1 = float(input("v1 = "))
v2 = float(input("v2 = "))
v3 = float(input("v3 = "))
r1=math.pow((v1/math.pi)*(3/4),(1/3))
r2=math.pow((v2/math.pi)*(3/4),(1/3))
r3=math.pow((v3/math.pi)*(3/4),(1/3))
z = (r1+r2+r3)/3
print (z)
