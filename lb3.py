import math as m
x1 = 1
xn = 6
step_x = 0.5
a = 0.57
b = 9


def fx(x):
    return (b*m.cos(m.radians(x)))/(1+(a**2)*(m.sin(m.radians(x)))**3)


n = x1
while not n >= xn:
    n += step_x
    print('x= ', round(n, 3), 'f(x) = ', round(fx(n), 7))
