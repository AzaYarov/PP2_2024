# [выражение for i in коллекция]

import random

a = [i**2 for i in range(7)]

print(a)

b = [i for i in "Hello"]

print(b)

c = [random.randint(-10, 10) for i in range(10)]

print(c)

