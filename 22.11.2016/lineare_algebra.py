"""Für lineare Algebra gibt es das Modul Numpy, das viele Funktionen schon enthält"""

import numpy as np


# Vektoren lassen sich folgendermaßen erstellen:

x = np.array([1, 2, 3], dtype=int)
y = np.array([3, 4, 7], dtype=float)

print("x =", x)

print("x + x =", x + x)

print("x + y =", x + y)

print("x * y =", x * y)

print("Skalarprodukt von x und y:", x @ y)  # geht nur ab Python 3.5
# Alternativ:
print(np.dot(x, y))

print("Kreuzprodukt:", np.cross(x, y))



# Matrizen funktionieren nach dem selben Prinzip

print("Matrizen:")

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(A)
