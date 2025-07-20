import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

soma = v1 + v2
sub = v1 - v2

dot = np.dot(v1, v2)

norma = np.linalg.norm(v1)

print(f"v1 = {v1}")
print(f"v2 = {v2}")

print(f"Soma: {soma}")
print(f"Sub: {sub}")

print(f"Produto escalar: {dot}")
print(f"Norma: {norma}")
