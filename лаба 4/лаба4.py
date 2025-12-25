#задание 1
from math import sqrt
x = int(input("Введите число: "))
def f(x):
    return sqrt(x)
print(f(x))

from datetime import datetime
today = datetime.now()
print(today)

#задание 2
import my_module

a = my_module.sum(1, 2)
b = my_module.mult(1, 2)
c = my_module.minus(1, 2)

print(a, b, c)

#задание 3
from package1 import *

x = sq_root(9) + square(2)
print(x)
print(greet('Ivan'))
print(describe_person('Ivan', 18))