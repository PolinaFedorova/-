import math
p = float(1.6)
x = float(input("x = "))
b = (math.pow(x,4))+(math.log10(math.pow(p,3)))
print ('b = ',b)
a = (math.log(math.fabs(x)))
print ('a = ',a)
print ('y = ', (math.pow(math.sin(a*x),3)+math.sqrt(b)*math.cos(math.pow(x,2))))

