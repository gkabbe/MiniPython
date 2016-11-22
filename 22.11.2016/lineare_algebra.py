"""Für lineare Algebra gibt es das Modul Numpy, das viele Funktionen schon enthält"""

import numpy as np


# Vektoren lassen sich folgendermaßen erstellen:

x = np.array([1, 2, 3], dtype=int)  # ein Array aus Ganzzahlen (Integern)
y = np.array([3, 4, 7], dtype=float)  # ein Array aus Gleitkommazahlen (Floats)

print("x =", x)
print()
print("x + x =", x + x)
print()
print("x + y =", x + y)
print()
print("x * y =", x * y)
print()

print("Skalarprodukt von x und y:", x @ y)  # geht erst ab Python 3.5
# Alternativ:
print(np.dot(x, y))

print("Kreuzprodukt:", np.cross(x, y))
print()
print()


# Matrizen funktionieren nach dem selben Prinzip

print("Matrizen:")

A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])
              
I = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

print("A =")
print(A)
print()
print("I =")
print(I)
print()
print("A * I =")
print(A @ I)   # Matrixmultiplikation. Alternative wieder np.dot(A, I)
print()
print("Elementweises Produkt:")
print(A * I)


# Determinante

print("A =")
print(A)
print("det(A) =", np.linalg.det(I))

print()
print()

# Auf einzelne Elemente eines Vektors / einer Matrix zugreifen:

x = np.linspace(0, 10, 50)  # dieser Befehl erzeugt einen Array der Länge 50 mit Werten von 0 bis 10

print("x =", x)
print("x[0] =", x[0])  # gibt das erste Element aus
print("x[-1] =", x[-1]) # gibt das letzte Element aus

print()
print()
# Ähnlich bei einer Matrix:

# Folgender Befehl gibt den Eintrag der 0. Zeile und 0. Spalte aus (Nummeriert wird immer von 0 aus!)
print("A[0, 0] =", A[0, 0])  
# gibt den Eintrag der 1. Zeile und der letzten, d.h. der 2. Spalte aus
print("A[1, -1] =", A[1, -1])


# Was, wenn wir auf die gesamte erste Spalte von A zugreifen wollen?
# -> Slicing
print("A[:, 0] =", A[:, 0])  #  bedeutet: gib jede Zeile der nullten Spalte aus
print()
# Wenn wir nur einen Teil der ersten Spalte wollen, z.B. alles bis auf das letzte Element?
print("A[:2, 0] =", A[:2, 0])
print()

# Slicen geht auch in mehreren Dimensionen gleichzeitig:
# Mache aus der 3x3 Matrix A eine 2x2 Matrix:

print("A[:2, :2] =")
print(A[:2, :2])

# Aufgabe 1:
# Schreiben Sie eine eigene Funktion det, die die Determinante einer 2x2 Matrix berechnet

# Aufgabe 2:
# Schreiben Sie eine Funktion, die eine 2x2 Matrix invertiert
