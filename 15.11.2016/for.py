"""Bei sich wiederholenden Aufgaben sind for-Schleifen hilfreich, da sie es erlauben, einen
Befehl bzw. eine Reihe von Befehlen mehrmals hintereinander auszuführen"""


# Aufgabe: Schreiben Sie ein Programm, das die Zahlen von 0 bis 9 ausgibt




# Ziemlich mühsam, oder?
# Einfacher geht es mit einer for-Schleife:

for i in range(10):   # Anstelle von i kann man auch einen anderen beliebigen Namen benutzen
    print(i)

# Das Programm besteht nur aus zwei Zeilen Code, tut aber genau das, was wir wollen
# Was passiert hier? Innerhalb der for-Schleife wird die Variable i erzeugt. Diese startet mit
# dem Wert Null und wird mit jedem Schleifendurchlauf um eins erhöht


# Anstelle der range Funktion kann man auch eine sogenannte Liste definieren und über diese iterieren:

meine_liste = [1, 2, 3, "a", "b", "c", "usw.", ["noch eine Liste in der Liste", 7, 8, 9]]

print("Inhalt meiner Liste:")

for item in meine_liste:
    print(item)



# Aufgabe 1: Berechnen Sie die Summe der Zahlen von 1 bis 100


# Aufgabe 2: Berechnen Sie die Quadratzahlen von 1**2 bis 100**2


# Aufgabe 3: Geben Sie alle durch 7 teilbaren Zahlen zwischen 1 und 100 aus


# Aufgabe 4: Berechnen Sie die Fibonacci Folge. 
# Für die n. Zahl in der Folge gilt: f_n = f_{n-2} + f_{n-1}, d.h. die n. Zahl ist die Summe aus
# der (n - 2). und der (n - 1). Zahl
