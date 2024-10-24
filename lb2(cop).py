import math as m
b = True
a = 0
x, y = float(input('x=')), float(input('y='))
hp1 = x > y
hp2 = x < y
hp3 = x == y


def fx1(x, y):
    return m.sin(m.radians(y - 0.5 * x))


def fx2(y):
    return m.exp(y)


def fx3(x):
    return m.log(x)


while b:
    gh = input('f1 == 1, f2 == 2, f3 == 3: ')
    if gh == '1':
        a = fx1(x, y)
        b = False
    elif gh == '2':
        a = fx2(y)
        b = False
    elif gh == '3':
        a = fx3(x)
        b = False
    else:
        print('Ошибочкааа')
        gh = ''
if hp1:
    c = y * m.sqrt(a) + 3*m.sin(x)
elif hp2:
    c = x * m.sqrt(a)
elif hp3:
    c = a**1/3 + (x**3)/3
print('c=', c)