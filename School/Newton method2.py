from sympy import *

x = Symbol('x')
y = input('Enter your equation in python syntax: y=')


yprime = diff(y, x)

y1 = eval(y)
while True:
    try:
        x = float(input('Enter your initial guess:'))
        break
    except ValueError:
        print('invalid input please try again')

for i in range(5):
    yp1 = yprime.subs(x: x)
    x = x - (y1 / yp1)
print(x)
