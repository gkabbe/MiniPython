"""Für lineare Algebra gibt es das Modul Numpy, das viele Funktionen schon enthält"""

import numpy as np


# Vektoren lassen sich folgendermaßen erstellen:

x = np.array([1, 2, 3], dtype=int)
y = np.array([3, 4, 7], dtype=float)

print("x =", x)

print("x + x =", x + x)

print("x + y =", x + y)

print("x * y =", x * y)

print("Skalarprodukt von x und y:", x @ y)  # geht erst ab Python 3.5
# Alternativ:
print(np.dot(x, y))

print("Kreuzprodukt:", np.cross(x, y))



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
print("det(A) =")
print(np.linalg.det(I))


# Auf einzelne Elemente eines Vektors / einer Matrix zugreifen:

x = np.linspace(0, 10, 50)  # dieser Befehl erzeugt einen Array der Länge 50 mit Werten von 0 bis 10

print(x[0])  # gibt das erste Element aus
print(x[-1]) # gibt das letzte Element aus


# Ähnlich bei einer Matrix:

# Folgender Befehl gibt den Eintrag der 0. Zeile und 0. Spalte aus (Nummeriert wird immer von 0 aus!)
print("A[0, 0] =", A[0, 0])  
# gibt den Eintrag der 1. Zeile und der letzten, d.h. der 2. Spalte aus
print("A[1, -1] =", A[1, -1])



# Aufgabe 1:
# Schreiben Sie eine eigene Funktion det, die die Determinante einer 2x2 Matrix berechnet

# Aufgabe 2:
# Schreiben Sie eine Funktion, die eine 2x2 Matrix invertiert


