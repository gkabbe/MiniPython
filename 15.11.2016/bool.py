"""Boolesche Ausdrücke und if-Statements

Bisher waren unsere Programme noch recht simpel gestrickt und waren nicht in der Lage, mehr als ein
gewöhnlicher Taschenrechner zu machen.
Hier wird nun gezeigt, wie man ein Programm schreibt, das gewissermaßen Entscheidungen treffen kann,
d.h. auf unterschiedliche Situationen unterschiedlich reagiert.

Zuerst müssen wir dafür Boolesche Ausdrücke verstehen. Das sind "Aussagen", die entweder wahr 
(True) oder falsch (False) sind.

Ein if-Statement erlaubt uns dann, anhand eines Booleschen Ausdrucks zu entscheiden, wie sich das 
Programm im weiteren Verlauf verhält.
"""


# Boolesche Ausdrücke

print(4 + 4 == 8) 

# Hier wurde der Vergleichsoperator "==" benutzt. Er vergleicht den Wert der linken und der rechten
# Seite und gibt True zurück wenn beide Seiten gleich sind. Ansonsten False
# Wie immer können wir das Ergebnis in einer Variablen speichern:

boolescher_wert = 4 + 4 == 8
print(boolescher_wert)


# Es gibt noch weitere Vergleichsoperatoren:

# kleiner/größer:
print("3 + 3 < 7 ->", 3 + 3 < 7)
print("4 + 4 > 10 ->", 4 + 4 > 10)

# kleiner gleich / größer gleich:
print("4 <= 5 ->", 4 <= 5)
print("8 >= 8 ->", 8 >= 8)

# ungleich:
print("3 + 3 != 12 ->", 3 + 3 != 12)


# Darüberhinaus gibt es die booleschen Operatoren "and", "or" und "not":

# "and" gibt genau dann True zurück wenn beide Argumente True sind, ansonsten False
print("True and False ->", True and False)
print("True and True ->", True and True)
print("False and False ->", False and False)

# "or" gibt genau dann True zurück wenn mindestens eines der beiden Argumente True ist, ansonsten 
# False

print("True or False ->", True or False)
print("False or False ->", False or False)
print("usw.")


# Statt direkt True oder False zu benutzen, können wir natürlich auch einen booleschen Ausdruck
# verwenden

x = 
print("Liegt x zwischen 0 und 10?")
print(x > 0 and x < 10)


# Wir können nun ein if - Statement benutzen, um einen booleschen Ausdruck auszuwerten und dann
# zu entscheiden, wie der weitere Programmablauf ist:

x = 
print("x =", x)
print("Liegt x zwischen 0 und 10?")
if 0 < x < 10:
    print("Ja!")
else:
    print("Nein")
    
    
# Wenn es mehr als zwei mögliche Entscheidungen gibt, kann man elif verwenden:

punkte = 

if punkte >= 90:
    print("Sehr gut!")
elif punkte >= 80:
    print("Gut")
elif punkte >= 70:
    print("Befriedigend")
elif punkte >= 60:
    print("Ausreichend")
else:
    print("Durchgefallen...")
    

# Aufgabe 1: Schreiben Sie ein Programm, das entscheidet, ob die Variable x durch 3 teilbar ist

# Aufgabe 2: 

# Gegeben seien die Variablen

#   student_motiviert = True
#   student_ausgeschlafen = False
#   unterricht_spannend = True

# Welchen Wert hat python lernerfolg = student_ausgeschlafen or (student_motiviert and unterricht_spannend) ?

# Schreiben Sie ein Programm, das
