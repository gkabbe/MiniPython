"""Um Eigenwerte und -vektoren einer Matrix zu bestimmen, gibt es in Numpy schon vorgefertigte
Funktionen"""

import matplotlib.pylab as plt
import numpy as np


# Hilfsfunktion. Nicht weiter beachten..
def plot_vector(*vectors):
    """Zeigt Vektoren grafisch an"""
    start_x = np.zeros(len(vectors), int)
    start_y = np.zeros(len(vectors), int)
    end_x, end_y = zip(*vectors)
    
    plt.quiver(start_x, start_y, end_x, end_y, angles="xy", scale_units="xy", scale=1)
    print(max(end_x), max(end_y))
    plt.xlim(-1, max(end_x) * 2 + 1)
    plt.ylim(-1, max(end_y) * 2 + 1)
    plt.show()



# Beispiel: Matrix, die den y-Wert eines 2D-Vektors mit -1 multipliziert

A = np.array([[1, 0],
              [0, -0.5]])

# Aufgabe:
# * Erzeugen Sie einen Numpy-Array x mit zwei beliebigen Werten. 
# * Erzeugen Sie einen zweiten Array y = A @ x
# * Betrachten Sie die zwei Arrays, indem Sie die Funktion plot_vector aufrufen
# * Wie wirkt die Matrix A auf einen Vektor?
# * Können Sie schon sagen, was die Eigenwerte und -vektoren von A sind?
# * Entfernen Sie die folgenden Kommentare, um sich mithilfe der Funktion np.linalg.eig
#   die Eigenwerte und -vektoren von A berechnen zu lassen


#eigenwerte, eigenvektoren = np.linalg.eig(A)
#print(eigenwerte)

#plot_vector(*eigenvektoren.T)
