import math as m
x, y, z = float(input('x=')), float(input('y=')), float(input('z='))
a = m.log(y**(abs(x)**1/2))
b = x - y/2
c = m.sin(m.radians(m.atan(z))**2)
s = a*b + c
print('s=', round(s, 10))