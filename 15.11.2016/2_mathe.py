"""Python lässt sich wie ein Taschenrechner benutzen."""

print("1 + 1 =", 1 + 1)

print("7 / 2 =", 7 / 2)

print("4 * (325/12 + 143) =", 4 * (325/12 + 143))

print("10 modulo 3 =", 10 % 3)

print("2 hoch 10 =", 2**10)

# Für weitere mathematische Funktionen müssen wir das Paket Numpy laden, das viele weitere 
# mathematische Funktionen enthält

import numpy as np

print("Wurzel aus 3 =", np.sqrt(3))

# Oder alternativ (ohne Numpy):
print("Wurzel aus 3 =", 3**0.5)

