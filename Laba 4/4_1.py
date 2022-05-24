from scipy import integrate
import numpy as np
f = lambda x, y, z : x
g = lambda x : 0
h = lambda x : (1 - x) / 2
q = lambda x, y : 0
r = lambda x, y : 1 - x - 2 * y
v, err = integrate.tplquad(f, 0, 1, g, h, q, r)
print(v)