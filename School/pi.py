import math
import random
from random import *
from math import *
n = int(input('Number of Trials?'))
inside=0
for i in range(0,n):
	x=random()
	y=random()
	if sqrt(x*x+y*y)<=1:
		inside+=1
pi=4*inside/n
print(pi)
print(math.pi)