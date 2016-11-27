"""Dateien (die z.B. Messwerte enthalten), lassen sich leicht mit numpy einlesen"""
import numpy as np


data = np.loadtxt("messwerte.dat")


# Um eine Datei zu speichern, benutzen Sie savetxt

new_data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

np.savetxt("neue_werte.txt", new_data)
