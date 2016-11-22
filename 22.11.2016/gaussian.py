"""Funktionen numerisch auswerten in Numpy"""

# Wie wir schon gesehen haben, rechnet Numpy vektoriell, d.h. Operationen wie z.B +, -, /, etc.
# werden auf jedes Element in einem Vektor angewendet
# Das selbe gilt auch für Funktionen wie z.B. sin, cos, exp, etc.

import numpy as np
import matplotlib.pylab as plt   # Ermöglicht uns, die Funktionen grafisch anzuzeigen

# Zuerst brauchen wir einen x-Achsen Abschnitt:

# Erzeuge einen Vektor mit Werten von 0 bis 2 pi mit insgesamt 100 Werten
x = np.linspace(0, 2 * np.pi, 100)
# Erzeuge die Werte einer Sinus-Funktion, die von 0 bis 2 pi läuft
y = np.sin(x)

plt.plot(x, y)
plt.show()



# Aufgabe:
# Schreiben Sie eine Funktion gaussian, die die Parameter x, center und sigma entgegennimmt und
# plotten Sie die Funktion
# Bestimmen Sie das Integral der Funktion mithilfe von np.trapz (Trapezregel)
# Vergewissern Sie sich (grafisch), dass das Produkt zweier Gaussians wieder ein Gaussian ist
