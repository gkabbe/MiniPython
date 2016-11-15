"""Ähnlich wie in der Mathematik kann man in Python Funktionen definieren, die eine Eingabe
erwarten und eine Ausgabe dazu liefern.
Funktionen erlauben es, Code-Bausteine wiederzuverwenden und sorgen so für eine aufgeräumte 
Code-Struktur."""


# Um eine Funktion zu schreiben, wird das Keyword "def" benötigt
# Dann kommt der Name der Funktion, und schließlich in Klammern die erwarteten Argumente

# Bsp: Funktion, die zwei Zahlen addiert

def meine_funktion(zahl_1, zahl_2):
    # Wichtig: Python arbeitet mit Einrückungen. Alles, was nach der Funktionsdefinition eingerückt
    # ist, gehört zur Funktion
    summe = zahl_1 + zahl_2
    return summe   # Mit return können wir festlegen, was die Funktion zurückgibt
    
# Ab hier hört die Funktion auf, weil es keine Einrückung mehr gibt

a = 5
b = 10
print(meine_funktion(a, b))   # Hier übergeben wir der Funktion zwei Variablen

print(meine_funktion(12, 13)) # Wir können aber auch direkt die Werte einfügen



# Aufgabe 1: Schreiben Sie eine Funktion, die das Produkt von drei Zahlen zurückgibt

# Aufgabe 2: Schreiben Sie eine Funktion, die den Betrag einer Zahl zurückgibt

# Aufgabe 3: Schreiben Sie die Fakultätsfunktion fak(n), die für eine Zahl n die Fakultät
# n! = n * (n - 1) * (n - 2) * ... * 1 berechnet
